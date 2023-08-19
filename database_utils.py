from sqlalchemy.orm import Session
from Weefo.connect import engine
from Weefo.models import Admin, Livreur, Client, Livraison,Base
import logging

logging.getLogger('sqlalchemy').setLevel(logging.CRITICAL)
Base
session = Session(bind=engine)
