from main import session
from models import Livreur

Eulalie = session.query(Livreur).filter_by(username = 'Eulalie THIOMBIANO').first()

print(Eulalie)