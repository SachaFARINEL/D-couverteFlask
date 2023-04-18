import os

from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from flask import send_from_directory

from model import Facture, db

app = Flask(__name__)
engine = create_engine('sqlite:///comptatruck.db')
db.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def accueil():  # put application's code here
    return render_template('accueil.html')


@app.route('/comptabilite')
def comptabilite():
    return render_template('comptabilite.html', factures=session.query(Facture).all())


@app.route('/addFacture')
def addFacture():
    return render_template('addFacture.html')


@app.route('/getFields', methods=["POST"])
def getFields():
    libelle = request.form["libelle"]
    nom_fournisseur = request.form["nom_fournisseur"]
    montant_facture_ht = float(request.form["montant_facture_ht"])
    date_acquittement = request.form["date_acquittement"]
    facture_pdf = request.files['facture_pdf']
    filename = secure_filename(facture_pdf.filename)
    facture_pdf.save(os.path.join(app.root_path, 'uploads', filename))

    print('FACTURE', facture_pdf)
    facture = Facture(libelle=libelle,
                      nom_fournisseur=nom_fournisseur,
                      montant_facture_ht=montant_facture_ht,
                      date_acquittement=date_acquittement,
                      facture_pdf=filename)

    session.add(facture)
    session.commit()
    return redirect('/comptabilite')


@app.route('/download/<filename>')
def download_facture(filename):
    directory = app.config['UPLOAD_FOLDER']
    return send_from_directory(directory, filename)


@app.route('/delete_all')
def delete_all():
    session.query(Facture).delete()
    session.commit()
    return redirect('/comptabilite')


if __name__ == '__main__':
    app.run()
