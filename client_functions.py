from Weefo.database_utils import session, Admin, Livreur, Client, Livraison
import logging

logging.getLogger('sqlalchemy').setLevel(logging.WARNING)

def Livre_moi():
    id = input("entrez votre Id pour la livraison: ")
    id_ = int(id)
    creer_nouvelle_livraison(id_,"en cours",session)

def creer_nouvelle_livraison(client_id, etatLivraison,session):
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        livreur = session.query(Livreur).filter_by(disponibilite = "oui").first()
        if livreur:
            nouvelle_livraison = Livraison(etatLivraison=etatLivraison, admin=livreur.admin, livreur=livreur, client=client)
            livreur.disponibilite = "non"
            session.add(nouvelle_livraison)
            session.commit()
            print("Nouvelle livraison créée avec succès!")
        else:
            print("Aucun livreur disponible pour le moment.")
    else:
        print("Client non trouvé.")
 
def afficherLivraisonsClient(client_id):
    client = session.query(Client).get(client_id)
    if client:
        livraisons = client.livraisons
    for livraison in livraisons:
         print(f"ID de la livraison : {livraison.id}, Etat : {livraison.etatLivraison}, Client: {livraison.livreur.username}, Addresse: {livraison.livreur.numCNIB}")

# Ajoutez ici d'autres fonctions pour gérer les opérations des clients
