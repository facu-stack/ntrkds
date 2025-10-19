from flask import flask, g, render_template, request, redirect, url_for, session, flash, jsonify
import sqlalchemy
import os 
import _mysql_connector as mysql

app = flask("Nutrikids-proyecto", template_folder='templates')
app.secret_key = "tu_clave_secreta"

#conexion de la base de datos desde railway
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


#ruta principal 
@app.route('/')
def index():
    return render_template('index.hmtl') 


#ruta para el html de agenda 
def agenda():
    return render_template('agenda.html')