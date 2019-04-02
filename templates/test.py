



import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('../zest-2k19-37078-firebase-adminsdk-2z2uu-fda1eb5560.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
uid = 'KxhsKksVuae8dBH4vure7AjtpVS2'
user_data = db.collection(u'users').document(uid).get()
user_in = user_data.to_dict()
for user in user_in:
    print(user+ " "+ user_in[user])
print(user_in)
print(user_in['email'])
'''
doc_ref = db.collection(u'users').document(uid)
doce = doc_ref.collection(u'details').document()

doce.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912

})
'''
