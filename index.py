from menu import crearPaciente
from menu import calcularImc
from menu import consultarRegistros

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def mostrar_menu():
    option = ""
    while option != "4":
        print("************ Menu ************")
        print("\t 1. Crear paciente")
        print("\t 2. Calcular Imc")
        print("\t 3. Consultar Paciente")
        print("\t 4. Exit")
        option = input("Elige una opción: ")
        opcionesUsuario(option)

def opcionesUsuario (opcion):
    if opcion == "1":
        clear_console()
        crearPaciente()
    if opcion == "2":
        clear_console()
        calcularImc()
    if opcion == "3":
        clear_console()
        consultarRegistros()

def main():
    # menuitems()
    clear_console()
    mostrar_menu()

if __name__ == "__main__":
    main()