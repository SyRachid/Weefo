from sqlalchemy import create_engine, Column,Integer, String
from sqlalchemy.ext.declarative import declarative_base

username = 'SyRachid10'
password = 'eulalie10'
host = 'SyRachid10.mysql.pythonanywhere-services.com'
db_name = 'SyRachid$Weefo'

url = f'mysql://{username}:{password}@{host}/{db_name}'
#Créer une classe de base pour la déclaration de mod_le

#creation du moteur (engine) pour la base de données MySQL
engine = create_engine(url,echo=True)
Base = declarative_base()

class client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    nom_utilisateur = Column(String(50))
    mdp = Column(Integer)
    num_fone = Column(Integer)
    addresse = Column(String(50))

#creation de la base de données
Base.metadata.create_all(engine)