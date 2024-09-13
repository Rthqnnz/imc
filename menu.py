
from db import conectarDb
from db import guardarPacientes
from db import cerrarBase
from db import consultarPaciente
from db import guardarImc
from db import getRegistros

######

def crearPaciente(): 
    print("********* Ingrese los datos del paciente *******")
    ci = input("CI: ")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    
    if(nombre == "" or ci == "" or edad == ""):
        print("Debe ingresar todos los datos")
    else :
        print("Conectando...")
        conexion = conectarDb()
        if conexion:
            guardarPacientes(conexion, ci, nombre, edad)
        print("Desconectando...")
        cerrarBase(conexion)

def calcularImc():
     print("********* Calcular IMC *******")
     ci = input("Ingrese su CI: ")
     conexion = conectarDb()
     if conexion:
        paciente = consultarPaciente(conexion, ci)
        cerrarBase(conexion)
        if paciente[0] == "error":
            print("Paciente no encontrado, registrese")
            return
        paciente = paciente[1]
        
        print("------------------------------------------------------------------------------------------------")
        print("'\t\tCi\t\t'\t\tNombre\t\t'\t\tEdad\t\t'")
        print("------------------------------------------------------------------------------------------------")
        print("\t\t", paciente[0], "\t\t","\t", paciente[1],"\t\t", "\t", paciente[2],"\t\t")
        
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (mt: ejemplo 1.65): "))
        result = peso / (altura ** 2)
        
        descripcion = "default"
        
        print("Su IMC es: ", result)
        if result < 18.5:
            descripcion = "Bajo peso"
        elif result >= 18.5 and result < 25:
            descripcion = "Peso normal"
        elif result >= 25 and result < 30:
            descripcion = "Sobrepeso"
        else:
            descripcion = "Obesidad"
        conexion = conectarDb()
        print("Su peso es: ", peso , "kg", "y su altura es: ", altura, "mt", "por lo tanto su IMC es: ", result, "y su estado es: ", descripcion)
        guardarImc(conexion, ci, peso, altura, result, descripcion)
        cerrarBase(conexion)
    
def consultarRegistros():
    print("********* Consultar registros *******")
    ci = input("Ingrese su CI: ")
    conexion = conectarDb()
    if conexion:
        paciente = getRegistros(conexion, ci)
        cerrarBase(conexion)
        if paciente[0] == "error":
            print("Paciente no encontrado, registrese")
            return
        pacientes = paciente[1]
        # print(paciente[1][4])
        
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("'\t\tCi\t\t'\t\tNombre\t\t'\t\tEdad\t\t'\tAltura\t\t'\tPeso\t\t'\tIMC\t\t'\tEstado\t\t'")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for i in pacientes:
            # print(i)
            print("\t\t", i[0], "\t\t", "\t", i[1], "\t\t", "\t", i[2], "\t\t", "\t", i[3], "\t\t", "\t",i[4], "\t\t", "\t", i[5], "\t\t", "\t", i[6], "\t\t ")

       