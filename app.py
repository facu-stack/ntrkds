from flask import Flask, g, render_template, request, redirect, url_for, session, flash, jsonify
import sqlalchemy
import os 
import mysql.connector  

app = Flask("Nutrikids-proyecto", template_folder='templates')
app.secret_key = "tu_clave_secreta"

app.config["SLQALCHEMY_DATABASE"] = "sqlite://ntrkids.db"
app.config["SLQALCHEMY_TRACK_MODIFICATIONS"] = False

db = sqlalchemy(app)

class acceso(db.Model):
    ID = db.column(db.Integer, Primary_key=True)
    usuario = db.column(db.Varchar(45), nullable=False, unique=True)
    contraseña = db.column(db.Varchar(45), nullable=False)

class paciente(db.Model):
    id = db.column(Primary_key=True) 
    Domicilio = db.column(db.Varchar(45), nullable=False, unique=True)
    Nombre = db.Column(db.Varchar(45), nullable=False)
    Apellido = db.Column(db.Varchar(45),nullable=False)
    FechaNacimiento = db.Column(db.Date)
    DNI = db.Column(db.Integer, unique=True, nullable=False)
    Localidad = db
    





def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="ntrikids",
        port=3306  # MySQL usa el puerto 3306
    )
    return conn


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['User']
        contraseña = request.form['Contraseña']

        if usuario == "paciente@gmail.com" and contraseña == "12345":
            flash("Inicio de sesión exitoso ", "success")
            return redirect(url_for('paginaprincipal'))  # ⬅ redirige acá
        else:
            flash("Usuario o contraseña incorrectos ", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/paginaprincipal')
def paginaprincipal():
    return render_template('paginaprincipal')


@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route("/confirmacion", methods=["POST"])
def confirmacion():
    # Acá procesás los datos del formulario
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    # ... lo que necesites hacer ...
    return render_template("confirmacion.html", nombre=nombre, edad=edad)

@app.route('/home')
def home():
    return render_template("PaginaPrincipal.html")

if __name__ == '__main__':
    app.run(debug=True)


    @app.route('/registrar', methods=['POST'])
    def registrar():
    # Datos del paciente
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dni = request.form['dni']
        domicilio = request.form['domicilio']
        localidad = request.form['localidad']
        fecha_nacimiento = request.form['fecha_nacimiento']
        ficha_medica = request.form['ficha_medica']

        # Datos del tutor
        nombre_tutor = request.form['nombre_tutor']
        apellido_tutor = request.form['apellido_tutor']
        direccion_tutor = request.form['direccion_tutor']
        localidad_tutor = request.form['localidad_tutor']
        telefono_tutor = request.form['telefono_tutor']
        dni_tutor = request.form['dni_tutor']

        conexion = get_db_connection()
        cursor = conexion.cursor()

    # Insertar paciente
        cursor.execute("""
        INSERT INTO pacientes (Nombre, Apellido, DNI, Domicilio, Localidad, FechaNacimiento, FichaMedica)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nombre, apellido, dni, domicilio, localidad, fecha_nacimiento, ficha_medica))

    # Insertar tutor
        cursor.execute("""
            INSERT INTO datos_tutor (Nombre, Apellido, Direccion, Localidad, Telefono, DNI)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre_tutor, apellido_tutor, direccion_tutor, localidad_tutor, telefono_tutor, dni_tutor))

        conexion.commit()
        cursor.close()
        conexion.close()

        flash("Registro exitoso.")
        return redirect(url_for('login'))




