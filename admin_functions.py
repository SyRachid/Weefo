from database_utils import session, Admin, Livreur, Client, Livraison
import logging

logging.getLogger('sqlalchemy').setLevel(logging.CRITICAL)

def afficher_livreurs():
    livreurs = session.query(Livreur).all()
    for livreur in livreurs:
        print(f"ID: {livreur.id}, Nom d'utilisateur: {livreur.username}, Disponibilité: {livreur.disponibilite}")

# Autres fonctions administratives
