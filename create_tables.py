from Weefo.models import Base, Admin, Livreur, Client, Livraison
from Weefo.connect import engine

Base
print("CREATING TABLES >>>>")
def create_db() :
    Base.metadata.create_all(bind=engine)
create_db()