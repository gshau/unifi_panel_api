from flask import Flask
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

PANEL_ADDRESS = "10.0.5.85"


def get_client(panel_address=PANEL_ADDRESS):
    client = mqtt.Client("PANEL")
    client.connect(PANEL_ADDRESS, port=1883)
    return client


def turn_on(panel_address=PANEL_ADDRESS):
    client = get_client(panel_address)
    response = client.publish(
        "v2/req/set/ledlamp/output", json.dumps({"target": "output", "value": 1})
    )
    print(response)
    return "Turned On"


def turn_off(panel_address=PANEL_ADDRESS):
    client = get_client(panel_address)
    response = client.publish(
        "v2/req/set/ledlamp/output", json.dumps({"target": "output", "value": 0})
    )
    print(response)
    return "Turned Off"


@app.route("/led/<state>")
def change_state(state):
    if state == "on":
        return turn_on()
    elif state == "off":
        return turn_off()
    else:
        return 404


@app.route("/led/level/<int:level>")
def change_brightness(level):
    client = get_client(panel_address=PANEL_ADDRESS)
    if level < 0 or level > 100:
        return f"Invalid level: {level}"
    client.publish(
        "v2/req/set/ledlamp/led", json.dumps({"target": "led", "value": level})
    )
    return f"Changed brightness to {level}"


@app.route("/")
def index():
    return "Unifi LED flat panel api"

