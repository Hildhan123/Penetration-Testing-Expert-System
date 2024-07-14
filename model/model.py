from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CIA(Base):
    __tablename__ = 'cia'

    id = Column(Integer, primary_key=True)
    cia_name = Column(String)
    cia_indonesia = Column(String)
    definisi = Column(String)
    solusi = Column(String)
    
    alerts = relationship('Relasi', back_populates='cia')

    def __str__(self):
        return f"ID: {self.id}, Name: {self.cia_name}, Indonesia: {self.cia_indonesia}, Definisi: {self.definisi}, Solusi: {self.solusi}"

class Alert(Base):
    __tablename__ = 'alert'

    id = Column(String, primary_key=True)
    alert = Column(String)
    status = Column(String)
    risk = Column(String)
    type = Column(String)

    cias = relationship('Relasi', back_populates='alert')

    def __str__(self):
        return f"ID: {self.id}, Alert: {self.alert}, Status: {self.status}, Risk: {self.risk}, Type: {self.type}"

class Relasi(Base):
    __tablename__ = 'relasi'

    id = Column(String, primary_key=True)
    id_alert = Column(String, ForeignKey('alert.id'))
    id_cia = Column(Integer, ForeignKey('cia.id'))

    cia = relationship('CIA', back_populates='alerts')

    alert = relationship('Alert', back_populates='cias')