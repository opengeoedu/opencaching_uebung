# Processing-Werkzeuge, Workflows und SQL-Anweisungen zur Übung 'OpenCaching'

Dieses Repositorium enthält Resourcen und Werkzeuge, die für die Umsetzung die zur Auswertung von GeoCaching-Daten der Plattform https://www.opencaching.de/ im Zusammenhang mit europäischen Statistiken (siehe https://ec.europa.eu/eurostat) und Landnutzungsdaten (siehe https://land.copernicus.eu/pan-european/corine-land-cover/).

Die Auswertung ist Teil einer Übung des offenen Onlinekurses OpenGeoEdu im Rahmen des gleichnamigen Projektes (https://www.opengeoedu.de). 

Ausführliche Anleitungen dazu werden bald im Kursteil Open Data veröffentlicht:
* Vorlesungsteil Open Data: https://learn.opengeoedu.de/opendata
* Übungsteil Open Data: https://ilias.opengeoedu.de/ilias/goto_opengeoedu_crs_249.html


der Übung 'OpenCaching' des Kursteils Open Data

## Software

Die hier enthaltenen Resourcen wurden mit den folgenden Anwendungen entwickelt:

* QGIS 3.8
* PostgreSQL 11.5 mit der Erweiterung Postgis 2.5.3

## Ordnerstruktur

- **models:** Enhält Modelle und Workflows im Format des QGIS 'Graphical Modeler'
- **scripts:** Enthält Python 3-basierte Skript-Dateien, die mit der Processing-Toolbox (Werkzeugkasten) und als Teil von QGIS-3 Workflows ausgeführt werden können.
- **sql:** Enthält SQL-Skripte zur Datenmodellierung und Auwertung mit PostgreSQL und Postgis
- **documentation:** selbsterklärend

## Verwendung der Processing-Werkzeuge mit QGIS 3

Die einfachste Möglichkeit, die Processing-Scripte und Modelle in QGIS 3 einzubinden, ist es ist es, die Dateien der Ordner **"models"** und **"scripts"** in die gleichnamigen Verzeichnisse Ihres QGIS-Benutzerprofils zu verschieben und **QGIS dannach zu (neu-)zustarten**. Sie können diese Pfade unter `Einstellungen > Optionen > Reiter "Verarbeitung > "Modelle" bzw. "Scripte"` einsehen und Anpassen

Für den Standardnutzer "dafault" benutzt QGIS standardmäßig die folgenden Standardpfade:

**Windows-Pfad:**
[Ergänzen]

**Linux-Pfad:**
~/.local/share/QGIS/QGIS3/profiles/default/processing/models
~/.local/share/QGIS/QGIS3/profiles/default/processing/scripts

Alternativ können Sie die Dateien auch einzeln aus der Werkzeugkiste heraus über die Optionen (Rechtsklick auf entsprechendes Symbol) `Modell / Skript zum Werkzeugkasten hinzufügen...` auswählen.

Weitere Informationen:
https://docs.qgis.org/testing/en/docs/user_manual/processing/modeler.html#saving-and-loading-models
