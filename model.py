from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, LargeBinary

db = declarative_base()


class Facture(db):
    __tablename__ = 'T_Facture'
    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)
    nom_fournisseur = Column(String(50), nullable=False)
    montant_facture_ht = Column(Numeric(precision=10, scale=2), nullable=False)
    montant_facture_ttc = Column(Numeric(precision=10, scale=2), nullable=False)
    date_acquittement = Column(String(50), nullable=False)
    facture_pdf = Column(String(50))

    def __init__(self, libelle, nom_fournisseur, montant_facture_ht, date_acquittement, facture_pdf):
        self.libelle = libelle
        self.nom_fournisseur = nom_fournisseur
        self.montant_facture_ht = montant_facture_ht
        self.montant_facture_ttc = montant_facture_ht * 1.206
        self.date_acquittement = date_acquittement
        self.facture_pdf = facture_pdf
