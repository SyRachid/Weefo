from models import Admin, Livreur, Client, Livraison
from admin_functions import afficher_livreurs, afficher_Clients,afficher_livraisons
from livreur_functions import LivreurEffect,afficher_livraisons_livreur
from client_functions import creer_nouvelle_livraison,Livre_moi,afficherLivraisonsClient
from database_utils import session
import logging

# Configure le niveau de journalisation global
logging.basicConfig(level=logging.INFO)

# Configure le niveau de journalisation spécifiquement pour le moteur SQLAlchemy
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)


def authentification(username, password):
    # Vérifier l'authentification pour admin
    admin = session.query(Admin).filter_by(username=username, password=password).first()
    if admin:
        return "admin"
    
    # Vérifier l'authentification pour livreur
    livreur = session.query(Livreur).filter_by(username=username, password=password).first()
    if livreur:
        return "livreur"
    
    # Vérifier l'authentification pour client
    client = session.query(Client).filter_by(username=username, password=password).first()
    if client:
        return "client"
    
    return None


def creer_livraison(etatLivraison, admin, livreur, client):
    livraison = Livraison(etatLivraison=etatLivraison, admin=admin, livreur=livreur, client=client)
    session.add(livraison)
    session.commit()
    return livraison

def main():
    print("Bienvenue dans votre application de gestion de livraisons!")

    while True:
        print("\n1. Se connecter")
        print("2. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            user_type = authentification(username, password)
            
            if user_type == "admin":
                while True:
                 print("entrez pour afficher: ")
                 option = input("1-livreurs\n2-clients\n3-livraisons\n0-pour quitter: \n")
                 if option == "1":
                    afficher_livreurs()
                    print("\n")
                 elif option == "2":
                    afficher_Clients()
                    print("\n")
                 elif option == "3":
                    afficher_livraisons()
                    print("\n")
                 elif option == "0" :
                     print("Au revoir chere admin!!!")
                     break
                 else:
                    print("option incorrect")
                 
                # Appel de fonctions pour gérer les opérations administratives
            elif user_type == "livreur":
                # Appel de fonctions pour gérer les opérations des livreurs
                LivreurEffect()
            elif user_type == "client":
                while True:
                    print("Tapez: ")
                    option = input("1-pour se faire livrer a votre addresse\n2-pour afficher la liste des livraisons\n0-pour quitter")
                    if option == "1":
                        Livre_moi()
                    elif option == "2":
                        use = input("Entrez votre Id pour plus de sécurité: ")
                        use_=use
                        afficherLivraisonsClient(use_)
                        #affichage liste des livraisons
                    elif option == "0":
                        print("Au revoir")
                        break
            else:
                print("Authentification échouée")

        elif choix == "2":
            print("Merci d'avoir utilisé l'application!")
            break

        else:
            print("Option invalide")

if __name__ == "__main__":
    main()
