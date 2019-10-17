import subprocess
import tempfile
from qgis.processing import alg
from qgis.core import QgsRasterLayer, QgsSettings, QgsProcessingOutputRasterLayer

import processing


@alg(name='raster2postgis', label='Raster nach Postgis', group='opengeoedu', group_label='OpenGeoEdu')
@alg.input(type=alg.STRING, name='dbverbindungsname', label='db Verbindungsname')
@alg.input(type=alg.STRING, name='dbschema', label='db Schema')
@alg.input(type=alg.STRING, name='dbtabelle', label='db Tabellenname')
@alg.input(type=alg.FILE, name='raster2psql', label='Pfad zur Datei \'raster2psql\'', default="raster2pgsql")
@alg.input(type=alg.STRING, name='args', label='Argumente für raster2psql', optional=True)
@alg.input(type=alg.RASTER_LAYER, name='raster', label='Input raster')
@alg.output(type=alg.RASTER_LAYER, name='output', label='Output raster')
def raster2postgis(instance, parameters, context, feedback, inputs):
    """
    Dies ist eine Proxy-Script der ein gegebenes Rasterfile mithilfe des Kommandozeilen-Tools raster2psql in eine Postgis-Datenbank exportiert
    """

    RASTER_PATH = instance.parameterAsFileOutput(parameters, 'raster', context)
    RASTER2PGSQL_PATH = instance.parameterAsFileOutput(parameters, 'raster2psql', context)
    RASTER2PGSQL_ARGUMENTS = instance.parameterAsFileOutput(parameters, 'args', context)
    DB_VERBINDUNGSNAME = instance.parameterAsString(parameters, 'dbverbindungsname', context)
    DB_TABLENAME = instance.parameterAsString(parameters, 'dbtabelle', context)
    DB_SCHEMA = instance.parameterAsString(parameters, 'dbschema', context)

    with tempfile.NamedTemporaryFile(mode="w+t", suffix=".sql") as tmp:
        cmd_args = filter(None, [RASTER2PGSQL_PATH, RASTER2PGSQL_ARGUMENTS, RASTER_PATH, DB_SCHEMA + "." + DB_TABLENAME,
                                 "> " + tmp.name])
        cmd = " ".join(cmd_args)
        feedback.setProgressText("Führe raster2psql aus: \n\t" + cmd)
        MyOut = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        stdout, stderr = MyOut.communicate()
        feedback.setProgressText(str(stdout))
        feedback.setProgressText(str(stderr))
        sql_cmd = tmp.read()
        if not len(sql_cmd):
            raise processing.QgsProcessingException("raster2psql hat anscheinend keine SQL-Befehle generiert")
        feedback.setProgressText("SQL Befehle wurden generiert und werden an die Datenbank übermittelt.")
        if feedback.isCanceled():
            return {}
        try:
            processing.run("qgis:postgisexecutesql", {'DATABASE': DB_VERBINDUNGSNAME, 'SQL': sql_cmd},
                           is_child_algorithm=True,
                           context=context,
                           feedback=feedback)
        except Exception as error:
            raise processing.QgsProcessingException(
                "Ein Fehler ist beim Senden der SQL-Anfrage aufgetreten: \n\t" + str(error))
        finally:
            tmp.close()
        feedback.setProgressText("Rasterdaten wurden an die Datenbank übermittelt. Lade Layer.")
        if feedback.isCanceled():
            return {}
        rasterLayer = createRasterLayer(DB_VERBINDUNGSNAME, DB_SCHEMA, DB_TABLENAME, feedback)
        rasterid = context.temporaryLayerStore().addMapLayer(rasterLayer).id()
        feedback.setProgressText("Registered layer with id " + str(rasterid))

        context.addLayerToLoadOnCompletion(
            rasterid,
            processing.QgsProcessingContext.LayerDetails('SQL layer',
                                                         context.project(),
                                                         'output'))
    return {'output': rasterid}


def createRasterLayer(DB_VERBINDUNGSNAME, DB_SCHEMA, DB_TABLENAME, feedback):
    settings = QgsSettings()

    settings.beginGroup(u"/PostgreSQL/connections/%s" % DB_VERBINDUNGSNAME)
    settingsList = ["service", "host", "port", "database", "username", "password", "authcfg", "sslmode"]
    quotesettings = ["service", "host", "database", "authcfg", "sslmode"]
    config = {}
    for key in settingsList:
        value = settings.value(key, "", type=str)
        if key == "database":
            config["dbname"] = "'" + value + "'"
            continue
        if value == "":
            continue
        if key in quotesettings:
            config[key] = "'" + value + "'"
        else:
            config[key] = value
    settings.endGroup()

    config["mode"] = "2"
    config["schema"] = "'" + DB_SCHEMA + "'"
    config["table"] = "'" + DB_TABLENAME + "'"
    config["column"] = "'rast'"

    conn_string = "PG:"

    for key, value in config.items():
        conn_string += " " + key + "=" + value + ""

    layer = QgsRasterLayer(conn_string, DB_TABLENAME)
    feedback.setProgressText("Lade layer with connection: "+conn_string+"\n and tablename: "+DB_TABLENAME)
    if not layer.isValid():
        raise processing.QgsProcessingException("Der Layer kann nicht aus der Datenbank geladen werden!")
        return None
    return layer
