from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.debug = True
Bootstrap(app)

db = SQLAlchemy(app)
#CAMBIO
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:12345@localhost:5432/escolares'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://kxzqzoiceiicjh:09244940a207ccbd7d9a32f23c1e9880a8e7a095d21192c0e7a0012ca0b9b67b@ec2-54-211-238-131.compute-1.amazonaws.com:5432/d1unl284n22aid'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

#Modelo de datos
class Alumnos(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	nombre = db.Column(db.String(30))
	apellido = db.Column(db.String(100))

	lista = ["Nosotros", "Contacto", "Preguntas frecuentes"]

@app.route('/', methods=['GET', 'POST'] )
def index():
	print("index")
	if  request.method =="POST":
		print("request")
		campo_nombre = request.form['nombre']
		campo_apellido = request.form['apellido']
		alumno = Alumnos(nombre=campo_nombre,apellido=campo_apellido)
		db.session.add(alumno)
		db.session.comit()
		mensaje = "Alumno registrado"
		return render_template("index.html", mensaje = mensaje)
		return render_template("index.html", variable = lista)

@app.route('/acerca')
def acerca():
	colsulta = Alumno.query.all()
	print(consulta)
	return render_template("acerca.html", variable = consulta)

if __name__ == "__main__":
	app.run()