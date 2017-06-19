#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import homie
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TEMPERATURE_INTERVAL = 3

Homie = homie.Homie("homie-python.json")
temperatureNode = Homie.Node("temperature", "temperature")
temperatureNode\
    .addProperty("value")\
    .addProperty("unit")

humidityNode = Homie.Node("humidity", "humidity")
humidityNode\
    .addProperty("degree")\
    .addProperty("unit")

def main():
    Homie.setFirmware("awesome-temperature", "1.0.0")
    Homie.setup()
    Homie.setNodeProperty(temperatureNode, "unit", "°C", True)
    Homie.setNodeProperty(humidityNode, "unit", "%", True)

    while True:
        temperature = 22.0
        humidity = 60.0

        logger.info("Temperature: {:0.2f} °C".format(temperature))
        Homie.setNodeProperty(temperatureNode, "value", temperature, True)

        logger.info("Humidity: {:0.2f} %".format(humidity))
        Homie.setNodeProperty(humidityNode, "value", humidity, True)

        time.sleep(TEMPERATURE_INTERVAL)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Quitting.")
