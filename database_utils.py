from sqlalchemy.orm import Session
from connect import engine
from models import Admin, Livreur, Client, Livraison
import logging

logging.getLogger('sqlalchemy').setLevel(logging.CRITICAL)

session = Session(bind=engine)
