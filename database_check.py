import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("firebase-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://datebot-f12cb-default-rtdb.firebaseio.com/'
    # 'storageBucket': 'datebot-f12cb.appspot.com'
})
ref = db.reference('/')
users_ref = ref.child('users')

all_users=list[users_ref.get().items()]

for i in all_users:
    print(i)