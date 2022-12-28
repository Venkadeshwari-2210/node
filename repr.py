
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@firestore.transactional
def trans_identical_key_item(transaction, burger_ref):
    snapshot = burger_ref.get(transaction=transaction)
    if snapshot.exists:
        transaction.update(burger_ref,{u'fee':{u'price': 200},})

transaction = db.transaction()
burger_ref = db.collection(u'breakfast').document(u'hamburger')
trans_identical_key_item(transaction, burger_ref)
