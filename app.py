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


# Ruta principal 
@app.route('/')
def index():
    return render_template('index.html')

# ruta para registrarse

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/')
def PaginaPrincipal():
    return render_template('PaginaPrincipal.html')

# Ruta para el html de agenda 
@app.route('/agenda')
def agenda():
    return render_template('agenda.html')




# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
