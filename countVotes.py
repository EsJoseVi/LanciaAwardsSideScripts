import firebase_admin
from firebase_admin import firestore

cred = firebase_admin.credentials.Certificate("./cred.json")

app = firebase_admin.initialize_app(cred)

client = firestore.client(app=app)

docs = client.collection('Test').get()

total = {'A': dict(),'B': dict(),'C': dict(),'D': dict(),'E': dict(),'F': dict(),'G': dict(),'H': dict(),'I': dict(),'J': dict(),'K': dict(),'L': dict()}

for doc in docs:
    info = doc.to_dict()
    votos =  info["Votos"]
    for i in votos:
        category = total[i]
        if votos[i] not in category.keys():
            category[votos[i]] = 0
        if votos[i] in category.keys():
            category[votos[i]] = category[votos[i]] + 1


for letter in total:
    print(f"Categoria {letter}: {total[letter]}")