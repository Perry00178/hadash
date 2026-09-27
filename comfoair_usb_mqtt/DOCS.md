# ComfoAir 350 USB MQTT

Lokales Add-on auf Basis von adorobis/hacomfoairmqtt, Commit dc44e4f86c3390301353d0444c544e229a18f85a (MIT, siehe LICENSE).
MQTT-Zugangsdaten werden aus dem Supervisor-Dienst bezogen und nicht in Logs ausgegeben.
Lokale Anpassung im Upstream-Skript: ConfigParser ohne Interpolation, damit MQTT-Passwoerter mit Prozentzeichen funktionieren.
Lokale Anpassung 1.0.2 (27.09.2026): Serieller Zugriff per Lock (MQTT-Befehle und Abfrageschleife stahlen sich gegenseitig die Antworten); Stufenbefehle laufen ueber eine Warteschlange in der Hauptschleife (schnell aufeinanderfolgende Befehle -> nur der letzte), Stufe wird zusaetzlich alle 10 s und 5 s nach einem Befehl abgefragt.

## Einrichtung
1. Add-on-Store aktualisieren und dieses lokale Add-on installieren.
2. openHAB-ComfoAir-Anbindung deaktivieren, USB-Adapter umstecken.
3. Den in HA erkannten /dev/serial/by-id/...-Pfad als serial_port eintragen.
4. enable_pc_mode erst nach Klaerung eines vorhandenen Wandbedienteils einstellen.
5. Starten, Protokoll pruefen, MQTT-Geraet ComfoAir350 kontrollieren.
6. Nach erfolgreichem Test Start beim Booten aktivieren.

Das Add-on startet nicht automatisch. Es setzt beim Start keine Luefter-Prozentwerte.
Achtung: Die Upstream-Funktion zum separaten Aktivieren/Deaktivieren von Zu-/Abluft kann dennoch die Prozentwerte aus config.ini.dist schreiben. Diese Funktion erst nach Abgleich mit den eingemessenen Anlagenwerten verwenden. Die normale Stufenauswahl ist davon getrennt.
Rueckweg: Add-on stoppen, USB zu openHAB zurueckstecken und dort die Anbindung wieder aktivieren.

Die Installation und Kommunikation mit der Anlage muessen noch auf HA getestet werden.