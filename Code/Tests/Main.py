import os
import firebase_admin
from firebase_admin import credentials, firestore
import time
import keyboard

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'

config = {
    #[API_Key]
}

cred = credentials.Certificate(config)
app = firebase_admin.initialize_app(cred)

db = firestore.client()
rasbots_ref = db.collection("rasBots")
rasbots = rasbots_ref.stream()

while True:
    if keyboard.is_pressed("q"):
        print("\nLoop aborted.")
        break

    query = rasbots_ref.where("rasBotId", "==", "1234")
    docs = query.stream()
    print("\r", end="")

    for doc in docs:
        data = doc.to_dict()
        print(f"rasBotId: {data['rasBotId']}, timeStamp: {data['timeStamp']}, x: {data['x']}, y: {data['y']}", end="")

    time.sleep(0.1)

