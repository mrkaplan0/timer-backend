# Django Timer Projekt - Zeitmanagement mit Kalender

Dieses Projekt ist eine einfache Zeitmanagement-Anwendung, die mit dem Django-Framework in Python entwickelt wurde und einen integrierten Kalender zur besseren Übersicht bietet. Sie ermöglicht Benutzern, verschiedene Timer zu erstellen, zu starten, zu stoppen und zu verwalten, um ihre Zeit effektiv zu tracken. Der Kalender dient dazu, abgeschlossene Timer-Sessions oder geplante Zeitblöcke visuell darzustellen.

## Funktionen
* ** Dashboard Verwaltung:** 
* **Timer erstellen:** Benutzer können neue Timer mit einer benutzerdefinierten Beschreibung erstellen.
* **Starten und Stoppen:** Jeder erstellte Timer kann einzeln gestartet und gestoppt werden.
* **Anzeige der verstrichenen Zeit:** Die verstrichene Zeit für jeden aktiven Timer wird in Echtzeit angezeigt.
* **Verwaltung von Timern:** Benutzer können eine Übersicht aller ihrer erstellten Timer einsehen.
* **Löschen von Timern:** Timer können bei Bedarf gelöscht werden.
* **Kalenderintegration:** Eine Kalenderansicht ermöglicht die Visualisierung von abgeschlossenen Timer-Sessions oder geplanten Zeitblöcken.
* **Zeitliche Zuordnung:** Timer-Aktivitäten können bestimmten Zeitpunkten oder Zeiträumen im Kalender zugeordnet werden.

## Voraussetzungen

Bevor Sie dieses Projekt ausführen können, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

* **Python:** Version 3.x ist erforderlich. Sie können Python von der offiziellen Website herunterladen: [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **pip:** Der Python-Paketinstaller sollte standardmäßig mit Ihrer Python-Installation enthalten sein. Überprüfen Sie, ob er installiert ist, indem Sie in Ihrem Terminal oder Ihrer Eingabeaufforderung `pip --version` ausführen.
* **Django:** Dieses Projekt basiert auf dem Django-Framework. Sie müssen Django installieren, falls Sie es noch nicht haben. Verwenden Sie dazu pip:
    ```bash
    pip install Django
    ```

## Installation

1.  **Repository klonen (optional):** Wenn der Code in einem Git-Repository gespeichert ist (z.B. auf GitHub, GitLab oder Bitbucket), klonen Sie das Repository auf Ihren lokalen Rechner:
    ```bash
    git clone <REPOSITORY_URL>
    cd timer-backend  # Oder der Name Ihres Repository-Ordners
    ```

2.  **Virtual Environment erstellen (empfohlen):** Es ist eine gute Praxis, ein virtuelles Environment für Ihr Django-Projekt zu erstellen, um Abhängigkeiten isoliert zu halten.
    * Unter Linux/macOS:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * Unter Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Abhängigkeiten installieren:** Installieren Sie alle erforderlichen Python-Pakete, die im `requirements.txt`-Datei aufgeführt sind. (Stellen Sie sicher, dass sich die Datei im Hauptverzeichnis des Projekts befindet).
    ```bash
    pip install -r requirements.txt
    ```
    Sollte die Datei `requirements.txt` noch nicht existieren (z.B. bei einem neuen Projekt), können Sie diesen Schritt vorerst überspringen und später, nachdem Sie Django und eventuelle andere Pakete installiert haben, mit `pip freeze > requirements.txt` erstellen.

## Datenbank konfigurieren

Django unterstützt verschiedene Datenbanken (z.B. SQLite, PostgreSQL, MySQL). Die Standardeinstellung ist SQLite, die keine zusätzliche Konfiguration erfordert und für Entwicklung und kleinere Projekte gut geeignet ist.

Für andere Datenbanken müssen Sie die entsprechenden Datenbank-Backends installieren (z.B. `psycopg2` für PostgreSQL, `mysqlclient` für MySQL) und die `DATABASES`-Einstellungen in der `settings.py`-Datei Ihres Django-Projekts konfigurieren.

1.  **Migrationen durchführen:** Führen Sie die Django-Migrationen aus, um die Datenbanktabellen für Ihre Modelle zu erstellen:
    ```bash
    python manage.py migrate
    ```

## Entwicklungsserver starten

Um die Anwendung lokal zu starten, verwenden Sie den integrierten Django-Entwicklungsserver:

```bash
python manage.py runserver
