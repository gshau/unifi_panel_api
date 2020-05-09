# Unifi LED simple API

This is a simple API to interact with Unifi LED panels using a GET request.  Options to turn on/off and control the brightness of the panel are available.  Brightness can be controlled down to 1% (below the 10% limit allowed by the mobile app).

### Setup

Docker is used to serve the app.  In `src/app.py` change `PANEL_ADDRESS` to the ip address of your LED panel.  To start the app:

```
docker-compose up
```

### Usage

To control on/off:
```
curl http://app-ip-address:5000/led/on
curl http://app-ip-address:5000/led/off
```

To set brightness (e.g. 30%):
```
curl http://app-ip-address:5000/led/level/30
```

