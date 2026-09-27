import configparser
import json
import os
from pathlib import Path
import urllib.request


def prepare(options, mqtt, template, destination):
    port = options.get("serial_port", "")
    if not port.startswith("/dev/") or not Path(port).exists():
        raise ValueError("Bitte zuerst den angeschlossenen USB-Adapter unter serial_port eintragen.")
    cfg = configparser.ConfigParser(interpolation=None)
    cfg.read(template)
    cfg["DEFAULT"].update(SerialPort=port, RS485_protocol="False",
        refresh_interval=str(options["refresh_interval"]),
        enablePcMode=str(options["enable_pc_mode"]), debug="False")
    cfg["DEVICE"]["SetUpFanLevelsAtStart"] = "False"
    cfg["MQTT"].update(MQTTServer=mqtt["host"], MQTTPort=str(mqtt["port"]),
        MQTTUser=mqtt["username"], MQTTPassword=mqtt["password"])
    cfg["HA"].update(HAAutoDiscoveryDeviceId="comfoair350_usb",
        HAAutoDiscoveryDeviceName="ComfoAir350",
        HAEnableAutoDiscoverySensors="True", HAEnableAutoDiscoveryClimate="True")
    with open(destination, "w") as output:
        cfg.write(output)
    os.chmod(destination, 0o600)


def main():
    options = json.loads(Path("/data/options.json").read_text())
    req = urllib.request.Request("http://supervisor/services/mqtt", headers={
        "Authorization": "Bearer " + os.environ["SUPERVISOR_TOKEN"]})
    with urllib.request.urlopen(req, timeout=20) as response:
        mqtt = json.load(response)["data"]
    prepare(options, mqtt, "/app/config.ini.dist", "/app/config.ini")
    os.execvp("python", ["python", "/app/ca350.py"])


if __name__ == "__main__":
    main()
