from  Weefo.database_utils import session, Admin, Livreur, Client, Livraison

from sqlalchemy.exc import SQLAlchemyError

def afficher_livraisons_livreur(livreur_id, session):
    livreur = session.query(Livreur).get(livreur_id)
    if livreur:
        livraisons = livreur.livraisons
        if livraisons:
            print(f"Livraisons du livreur {livreur.username}:")
            for livraison in livraisons:
                if livraison.client:
                    print(f"ID de la livraison : {livraison.id}, Etat : {livraison.etatLivraison}, Client: {livraison.client.username}, Addresse: {livraison.client.adr}")
            choice = input("tapez l'ID de la livraison a effectuée ou tapez exit pour quitter:  ")
            if choice != "exit":
                choice_ = int(choice)
                session.close()
                livraison = session.query(Livraison).get(choice_)
                if livraison.etatLivraison == "effectuée":
                    print("Livraison deja effectuée")
                    exit()
                else:
                    livraison.etatLivraison = "effectuée"
                    session.commit()
                    livraison.livreur.disponibilite = "oui"
                    session.commit()
                    print(f"Veuillez gérer la livraison a l'addresse {livraison.client.adr}")
        else:
            print(f"Aucune livraison pour le livreur {livreur.username}.")
    else:
        print("Livreur non trouvé ou aucune livraison disponible pour ce livreur.")
#fonction pour effectuée une livraison 
def LivreurEffect():
    id = input("entrer l'id du livreur: ")
    id_ = int(id)
    afficher_livraisons_livreur(id_)
# Ajoutez ici d'autres fonctions pour gérer les opérations des livreurs
