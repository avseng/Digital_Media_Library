#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import paho.mqtt.client as mqtt
from jproperties import Properties
import logging


reader = SimpleMFRC522()
topic = "chromecast"


def readContentFromFile(id):
    configs = Properties()
    video_id = "INVALID"
    with open('/home/pi/rfid/list.properties', 'rb') as config_file:
         try:
             configs.load(config_file)
             video_id = configs.get(str(id)).data
         except AttributeError as a:
             logger.error("Invalid card id")
         return video_id



if __name__ == '__main__':

    logger = logging.getLogger('rfid')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("/home/pi/rfid/rfid.log")
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)


    while True:
        logger.info('Reading RFID')
        try:
            id, text = reader.read()
            logger.info("Card Number: "+str(id))
            video_id = readContentFromFile(id)
            if video_id != "INVALID":
                logger.info("Card matched : video_id = "+video_id)
                client = mqtt.Client()
                client.connect("192.168.0.14", 1883, 60)
                client.publish(topic, video_id)
                time.sleep(2)

        finally:
            GPIO.cleanup()
