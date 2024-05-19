import firebase_admin
from firebase_admin import firestore
from rich.console import Console
from rich.table import Table

top = 6


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
    table = Table(title=letter)
    columns = ["Nominacion", "Nº Votos"]
    nominados = dict(sorted(total[letter].items(), key=lambda x: x[1], reverse=True))
    for column in columns:
        table.add_column(column)
    n = 0
    for row in nominados:
        row = [row, str(nominados[row])]
        if row[0] == '':
            row[0] = 'Voto Blanco'
        if n < top:
            table.add_row(*row, style='bright_yellow')
        else:
            table.add_row(*row, style='bright_red')
        n = n + 1
    console = Console()
    console.print(table)
