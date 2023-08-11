from main import session
from models import Admin, Livreur, Client, Livraison

def delete_livreur(livreur_id):
    livreur = session.query(Livreur).get(livreur_id)
    if livreur:
        session.delete(livreur)
        session.commit()
        print(f"Livreur avec ID {livreur_id} supprimé.")
    else:
        print(f"Livreur avec ID {livreur_id} non trouvé.")

def delete_client(client_id):
    client = session.query(Client).get(client_id)
    if client:
        session.delete(client)
        session.commit()
        print(f"Client avec ID {client_id} supprimé.")
    else:
        print(f"Client avec ID {client_id} non trouvé.")

def delete_admin(admin_id):
    admin = session.query(Admin).get(admin_id)
    if admin:
        session.delete(admin)
        session.commit()
        print(f"Admin avec ID {admin_id} supprimé.")
    else:
        print(f"Admin avec ID {admin_id} non trouvé.")

def delete_livraison(livraison_id):
    livraison = session.query(Livraison).get(livraison_id)
    if livraison:
        session.delete(livraison)
        session.commit()
        print(f"Livraison avec ID {livraison_id} supprimée.")
    else:
        print(f"Livraison avec ID {livraison_id} non trouvée.")


