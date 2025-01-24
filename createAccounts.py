import firebase_admin
from firebase_admin import auth
from email.message import EmailMessage
import win32com.client
import hashlib
import time

outlook = win32com.client.Dispatch('Outlook.Application')

mailitem = 0x0
cred = firebase_admin.credentials.Certificate("./cred.json")
app = firebase_admin.initialize_app(cred)

def sendEmail(email_reciver):
    newmail = outlook.CreateItem(mailitem)
    newmail.To = email_reciver
    newmail.subject = "Link para participar en las SEGUNDAS votaciaciones de los Lancia Awards"

    #auth.create_user(email=email_reciver, password=hashlib.md5(email_reciver.encode('utf-8')).hexdigest())

    newmail.Body = """\
    Utiliza la contraseña de abajo para ingresar en la plataforma de votacion
    de la gala de premios Lancia Awords, Un saludo la Academia.
    """

    newmail.HTMLBody = f"""\
    <html>
        <head></head>
        <body style="font-family:Arial">
            <p>
                Gracias a vuestros votos hemos reducido las opciones de cada categoria a 4 nominaciones,
                esta sera la votación que dictaminara el ganador de cada categoria.
                Utiliza la contrasña de abajo para ingresar en la plataforma de votacion de la gala de premios Eso Awords.
            </p>
            <p style="color:red">
                RECUERDA VOTAR SIENDO OBJETIVO!!!
            <p>
            <p style="color:red">
                COPIA LA CONTRASEÑA
            <p>
            <p>
                {hashlib.md5(email_reciver.encode('utf-8')).hexdigest()}
            </p>
        </body>
    </html>   
    """
    print(hashlib.md5(email_reciver.encode('utf-8')).hexdigest())
    gmail = outlook.Session.Accounts['lanciaawards@gmail.com']

    newmail._oleobj_.Invoke(*(64209, 0, 8, 0, gmail))

    newmail.Send()

f = open('emails.txt', 'r', encoding='UTF-8')

for line in f:
    print(line[:-1])
    time.sleep(1)
    sendEmail(line[:-1])
    time.sleep(1)
