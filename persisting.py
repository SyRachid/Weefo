from Weefo.models import Admin, Livreur, Client,Livraison
from Weefo.database_utils import session

admin1= Admin(
    username='Monsieur',
    password='Monsieur10'
)

admin2= Admin(
    username='Madame',
    password='Madame10'
)

livreur1 = Livreur(

    username ='Rachid SANOGO',
    password='Chidra10',
    numtel='70-26-86-34',
    numCNIB='B985624',
    disponibilite='non',
    admin=admin1
)


livreur2 = Livreur(
    username ='Eulalie THIOMBIANO',
    password='eulalie10',
    numtel='70-77-68-37',
    numCNIB='B9856254',
    disponibilite='oui',
    admin=admin2

)

client1 = Client(
    username='Jamiil',
    password='Jamiil10',
    numtel='67-27-09-69',
    adr='kaarpala'
)

client2 = Client(
    username='Jamiila',
    password='Jamiila10',
    numtel='67-27-19-69',
    adr='kaarpala'
)

livraison1= Livraison(
    etatLivraison='en cours',
    admin=admin1,
    livreur=livreur1,
    client=client1
)

livraison2= Livraison(
    etatLivraison='effectuée',
    admin=admin2,
    livreur=livreur2,
    client=client2
)

session.add_all([admin1,admin2,livreur1,livreur2,client1,client2,livraison1,livraison2])
session.commit()