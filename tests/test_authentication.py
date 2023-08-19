from Weefo.models import Admin, Livreur, Client
from Weefo.main import authentification

def test_authentification_admin(db_session):
    admin = Admin(username='admin', password='password')
    db_session.add(admin)
    db_session.commit()
    
    user_type = authentification('admin', 'password',session=db_session)
    assert user_type == 'admin'

def test_authentification_livreur(db_session):
    admin = Admin(username='admin', password='password')
    db_session.add(admin)
    db_session.commit()
    livreur = Livreur(username='livreur1', password='password', numtel='12345', numCNIB='54321', disponibilite='oui', admin=admin)
    db_session.add(livreur)
    db_session.commit()
    
    user_type = authentification('livreur1', 'password',session=db_session)
    assert user_type == 'livreur'

def test_authentification_client(db_session):
    client = Client(username='client1', password='password', numtel='67890', adr='adresse1')
    db_session.add(client)
    db_session.commit()
    
    user_type = authentification('client1', 'password',session=db_session)
    assert user_type == 'client'

def test_authentification_invalid(db_session):
    # Assurez-vous que les utilisateurs n'ont pas été ajoutés à la base de données pour ce test
    user_type = authentification('utilisateur_inexistant', 'mot_de_passe_incorrect',session=db_session)
    assert user_type is None
