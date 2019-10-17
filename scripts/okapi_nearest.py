from qgis.processing import alg
from qgis.core import QgsProject, QgsCoordinateTransform, QgsCoordinateReferenceSystem

import requests

@alg(name='oc_nearest', label='Geocaching-Daten abrufen', group='opengeoedu', group_label='OpenGeoEdu')
@alg.input(type=alg.POINT, name='CENTER', label='Punkt, in dessen Nähe Daten abgefragt werden sollen',
           default='12.09872,54.07524 [EPSG:4326]' ) # Vorgabe Koordinaten in Rostock
@alg.input(type=alg.DISTANCE, name='RADIUS', label='Radius', default=10) #  Vorgabe: 10 km
@alg.input(type=alg.STRING, name='CONSUMER_KEY', label='OKAPI Consumer key')
@alg.input(type=alg.VECTOR_LAYER_DEST, name='OUTPUT', label='Geocaching-Punktdaten', default="geocaches.gpx")

def oc_nearest(instance, parameters, context, feedback, inputs):
    """
    Dies ist ein einfaches Python-Script zur Abfrage von Geocaches in einem bestimmten Radius um einen Ort.
    Als Ausgabeformat MUSS GPX ausgewählt werden.
    """
    try:
        CONSUMER_KEY = instance.parameterAsString(parameters, 'CONSUMER_KEY', context)
        RADIUS = instance.parameterAsDouble(parameters, 'RADIUS', context)
        CENTER = instance.parameterAsPoint(parameters, 'CENTER', context)
        OUTPUT_PATH = instance.parameterAsFileOutput(parameters, 'OUTPUT', context)
        OUTPUT_LAYER = instance.parameterAsOutputLayer(parameters, 'OUTPUT', context)
        print(parameters)
        ## Transformiere Eingabekoordinaten in geographische Koordinaten (EPSG:4326)
        crsSrc = instance.parameterAsPointCrs(parameters, 'CENTER', context)
        feedback.setProgressText("Input CRS ID:" + str(crsSrc.srsid()))
        crsDest = QgsCoordinateReferenceSystem(4326)  # WGS 84
        xform = QgsCoordinateTransform(crsSrc, crsDest, QgsProject.instance())
        CENTER = xform.transform(CENTER)
        # Rufe Cache-codes in einem Radius um eine Standort (center) ab als JSON ab, z.B.
        # 'https://www.opencaching.de/okapi/services/caches/search/nearest?consumer_key=abcde&radius=10&center=54.07524|12.09872'
        cache_codes = requests.get("https://www.opencaching.de/okapi/services/caches/search/nearest?"
                                   + "consumer_key=" + CONSUMER_KEY
                                   + "&radius=" + str(RADIUS)
                                   + "&center=" + str(CENTER.y()) + "|" + str(CENTER.x())
                                   ).json()

        # formatiere die Ausgabe-Daten (Dictionary) der Form {'results': ['OC11ABA', 'OC00B4', 'OC695F' ... ]}
        # in eine Zeichenkette der Form "OC11ABA|OC00B4|OC695F|..."
        if 'results' not in cache_codes:
            feedback.setProgressText("Ungültige Anfrage oder keine Daten gefunden.")
            return {}
        cache_codes = ("|".join(cache_codes['results']))
        feedback.setProgressText("Cache-Codes wurden empfangen, lade Daten.")

        # Rufe GPX-Datei für Cache-Codes ab, z.B.:
        # https://www.opencaching.de/okapi/services/caches/formatters/gpx?consumer_key=abcde&cache_codes=OC11ABA|OC00B4
        req_message = "https://www.opencaching.de/okapi/services/caches/formatters/gpx?" + \
                      "consumer_key=" + CONSUMER_KEY + \
                      "&cache_codes=" + cache_codes
        response = requests.get(req_message)
        feedback.setProgressText(": " + OUTPUT_PATH)
        ofile = open(OUTPUT_PATH, 'wb')
        ofile.write(response.content)
        ofile.close()
        feedback.setProgressText("Ausgabedaten wurden geschrieben")

    except Exception as error:
        feedback.setProgressText("Ein Fehler ist aufgetreten: n\t" + str(error))

    return {'OUTPUT': OUTPUT_LAYER}
