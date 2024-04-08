import firebase_admin
from firebase_admin import auth
from email.message import EmailMessage
import win32com.client

outlook = win32com.client.Dispatch('Outlook.Application')

mailitem = 0x0

newmail = outlook.CreateItem(mailitem)

gpassword = "eswt huii qoxm kqah"
email_reciver = "jose.vicalv@educa.jcyl.es"
newmail.To = email_reciver
newmail.subject = "Link para participar en las votaciaciones de los Lancia Awards"

cred = firebase_admin.credentials.Certificate("./cred.json")

app = firebase_admin.initialize_app(cred)

#auth.create_user(email=email_reciver, password="123456")

link = auth.generate_password_reset_link(email=email_reciver)

newmail.Body = """\
Utiliza el enlaze de abajo para poder ingresar en la plataforma de votacion
de la gala de premios Lancia Awords, Un saludo la Academia.
"""

newmail.HTMLBody = f"""\
<html>
    <head></head>
    <body>
        <p>
            Utiliza el enlaze de abajo para poder ingresar en la plataforma de votacion de la gala de premios Lancia Awords.
        </p>
        <p style="color:red">
            Crea una contraseña diferente a la tuya
        <p>
        <a href={link}>Link</a> 
    </body>
</html>   
"""
gmail = outlook.Session.Accounts['lanciaawards@gmail.com']

newmail._oleobj_.Invoke(*(64209, 0, 8, 0, gmail))

newmail.Display()