import sys
sys.path.insert(0, 'C:/Users/HP Pavillon/Weefo') 
import pytest
from sqlalchemy.orm import Session
from create_tables import create_db
from database_utils import engine, Base

# Fixture pour initialiser la base de données
@pytest.fixture(scope='session')
def session():
    create_db()
    Base.metadata.create_all(engine)
    yield session
    Base.metadata.drop_all(engine)

# Fixture pour obtenir une session de base de données
@pytest.fixture
def db_session(session):
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

