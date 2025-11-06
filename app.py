from flask import Flask, g, render_template, request, redirect, url_for, session, flash, jsonify
import sqlalchemy
import os 
import mysql.connector  # <- Usá este, no "_mysql_connector"

app = Flask("Nutrikids-proyecto", template_folder='templates')
app.secret_key = "tu_clave_secreta"

# Conexión de la base de datos desde Railway
app.config['DATABASE_URL'] = os.getenv('MYSQL_URL')

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("RAILWAY_PRIVATE_DOMAIN"),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=3306  # MySQL usa el puerto 3306
    )
    return conn


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

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




