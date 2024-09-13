import mysql.connector

def conectarDb():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="imc"
        )
        # print("Conexión exitosa.")
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None
    
def guardarPacientes(conexion, ci, nombre, edad):
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO pacientes (ci, nombre, edad) VALUES (%s, %s, %s)"
        valores = (ci, nombre, edad)
        cursor.execute(query, valores)
        conexion.commit()
        print("Guardado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")
    finally:
        cursor.close()

def consultarPaciente(conexion, ci):
    try:
        cursor = conexion.cursor()
        query = "SELECT * FROM pacientes WHERE ci = %s"
        cursor.execute(query, (ci,))
        resultado = cursor.fetchone()
        if resultado:
            return ["success", resultado]
        else:
            # print("Paciente no encontrado.")
            return ["error", "Paciente no encontrado."]
    except mysql.connector.Error as err:
        print(f"Error al consultar datos: {err}")

def guardarImc(conexion, ci, peso, altura, result, descripcion):
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO registros (ci, peso, altura, result, descripcion) VALUES (%s, %s, %s,%s, %s)"
        valores = (ci, peso, altura, result, descripcion)
        cursor.execute(query, valores)
        conexion.commit()
        print("Guardado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos: {err}")

def getRegistros(conexion, ci):
    try:
        cursor = conexion.cursor()
        query = "select p.ci, p.nombre, p.edad, r.altura, r.peso, r.result, r.descripcion from registros as r inner join pacientes as p on r.ci = p.ci where r.ci = %s"
        cursor.execute(query, (ci, ))
        resultado = cursor.fetchall()
        if resultado:
            return ["success", resultado]
        else:
            return ["error", "Paciente no encontrado."]
    except mysql.connector.Error as err:
        print(f"Error al consultar datos: {err}")

def cerrarBase(conexion):
    if conexion.is_connected():
        conexion.close()
        # print("Conexión cerrada.")
