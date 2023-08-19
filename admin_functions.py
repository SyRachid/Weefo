from Weefo.database_utils import session, Admin, Livreur, Client, Livraison
import logging

logging.getLogger('sqlalchemy').setLevel(logging.CRITICAL)

def afficher_livreurs():
    livreurs = session.query(Livreur).all()
    print("Liste des Livreurs de Weefo:")
    for livreur in livreurs:
        print(f"ID: {livreur.id}, Nom d'utilisateur: {livreur.username} ,mot de pass: {livreur.password}, Disponibilité: {livreur.disponibilite} ,CNIB: {livreur.numCNIB}")

def afficher_Clients():
    clients = session.query(Client).all()
    print("Liste des clients de Weefo: ")
    for client in clients:
        print(f"ID: {client.id}, Nom d'utilisateur: {client.username}, Addresse: {client.adr}")

def afficher_livraisons():
    livraisons = session.query(Livraison).all()
    print("Historique des Livraisons de Weefo: ")
    for livraison in livraisons:
         print(f"ID de la livraison : {livraison.id}, Etat : {livraison.etatLivraison}, Client: {livraison.client.username}, Addresse: {livraison.client.adr}")
# Autres fonctions administratives
