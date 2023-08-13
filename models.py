from sqlalchemy.orm import DeclarativeBase,relationship,Mapped,mapped_column
from sqlalchemy import ForeignKey,Text
from typing import List
import logging

# Configure le niveau de journalisation global
logging.basicConfig(level=logging.INFO)

# Configure le niveau de journalisation spécifiquement pour le moteur SQLAlchemy
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

class Base(DeclarativeBase):
    pass

class Admin(Base):
    __tablename__= 'admin'
    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(nullable=False)
    password:Mapped[str]=mapped_column(nullable=False)
    livreurs = relationship("Livreur", back_populates="admin")
    livraisons = relationship("Livraison", back_populates="admin")

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Livreur(Base):
    __tablename__ = 'livreur'
    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(nullable=False)
    password:Mapped[str]=mapped_column(nullable=False)
    numtel:Mapped[str]=mapped_column(nullable=False)
    numCNIB:Mapped[str]=mapped_column(nullable=False)
    disponibilite:Mapped[str]=mapped_column(nullable=False)
    admin_id = mapped_column(ForeignKey('admin.id'))
    admin = relationship("Admin", back_populates="livreurs")
    livraisons = relationship("Livraison", back_populates="livreur")

    def __init__(self, username, password, numtel, numCNIB, disponibilite, admin):
        self.username = username
        self.password = password
        self.numtel = numtel
        self.numCNIB = numCNIB
        self.disponibilite = disponibilite
        self.admin = admin

class Client(Base):
    __tablename__= 'client'
    id:Mapped[int]=mapped_column(primary_key=True)
    username:Mapped[str]=mapped_column(nullable=False)
    password:Mapped[str]=mapped_column(nullable=False)
    numtel:Mapped[str]=mapped_column(nullable=False)
    adr:Mapped[str]=mapped_column(nullable=False)
    livraisons = relationship("Livraison", back_populates="client")

    def __init__(self, username, password, numtel, adr):
        self.username = username
        self.password = password
        self.numtel = numtel
        self.adr = adr

class Livraison(Base):
    __tablename__= 'livraison'
    id:Mapped[int]=mapped_column(primary_key=True)
    etatLivraison:Mapped[str]=mapped_column(nullable=False)
    admin_id = mapped_column(ForeignKey('admin.id'))
    admin = relationship("Admin", back_populates="livraisons")
    livreur_id = mapped_column(ForeignKey('livreur.id'))
    livreur = relationship("Livreur", back_populates="livraisons")
    client_id = mapped_column(ForeignKey('client.id'))
    client = relationship("Client", back_populates="livraisons")

    def __init__(self, etatLivraison, admin, livreur, client):
        self.etatLivraison = etatLivraison
        self.admin = admin
        self.livreur = livreur
        self.client = client