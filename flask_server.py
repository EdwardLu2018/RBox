from __future__ import print_function
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import sys, random, string, os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SECRET_KEY'] = "hack112_RBox"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Patient(db.Model):
    id = db.Column('patient_id', db.Integer, primary_key = True)
    name = db.Column(db.String(50)) #unique=True
    dosageA = db.Column(db.Integer)
    dosageB = db.Column(db.Integer) 
    dosageC = db.Column(db.Integer)
    code = db.Column(db.String(8))

    def __init__(self, name, dosageA, dosageB, dosageC, code):
        self.name = name
        self.dosageA = dosageA
        self.dosageB = dosageB
        self.dosageC = dosageC
        self.code = code
    
    def __repr__(self):
        return self.name

class Doctor(db.Model):
    id = db.Column('doctor_id', db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(10)) # unique=True

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return self.password

@app.route('/')
def home():
    admin = Doctor(name="elu2", password="qwerty")
    db.session.add(admin)
    db.session.commit()
    return render_template('home.html')

@app.route('/doctorLogin', methods = ['GET', 'POST'])
def doctorLogin():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            newDoctor = Doctor(name=request.form['name'], password=request.form['password'])
            for doctor in Doctor.query.all():
                if doctor.name == newDoctor.name and doctor.password == newDoctor.password:
                    db.session.add(newDoctor)
                    db.session.commit()
                    print(Doctor.query.all(), file=sys.stderr)
                    return redirect(url_for('doctorView'))
            flash('Login Unsuccessful', 'error')
            return redirect(url_for('doctorLogin'))
    return render_template('doctorLogin.html')

@app.route('/doctorView', methods = ['GET', 'POST'])
def doctorView():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['dosageA'] or \
           not request.form['dosageB'] or not request.form['dosageC']:
            flash('Please enter all the fields', 'error')
        else:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            patient = Patient(name=request.form['name'], dosageA=request.form['dosageA'], 
                              dosageB=request.form['dosageB'], dosageC=request.form['dosageC'],
                              code=code)
            db.session.add(patient)
            db.session.commit()
            print(Patient.query.all(), file=sys.stderr)
            flash('Patient was successfully added!', 'success')
            return redirect(url_for('doctorView'))
    return render_template('doctorView.html', patients=Patient.query.all())

@app.route('/customerLogin', methods = ['GET', 'POST'])
def customerLogin():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['code']:
                flash('Please enter all the fields', 'error')
        else:
            for patient in Patient.query.all():
                if request.form['name'] == patient.name and request.form['code'] == patient.code:
                    db.session.delete(patient)
                    db.session.commit()
                    return render_template('customerView.html')
            flash('Login Unsuccessful', 'error')
    return render_template('customerLogin.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
