import firebase_admin
from firebase_admin import auth
from email.message import EmailMessage
import win32com.client
import hashlib

outlook = win32com.client.Dispatch('Outlook.Application')

mailitem = 0x0
newmail = outlook.CreateItem(mailitem)
cred = firebase_admin.credentials.Certificate("./cred.json")
app = firebase_admin.initialize_app(cred)

def sendEmail(email_reciver):
    newmail.To = email_reciver
    newmail.subject = "Link para participar en las votaciaciones de los Lancia Awards"

    auth.create_user(email=email_reciver, password=str(hashlib.md5(email_reciver.encode())))

    link = auth.generate_password_reset_link(email=email_reciver)

    newmail.Body = """\
    Utiliza el enlaze de abajo para poder ingresar en la plataforma de votacion
    de la gala de premios Lancia Awords, Un saludo la Academia.
    """

    newmail.HTMLBody = f"""\
    <html>
        <head></head>
        <body style="font-family:Arial">
            <p>
                Utiliza el link de abajo para poder ingresar en la plataforma de votacion de la gala de premios Lancia Awords.
            </p>
            <p style="color:red">
                RECUERDA VOTAR SIENDO OBJETIVO!!!
            <p>
            <p style="color:red">
                CREA UNA CONTRASEÑA DIFERENTE A LA DE EDUCACYL!!!
            <p>
            <a href={link}>Link</a> 
        </body>
    </html>   
    """
    gmail = outlook.Session.Accounts['lanciaawards@gmail.com']

    newmail._oleobj_.Invoke(*(64209, 0, 8, 0, gmail))

    newmail.Send()
sendEmail('jose.vicalv@educa.jcyl.es')