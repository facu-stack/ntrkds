import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
import mysql.connector

app = Flask("Nutrikids-proyecto", template_folder='templates')
app.secret_key = "tu_clave_secreta"

# Datos de prueba para usuarios


# Configuración de base de datos...
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ntrkds.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Tus modelos aquí...
class Acceso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(45), nullable=False, unique=True)
    contraseña = db.Column(db.String(45), nullable=False)

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domicilio = db.Column(db.String(45), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    fecha_nacimiento = db.Column(db.Date)
    dni = db.Column(db.Integer, unique=True, nullable=False)
    localidad = db.Column(db.Integer)
    FichaMedica = db.Column(db.String(45))
    Tutor = db.Column(db.Integer)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="ntrkids",
        port=3306  
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

        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)

        # Buscar usuario REAL en MySQL
        cursor.execute("""
            SELECT ID_Acceso, Usuario, Contraseña, tipoUsuario 
            FROM acceso 
            WHERE Usuario = %s
        """, (usuario,))
        
        user = cursor.fetchone()

        cursor.close()
        conexion.close()

        # Validar credenciales
        if user and user['Contraseña'] == contraseña:
            session['logged_in'] = True
            session['usuario'] = usuario
            session['tipoUsuario'] = user['tipoUsuario']
            session['id_usuario'] = user['ID_Acceso']

            flash(f"Bienvenido {user['tipoUsuario']}!", "success")
            return redirect(url_for('paginaprincipal'))
        else:
            flash("Credenciales incorrectas", "error")
            return render_template('login.html')

    return render_template('login.html')


@app.route('/paginaprincipal')
def paginaprincipal():
    # ✅ Verificar si el usuario está logueado
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    # ✅ Pasar el tipoUsuario al template
    tipoUsuario = session.get('tipoUsuario', 'invitado')
    return render_template('paginaprincipal.html', tipoUsuario=tipoUsuario)

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
    return render_template("paginaPrincipal.html")

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

@app.route('/logout')
def logout():
    session.clear()
    flash("Sesión cerrada", "info")
    return redirect(url_for('login'))

@app.route("/profesionales")
def profesionales():
    return render_template("Profesionales.html")

@app.route("/pacientes")
def pacientes():
    return render_template("ListaPacientes.html")

# 🟢 RUTAS ACTUALIZADAS PARA EL FLUJO DE TURNOS
@app.route("/turno")
def turno():
    """Primera página - selección de día"""
    return render_template("agenda.html")

@app.route("/turnoHorario")
def turnoHorario():
    """Segunda página - selección de horario"""
    return render_template("grilla.html")

@app.route("/agenda")
def agenda():
    return render_template("agendaEspecialista.html")

@app.route("/configuracion")
def configuracion():
    return render_template("configuracion.html")

from datetime import datetime
from flask import request, render_template

@app.route("/anamnesis/<int:id>", methods=['GET', 'POST'])
def anamnesis(id):

    if request.method == "GET":
        return render_template("anamnesis.html", id=id)

    # Recibir los datos
    Leche = request.form.get('Leche', 0)
    Yogurt = request.form.get('Yogurt', 0)
    Quesos = request.form.get('Quesos', 0)
    Carnes = request.form.get('Carnes', 0)
    Huevos = request.form.get('Huevos', 0)
    Hortalizas = request.form.get('Hortalizas', 0)
    Frutas = request.form.get('Frutas', 0)
    Panificados = request.form.get('Panificados', 0)
    Pastas = request.form.get('Pastas', 0)
    Azucar = request.form.get('Azucar', 0)
    Edulcorantes = request.form.get('Edulcorantes', 0)
    Mermeladas = request.form.get('Mermeladas', 0)
    DulceDeLeche = request.form.get('DulceDeLeche', 0)
    Fritos = request.form.get('Fritos', 0)
    Manteca = request.form.get('Manteca', 0)
    Margarina = request.form.get('Margarina', 0)
    Crema = request.form.get('Crema', 0)
    Mayonesa = request.form.get('Mayonesa', 0)
    Caldos = request.form.get('Caldos', 0)
    Bebidas = request.form.get('Bebidas', 0)
    Favoritos = request.form.get('Favoritos', "")
    Aclaraciones = request.form.get('Aclaraciones', "")
    FechaActualizacion = datetime.today()

    conexion = get_db_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO anamnesialimentaria (
            Leche, Yogurt, Quesos, Carnes, Huevos, Hortalizas, Frutas,
            Panificados, Pastas, Azucar, Edulcorantes, Mermeladas,
            DulceDeLeche, Fritos, Manteca, Margarina, Crema, Mayonesa,
            Caldos, Bebidas, Favoritos, Aclaraciones, FechaActualizacion
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s)
    """, (
        Leche, Yogurt, Quesos, Carnes, Huevos, Hortalizas, Frutas,
        Panificados, Pastas, Azucar, Edulcorantes, Mermeladas,
        DulceDeLeche, Fritos, Manteca, Margarina, Crema, Mayonesa,
        Caldos, Bebidas, Favoritos, Aclaraciones, FechaActualizacion
    ))

    conexion.commit()
    cursor.close()
    conexion.close()

    return "Datos guardados correctamente"





@app.route("/api/pacientes")
def api_pacientes():
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT ID_usuario, Nombre, Apellido, DNI FROM pacientes ORDER BY Apellido")
    pacientes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(pacientes)

# app.py (api_turnos corregida)

@app.route("/api/turnos")
def api_turnos():
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    
    # Se eliminan las dos líneas extra de pacientes:
    # cursor.execute("SELECT ID_usuario AS id, Nombre, Apellido, DNI FROM pacientes ORDER BY Apellido")
    # pacientes = cursor.fetchall()

    consulta = """
        SELECT
            t.ID_Turnos as id, 
            p.Nombre, 
            p.Apellido, 
            p.DNI, 
            t.Hora AS HoraCita,           
            t.Fecha AS FechaCita, 
            t.Motivo,
            t.estadoCita AS EstadoCita,  
            t.cancelado AS Cancelado,    
            t.Paciente_ID 
        FROM 
            turnos t
        JOIN 
            pacientes p ON t.Paciente_ID = p.ID_usuario
        ORDER BY 
            t.Fecha, t.Hora
    """
    
    cursor.execute(consulta)
    turnos = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    # ... tu lógica de formateo de fechas y horas
    
    return jsonify(turnos) # Devuelve solo los turnos

# 🟢 RUTAS NUEVAS Y ACTUALIZADAS PARA LA AGENDA
@app.route('/api/dias-ocupados')
def obtener_dias_ocupados():
    try:
        especialista_id = request.args.get('especialista_id', 1, type=int)
        
        conexion = get_db_connection()
        cursor = conexion.cursor()
        
        # Consulta para obtener días que tienen al menos un turno ocupado
        query = """
        SELECT DISTINCT Fecha 
        FROM turnos 
        WHERE Especialista_ID = %s 
        AND Fecha >= CURDATE()
        AND Fecha < DATE_ADD(CURDATE(), INTERVAL 30 DAY)
        AND cancelado = FALSE
        AND estadoCita != 'cancelada'
        """
        
        cursor.execute(query, (especialista_id,))
        resultados = cursor.fetchall()
        
        # Formatear fechas como "dd/mm"
        dias_ocupados = []
        for resultado in resultados:
            fecha = resultado[0]
            if fecha:
                # Convertir date a string "dd/mm"
                dia = fecha.day
                mes = fecha.month
                dias_ocupados.append(f"{dia:02d}/{mes:02d}")
        
        cursor.close()
        conexion.close()
        
        return jsonify({
            'ocupados': dias_ocupados,
            'success': True
        })
        
    except Exception as e:
        print(f"Error en días ocupados: {e}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/horarios-ocupados')
def api_horarios_ocupados():
    try:
        fecha = request.args.get('fecha')  # YYYY-MM-DD
        especialista_id = request.args.get('especialista_id')

        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT Hora 
            FROM turnos 
            WHERE Fecha = %s AND Especialista_ID = %s AND cancelado = 0
        """, (fecha, especialista_id))

        horarios_ocupados = []
        for row in cursor.fetchall():
            hora_str = str(row['Hora'])
            if ':' in hora_str:
                horarios_ocupados.append(hora_str[:5])  # HH:MM

        cursor.close()
        conexion.close()

        return jsonify({'success': True, 'ocupados': horarios_ocupados})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# 🟢 RUTA PARA GUARDAR NUEVO TURNO
@app.route('/api/guardar-turno', methods=['POST'])
def guardar_turno():
    try:
        data = request.json
        fecha_display = data.get('fecha')  # Formato "dd/mm"
        hora = data.get('hora')
        especialista_id = data.get('especialista_id', {id})
        paciente_id = data.get('paciente_id', {id})  # Ajusta según tu lógica
        motivo = data.get('motivo', 'Consulta programada')
        
        # Validaciones
        if not fecha_display or not hora:
            return jsonify({'error': 'Fecha y hora requeridas', 'success': False}), 400
        
        # Convertir fecha de "dd/mm" a "yyyy-mm-dd"
        dia, mes = fecha_display.split('/')
        fecha_formateada = f"2025-{mes}-{dia}"  # Ajusta el año
        
        conexion = get_db_connection()
        cursor = conexion.cursor()
        
        # Verificar si el horario ya está ocupado
        verificar_query = """
        SELECT ID_Turnos FROM turnos 
        WHERE Especialista_ID = %s 
        AND Fecha = %s 
        AND Hora = %s
        AND cancelado = FALSE
        """
        cursor.execute(verificar_query, (especialista_id, fecha_formateada, hora))
        existe = cursor.fetchone()
        
        if existe:
            return jsonify({'error': 'El horario ya está ocupado', 'success': False}), 400
        
        # Insertar nuevo turno
        insert_query = """
        INSERT INTO turnos (Fecha, Hora, Motivo, estadoCita, cancelado, Paciente_ID, Especialista_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(insert_query, (
            fecha_formateada, 
            hora, 
            motivo, 
            'programada', 
            False, 
            paciente_id, 
            especialista_id
        ))
        
        conexion.commit()
        turno_id = cursor.lastrowid
        
        cursor.close()
        conexion.close()
        
        return jsonify({
            'success': True,
            'turno_id': turno_id,
            'mensaje': 'Turno reservado exitosamente'
        })
        
    except Exception as e:
        print(f"Error al guardar turno: {e}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

# -----------------------------------------------------------
# 🟢 NUEVA RUTA: RUTA PARA CANCELAR TURNO (CAMBIAR 'cancelado' a 1)
# -----------------------------------------------------------
@app.route("/api/turno/cancelar/<int:id_cita>", methods=['POST'])
def cancelar_turno(id_cita):
    # ⚠️ Nota: Esta acción asume que el campo 'cancelado' en tu DB acepta 1 para True/Cancelado
    try:
        # 1. Obtener la conexión a la base de datos MySQL
        conexion = get_db_connection()
        cursor = conexion.cursor() 
        
        # 2. Definir la consulta de actualización
        # Cambia 'cancelado' a 1 y 'estadoCita' a 'cancelada' (opcional, pero recomendado)
        update_query = """
            UPDATE turnos
            SET estadoCita = 'cancelada', cancelado = 1
            WHERE ID_Turnos = %s
        """
        
        # 3. Ejecutar la consulta con el ID del turno
        cursor.execute(update_query, (id_cita,)) 
        conexion.commit() # Guardar los cambios en la DB
        
        # 4. Cerrar recursos
        cursor.close()
        conexion.close()
        
        # 5. Devolver respuesta de éxito al frontend
        return jsonify({"success": True, "message": "Cita cancelada exitosamente."}), 200
        
    except Exception as e:
        print(f"Error al cancelar el turno {id_cita}: {e}") 
        # Devolver un error 500 si algo sale mal
        return jsonify({"success": False, "message": "Error interno del servidor al cancelar la cita."}), 500

from flask import render_template, abort, redirect, url_for, flash
# from tu_modulo_de_db import get_db_connection # Asume que tienes esto importado

from flask import render_template, abort, redirect, url_for, flash
# Asegúrate de importar get_db_connection

@app.route("/paciente/<int:id>")
def ficha_paciente(id):
    paciente = None
    fichamedica = None
    anamnesis = None
    
    try:
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)

        # 1. Datos del paciente
        cursor.execute("""
            SELECT ID_usuario AS id, Nombre, Apellido, DNI, FichaMedica
            FROM pacientes
            WHERE ID_usuario = %s
        """, (id,))
        paciente = cursor.fetchone()
        if paciente is None:
            abort(404)

        

        # 2. Ficha médica (usa el campo FichaMedica de pacientes)
        if paciente['FichaMedica'] is not None:
            cursor.execute("""
                SELECT *
                FROM fichamedica
                WHERE idFichaMedica = %s
            """, (paciente['FichaMedica'],))
            fichamedica = cursor.fetchone()

        # 3. Anamnesis alimentaria (supongamos que hay FK a paciente)
        cursor.execute("""
            SELECT *
            FROM anamnesisalimentaria
            WHERE idAnamnesisAlimentaria = %s
        """, (id,))
        anamnesis = cursor.fetchone()

        cursor.close()
        conexion.close()


        return render_template(
            "ficha_paciente.html",
            paciente=paciente,
            ficha=fichamedica,
            anamnesis=anamnesis
        )

    except Exception as e:
        return f"Error: {e}", 500

    except Exception as e:
        
        print(f"ERROR DE DB: No se pudo obtener el paciente {id}. Detalle: {e}")
        flash('Ocurrió un error al cargar los datos del paciente.', 'error')
        return redirect(url_for('paginaprincipal')) # <--- ¡CAMBIO AQUÍ!

   


@app.route("/cita/<int:id>")
def cita(id):
    paciente = None
    fichamedica = None
    anamnesis = None
    
    try:
        conexion = get_db_connection()
        cursor = conexion.cursor(dictionary=True)

        # 1. Datos del paciente
        cursor.execute("""
            SELECT ID_usuario AS id, Nombre, Apellido, DNI, FichaMedica
            FROM pacientes
            WHERE ID_usuario = %s
        """, (id,))
        paciente = cursor.fetchone()
        if paciente is None:
            abort(404)

        

        # 2. Ficha médica (usa el campo FichaMedica de pacientes)
        if paciente['FichaMedica'] is not None:
            cursor.execute("""
                SELECT *
                FROM fichamedica
                WHERE idFichaMedica = %s
            """, (paciente['FichaMedica'],))
            fichamedica = cursor.fetchone()

        # 3. Anamnesis alimentaria (supongamos que hay FK a paciente)
        cursor.execute("""
            SELECT *
            FROM anamnesisalimentaria
            WHERE idAnamnesisAlimentaria = %s
        """, (id,))
        anamnesis = cursor.fetchone()

        cursor.close()
        conexion.close()


        return render_template(
            "cita.html",
            paciente=paciente,
            ficha=fichamedica,
            anamnesis=anamnesis
        )

    except Exception as e:
        return f"Error: {e}", 500

    except Exception as e:
        
        print(f"ERROR DE DB: No se pudo obtener el paciente {id}. Detalle: {e}")
        flash('Ocurrió un error al cargar los datos del paciente.', 'error')
        return redirect(url_for('paginaprincipal')) # <--- ¡CAMBIO AQUÍ!

    
    

@app.route("/api/turno/confirmar/<int:id_cita>", methods=['POST'])
def confirmar_turno(id_cita):
    try:
        conexion = get_db_connection()
        cursor = conexion.cursor() 
        
        update_query = """
            UPDATE turnos
            SET estadoCita = 'confirmado'
            WHERE ID_Turnos = %s
        """
        
        cursor.execute(update_query, (id_cita,)) 
        conexion.commit() 
        
        cursor.close()
        conexion.close()
        
        return jsonify({"success": True, "message": "Cita confirmada exitosamente."}), 200
        
    except Exception as e:
        print(f"Error al confirmar el turno {id_cita}: {e}") 
        return jsonify({"success": False, "message": "Error interno del servidor."}), 500

@app.route("/api/profesionales")
def api_profesionales():
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            idUsuario AS id,
            Nombre,
            Especialidad,
            Telefono,
            email
        FROM especialista
    """)
    
    profesionales = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(profesionales)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)