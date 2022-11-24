import os

import pandas as pd
import numpy as np
from datetime import datetime,timezone, timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def do_something():
    # Use the application default credentials
    # cred = credentials.Certificate("/content/drive/MyDrive/secret key/yeonpick-0727-firebase-adminsdk-41a1r-57f7d55c29.json")
    cred = credentials.Certificate(os.getcwd() + "/scheduler/firebase-secret.json")
    print("something")
    try:
        firebase_admin.initialize_app(cred)
        print("Yes!!")
    except:
        print("Already Connected")
    print('HERERERERE!')
