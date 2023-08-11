from models import Base, Admin, Livreur, Client, Livraison
from connect import engine


print("CREATING TABLES >>>>")
Base.metadata.create_all(bind=engine)