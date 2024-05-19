import firebase_admin
from firebase_admin import auth
import time

cred = firebase_admin.credentials.Certificate("./cred.json")
app = firebase_admin.initialize_app(cred)

def delete(email):
    auth.delete_user(auth.get_user_by_email(email).uid)

f = open('emails.txt', 'r', encoding='UTF-8')

for line in f:
    print(line[:-1])
    time.sleep(1)
    delete(line[:-1])
    time.sleep(1)