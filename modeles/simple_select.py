from main import session
from models import Admin, Livreur, Client, Livraison
from sqlalchemy import select

livreurs = session.query(Livreur).all()

for livreur in livreurs:
    print(livreur)