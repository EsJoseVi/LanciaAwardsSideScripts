from firebase_admin import auth
import firebase_admin

cred = firebase_admin.credentials.Certificate("./cred.json")
app = firebase_admin.initialize_app(cred)

page = auth.list_users()
while page:
    for user in page.users:
        print(user.email)
    page = page.get_next_page()
