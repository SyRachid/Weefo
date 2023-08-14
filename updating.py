from database_utils import session, Livraison, Livreur
def update_livreur(livreur_id, new_username):
    livreur = session.query(Livreur).filter_by(id=livreur_id).first()
    if livreur:
        livreur.username = new_username
        session.commit()


def update_client(client_id, new_username):
    client = session.query(Client).filter_by(id=client_id).first()
    if client:
        client.username = new_username
        session.commit()

def update_livraison(livraison_id, new_etatLivraison):
    livraison = session.query(Livraison).filter_by(id=livraison_id).first()
    if livraison:
       livraison.etatLivraison = new_etatLivraison
       session.commit()

def update_admin(admin_id, new_username):
    admin = session.query(Admin).filter_by(id=admin_id).first()
    if admin:
        admin.username = new_username
        session.commit()