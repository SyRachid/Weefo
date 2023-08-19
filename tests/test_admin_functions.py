from Weefo.database_utils import session, Admin, Livreur, Client, Livraison
from Weefo.admin_functions import afficher_livreurs, afficher_Clients, afficher_livraisons

def test_afficher_livreurs(db_session, capsys):
    # Créez un administrateur pour le test
    admin = Admin(username='admin', password='password')
    db_session.add(admin)
    db_session.commit()

    # Créez des livreurs pour le test
    livreur1 = Livreur(username='livreur1', password='password', numtel='12345', numCNIB='54321', disponibilite='oui', admin=admin)
    livreur2 = Livreur(username='livreur2', password='password', numtel='67890', numCNIB='98765', disponibilite='non', admin=admin)
    db_session.add_all([livreur1, livreur2])
    db_session.commit()

    # Capturez la sortie de la fonction afficher_livreurs
    with capsys.disabled():
        afficher_livreurs()

def test_afficher_Clients(db_session, capsys):
    # Créez un administrateur pour le test
    admin = Admin(username='admin', password='password')
    db_session.add(admin)
    db_session.commit()

    # Créez des clients pour le test
    client1 = Client(username='client1', password='password', numtel='12345', adr='adresse1')
    client2 = Client(username='client2', password='password', numtel='67890', adr='adresse2')
    db_session.add_all([client1, client2])
    db_session.commit()

    # Capturez la sortie de la fonction afficher_Clients
    with capsys.disabled():
        afficher_Clients()

def test_afficher_livraisons(db_session, capsys):
    # Créez un administrateur pour le test
    admin = Admin(username='admin', password='password')
    db_session.add(admin)
    db_session.commit()

    # Créez des clients et des livreurs pour le test
    client = Client(username='client1', password='password', numtel='12345', adr='adresse1')
    livreur = Livreur(username='livreur1', password='password', numtel='67890', numCNIB='54321', disponibilite='oui', admin=admin)
    db_session.add_all([client, livreur])
    db_session.commit()

    # Créez des livraisons pour le test
    livraison1 = Livraison(etatLivraison='en cours', admin=admin, livreur=livreur, client=client)
    livraison2 = Livraison(etatLivraison='effectuée', admin=admin, livreur=livreur, client=client)
    db_session.add_all([livraison1, livraison2])
    db_session.commit()

    # Capturez la sortie de la fonction afficher_livraisons
    with capsys.disabled():
        afficher_livraisons()
