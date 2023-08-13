from database_utils import session, Admin, Livreur, Client, Livraison
import logging

logging.getLogger('sqlalchemy').setLevel(logging.CRITICAL)

def afficher_livraisons_livreur(livreur_id):
    livraisons = session.query(Livraison).filter_by(livreur_id=livreur_id).all()
    for livraison in livraisons:
        print(f"ID: {livraison.id}, État: {livraison.etatLivraison}, Client: {livraison.client.username}")

def LivreurEffect():
    id = input("entrer l'id du livreur")
    id_ = int(id)
    afficher_livraisons_livreur(id_)
# Ajoutez ici d'autres fonctions pour gérer les opérations des livreurs
