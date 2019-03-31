#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import datetime


cred = credentials.Certificate('rfid-scm-123.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://rfid-scm-123.firebaseio.com/'
})

while True:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    reader = SimpleMFRC522.SimpleMFRC522()
    # Fetch the service account key JSON file contents
    print("Now place your tag to Read")
    id, text = reader.read()
    print("Reading done")
    ref = db.reference('/importerdata')

    ref.push({


        'id': id,
        'text': text,
        'timestamp': st



    })

    time.sleep(2)

    GPIO.cleanup()
