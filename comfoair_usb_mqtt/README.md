# ComfoAir 350 USB MQTT

Home-Assistant-Add-on für die Zehnder ComfoAir 350 (auch StorkAir WHR 930/CA350) über einen USB-RS232-Adapter.
Werte und Stufenwahl laufen über MQTT, die Entitäten legt Home Assistant per Autodiscovery an
(`climate`, Temperaturen, Lüfter, Bypass, Filter …).

Basis: [adorobis/hacomfoairmqtt](https://github.com/adorobis/hacomfoairmqtt), Commit `dc44e4f` (MIT, siehe [LICENSE](LICENSE)).

## Lokale Änderungen gegenüber dem Original

- **1.0.0/1.0.1:** Add-on-Verpackung; MQTT-Zugangsdaten kommen vom Supervisor-Dienst (`mqtt:need`),
  ConfigParser ohne Interpolation (Passwörter mit `%`).
- **1.0.2:** Serieller Zugriff mit Lock – MQTT-Befehle und die Abfrageschleife liefen vorher gleichzeitig über
  die Schnittstelle und stahlen sich gegenseitig die Antworten (Stufe erschien erst nach ~1 min).
  Stufenbefehle laufen über eine Warteschlange in der Hauptschleife (mehrere schnell hintereinander →
  nur der letzte), die Stufe wird zusätzlich alle 10 s und 5 s nach einem Befehl abgefragt.
- **1.0.3:** Filter-Reset für RS232 korrigiert: Der Upstream-Befehl `0x0037` gilt nur für RS485 und setzte die
  Filterstunden nicht zurück. Jetzt wird `0x00DB` mit den Daten `00 00 00 01` gesendet (an der ComfoAir 350 getestet).
  Rückmeldung nach einem Stufenwechsel jetzt nach ca. 7–8 s.

## Optionen

| Option | Bedeutung |
|---|---|
| `serial_port` | Pfad des USB-Adapters, am besten `/dev/serial/by-id/...` |
| `enable_pc_mode` | PC-Modus der Anlage aktivieren |
| `refresh_interval` | Pause zwischen zwei vollständigen Abfragen in Sekunden (10–300) |

Weitere Hinweise zur Einrichtung: [DOCS.md](DOCS.md).
