from sqlalchemy import create_engine,text
import logging

# Configure le niveau de journalisation global
logging.basicConfig(level=logging.INFO)

# Configure le niveau de journalisation spécifiquement pour le moteur SQLAlchemy
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

engine=create_engine("sqlite:///weefo.db")

