import sys
sys.path.insert(0, 'C:/Users/HP Pavillon/Weefo') 

from Weefo.models import Client, Livreur, Livraison,Admin
from Weefo.client_functions import creer_nouvelle_livraison

def test_creer_nouvelle_livraison(db_session):
    # Créez des objets Client et Livreur pour le test
    admin = Admin(username='admin', password='password')
    livreur = Livreur(username='livreur1', password='password', numtel='12345', numCNIB='54321', disponibilite='oui', admin=admin)
    client = Client(username='client1', password='password', numtel='67890', adr='adresse1')

    # Ajoutez les objets à la session de la base de données
    db_session.add_all([admin, livreur, client])
    db_session.commit()
    
    
    
    # Appelez la fonction à tester
    creer_nouvelle_livraison(client_id=client.id, etatLivraison='en cours',session=db_session)

    # Vérifiez si la livraison a été créée
    livraisons = db_session.query(Livraison).all()
    assert len(livraisons) == 1
    assert livraisons[0].etatLivraison == 'en cours'
    assert livraisons[0].client == client
    assert livraisons[0].livreur == livreur
    assert livraisons[0].admin == admin
    