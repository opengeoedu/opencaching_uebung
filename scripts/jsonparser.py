#!/usr/bin/python3

import json
import re
import tarfile
import uuid
import processing
from datetime import datetime

from qgis.processing import alg


def postgis_insert(DB_VERBINDUNGSNAME, db_table, db_entry, context, feedback):
    try:

        sql_insert = "INSERT INTO "+db_table+" (" + ", ".join(db_entry.keys()) + ")\n" +\
                     "\tVALUES ('" + "', '".join(db_entry.values()) + "')\n" +\
                     "RETURNING id;"
        sql_insert = sql_insert.replace("'NULL'","NULL")
        processing.run("qgis:postgisexecutesql", {'DATABASE': DB_VERBINDUNGSNAME, 'SQL': sql_insert},
                       is_child_algorithm=True,
                       context=context)
    except Exception as error:
        feedback.setProgressText("Ein Fehler ist beim Senden der SQL-Anfrage aufgetreten (INSERT-statement): n\t" + str(error))
        feedback.setProgressText("Dateneintrag: "+ str(db_entry))
    return


@alg(name='oc_parser', label='OKAPI JSON-Parser', group='opengeoedu', group_label='OpenGeoEdu')
@alg.input(type=alg.FILE, name='DB_DUMP', label='Datenbanken-Abbild als ZIP-Archiv')
@alg.input(type=alg.STRING, name='dbverbindungsname', label='Postgis-DB Verbindungsname', default="db_opengeoedu")
@alg.input(type=alg.STRING, name='dbschema', label='db Schema', default="oc")
@alg.input(type=alg.STRING, name='dbtabelle_caches', label='db Tabellenname für Caches', default="geocaches")
@alg.input(type=alg.STRING, name='dbtabelle_protection', label='db Tabellenname für Schutzgebiete', default="schutzgebiete")
@alg.output(type=alg.NUMBER, name='status', label='Status Code')


def oc_parser(instance, parameters, context, feedback, inputs):
    """
    Dieses Python-Script liest aus Daten einem tar-komprimierten Abbild OpenCaching Datenbank Standorte und Attribute von Geocaches sowie Schutzgebieten ein und schreibt diese informationen jeweils in eine Tabelle der angegebenen Postgis-Datenbank
    """
    DB_DUMP_PATH = instance.parameterAsFileOutput(parameters, 'DB_DUMP', context)
    DB_VERBINDUNGSNAME = instance.parameterAsString(parameters, 'dbverbindungsname', context)
    DB_TABLENAME_CACHES = instance.parameterAsString(parameters, 'dbtabelle_caches', context)
    DB_TABLENAME_PROTECTION = instance.parameterAsString(parameters, 'dbtabelle_protection', context)
    DB_SCHEMA = instance.parameterAsString(parameters, 'dbschema', context)

    try:
        dump_tar = tarfile.open(DB_DUMP_PATH)
        index_file = dump_tar.extractfile("index.json")
        index_data = json.load(index_file)["data_files"]
        #print(index_data)
        index_file.close()
        invalid_count = 0
        file_names = list(index_data)
        total = 100.0 / len(file_names) if len(file_names) else 0
        current = 0;
        feedback.setProgress(0)
        starttime = datetime.now()
        feedback.setProgressText("Startzeit (DB-Parser): "+str(starttime.strftime('%H:%M:%S Uhr')))

        for filename in file_names :
            if feedback.isCanceled():
                break
            file = dump_tar.extractfile(filename)
            oc_data = json.load(file)
            for i in range(len(oc_data)):
                if feedback.isCanceled():
                    break
                try:
                    if oc_data[i]['object_type'].lower() != "geocache" or oc_data[i]['data']['status'].lower() != "available" or oc_data[i]['data']['type'].lower() == "event" :
                        continue
                    location = oc_data[i]['data']['location']  # location of format 52.532933|13.281033
                    location = re.split("\\|", location)
                    latitude = location[0]
                    longitude = location[1]
                    no_protection_areas = len(oc_data[i]['data']['protection_areas'])

                    entry_id = str(uuid.uuid4())
                    cache = {"id": entry_id,
                             "code": oc_data[i]['data']['code'],
                             "name": oc_data[i]['data']['names']['de'].replace("'","''"),
                             "location": "SRID=4326;POINT("+longitude + " "+latitude+")", # postgis expects long / lat instead of lat / long
                             "type": oc_data[i]['data']['type'],
                             "founds": str(oc_data[i]['data']['founds']),
                             "no_protection_areas": str(no_protection_areas),
                             "difficulty": str(oc_data[i]['data']['difficulty']).replace("None","NULL"),
                             "terrain": str(oc_data[i]['data']['terrain']).replace("None","NULL"),
                             "recommendations": str(oc_data[i]['data']['recommendations']),
                             "url": oc_data[i]['data']['url'].replace("'", "''"),
                             "country": oc_data[i]['data']['country'].replace("'","''"),
                             "country2": oc_data[i]['data']['country'].replace("'","''"),
                             "state": oc_data[i]['data']['state'].replace("'","''")}

                    postgis_insert(DB_VERBINDUNGSNAME, DB_SCHEMA+"."+DB_TABLENAME_CACHES, cache, context, feedback)
                    if no_protection_areas > 0:
                        for area_data in oc_data[i]['data']['protection_areas']:
                            area_data["cache_id"] = str(entry_id);
                            area_data["name"] = area_data["name"].replace("'", "''") ;
                            area_data["type"] = area_data["type"].replace("'", "''");
                            postgis_insert(DB_VERBINDUNGSNAME, DB_SCHEMA+"."+DB_TABLENAME_PROTECTION, area_data, context, feedback)
                except Exception as error:
                    feedback.setProgressText("Ein Fehler ist beim Einlesen des folgenden JSON-Objektes aufgetreten. Wird übersprungen")
                    feedback.setProgressText("Fehlermeldung: \n\t"+str(error))
                    feedback.setProgressText(oc_data[i]+"\n")
                    invalid_count += 1
                finally:
                    feedback.setProgress(int(current * total))
            file.close()
    except Exception as error:
        feedback.setProgressText("Ein Fehler ist aufgetreten: n\t" + str(error))

    if invalid_count > 0:
         feedback.setProgressText("WARNING: "+invalid_count+" json Objekte konnten nicht eingelesen werden!")

    endtime = datetime.now()
    feedback.setProgressText("Parsing beendet: "+str(endtime.strftime('%H:%M:%S Uhr'))+" (Dauer: "+str(endtime-starttime)+")")
    return {'status': 0}