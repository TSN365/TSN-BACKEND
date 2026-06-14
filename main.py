import firebase_admin
from firebase_admin import credentials, db
import json
import os

firebase_json = os.environ.get('FIREBASE_CONFIG')
database_url = os.environ.get('DATABASE_URL')

if not firebase_admin._apps:
    cred_dict = json.loads(firebase_json)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred, {
        'databaseURL': database_url
    })

def fetch_and_save():
    ref = db.reference('/')
    data = ref.get()
    # ফাইলের নাম ATV.json দেওয়া হয়েছে
    with open('tsn.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Success: tsn.json created")

if __name__ == "__main__":
    fetch_and_save()
