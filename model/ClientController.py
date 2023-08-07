from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Client

#creation de la machine
engine = create_engine('SyRachid10.mysql.pythonanywhere-services.com')

#création d'une session 
Session = sessionmaker(bind=engine)
session = Session()

class ClientController:
    def create_client(self,nom_utilisateur,mdp,addresse,num_fone):
        new_client = Client(nom_utilisateur=nom_utilisateur,mdp=mdp,addresse=addresse,num_fone=num_fone)
        session.add(new_client)
        session.commit()

    def get_all_clients(self):
        return session.query(Client).all()
    
    def get_client_by_id(self, client_id):
        return session.query(Client).filter_by(id=client_id).first()

    def update_client(self, client_id, nom_utilisateur,phone_number, addresse):
        client = session.query(Client).filter_by(id =client_id).first()
        if client:
            client.nom_utilisateur = nom_utilisateur
            client.num_fone = phone_number
            client.addresse = addresse
            session.commit()

    def delete_client(self, client_id):
        client = session.query(Client).filter_by(id=client_id).first()
        if client:
            session.delete(client)
            session.commit()    