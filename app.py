from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
Bootstrap(app)

#Configuración para la configuración con Postgrest
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:14122016@localhost:5432/Escolares'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://wexxhpbfyjixyg:f7464c6f3f5f33d391ad7cfca89c5a8d6bb2a185517c844d87f3c9c692209683@ec2-3-95-124-37.compute-1.amazonaws.com:5432/dd84g65v1srb21'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Alumnos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(100))

lista = ["Nosotros", "Contacto", "Preguntas frecuentes"]

@app.route('/', methods=['GET','POST']) #decorador
def index():
    print("index")
    if request.method == 'POST':
        print("request")
        campo_nombre = request.form['nombre']
        campo_apellido = request.form['apellido']
        alumno = Alumnos(nombre=campo_nombre,apellido=campo_apellido)
        db.session.add(alumno)
        db.session.commit()
        mensaje = "Alumno registrado"
        return render_template("index.html", mensaje = mensaje)
    return render_template("index.html", variable = lista)
    #return redirect(url_for('acerca'))

@app.route('/acerca') #decorador
def acerca():
    consulta = Alumnos.query.all()
    print(consulta)
    return render_template("acerca.html", variable = consulta)

@app.route('/editar/<id>') #decorador
def editar(id):
    r= Alumnos.query.filter_by(id=int(id)).first()
    return render_template("editar.html", alumno = r)

@app.route('/actualizar', methods=['GET','POST'])
def actualizar():
    if request.method == 'POST':
        qry = Alumnos.query.get(request.form['id'])
        qry.nombre = request.form['nombreE']
        qry.apellido = request.form['apellidoE']
        db.session.commit()
        return redirect(url_for('acerca'))

@app.route('/eliminar/<id>')
def eliminar(id):
    q= Alumnos.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('acerca'))




if __name__ == "__main__":
    app.run(debug=True)
