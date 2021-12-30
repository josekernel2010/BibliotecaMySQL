import os
from tabulate import tabulate
from libro import *


def inicio():
    os.system("cls")

    try:
        while True:
            print("**************************")
            print(':: Selecione una opción ::')
            print('**************************')
            print()
            print("\t1. Ingresar un libro")
            print("\t2. Ver todos los libros")
            print("\t3. Buscar un libro")
            print("\t4. Modificar un libro")
            print("\t5. Eliminar un libro")
            print("\t6. Salir de la aplicación")
            print()
            opcion = input("Escoja una opción: ")

            os.system("cls")

            if opcion == "1":
                nuevo_libro()
            elif opcion == "2":
                ver_libros()
            elif opcion == "3":
                buscar_libro()
            elif opcion == "4":
                modificar_libro()
            elif opcion == "5":
                eliminar_libro()
            elif opcion == "6":
                break
            else:
                print("--------------------------")
                print("Escoja una opción correcta")
                print("---------------------------")
    except AttributeError as err:
        print("***********************************")
        print(':: Error de conección ¯\_(ツ)_/¯ ::')
        print("***********************************")
        print()
        input("presione enter para continuar...")
        inicio()


def nuevo_libro():
    con = conectar()
    cursor = con.cursor()
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    estado = input("Ingrese el estado: ")
    os.system('cls')
    registro = registrar(titulo, autor, estado)
    print(len(registro) * '-')
    print(registro)
    print(len(registro) * '-')
    input("Presione enter para continuar...")
    os.system('cls')


def ver_libros():
    datos = mostrar()
    header = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
    tabla = tabulate(datos, header, tablefmt='fancy_grid')
    print(tabla)
    input("presione enter para seguir...")
    os.system('cls')


def buscar_libro():
    id = input("Ingrese el id del libro : ")
    os.system('cls')
    datos = buscar(id)

    if not datos:
        print("---------------------------------")
        print('*** El id del libro no existe ***')
        print("---------------------------------")
        input("Presione enter para continuar...")
        os.system('cls')
    else:
        header = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
        tabla = tabulate(datos, header, tablefmt='fancy_grid')
        print(tabla)
        input("Presione enter para continuar...")
        os.system('cls')


def modificar_libro():
    id = input("Ingrese el id del modificar : ")
    dato = buscar(id)

    if not dato:
        print("-------------------------------")
        print(':: El id del libro no existe ::')
        print('-------------------------------')
        input("Presione enter para continuar...")
        os.system('cls')

    else:
        header = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
        tabla = tabulate(dato, header, tablefmt='fancy_grid')
        print(tabla)
        nuevo_valor = ''
        print("---------------------------------------")
        campo = input("Seleccione el campo que desea modificar \n1. Titulo \n2. Autor \n3. Estado \n: ")

        while campo not in ['1', '2', '3']:
            os.system('cls')
            print("--------------------------")
            print("Escoja una opción correcta")
            print("--------------------------")
            campo = input("Seleccione el campo que desea modificar \n1. Titulo \n2. Autor \n3. Estado \n: ")

        if campo == '1':
            nuevo_valor = input("Ingerse el Titulo del libro : ")
        elif campo == '2':
            nuevo_valor = input("Ingerse el Autor del libro : ")
        elif campo == '3':
            nuevo_valor = input("Ingerse el Estado del libro : ")

        os.system('cls')

        respuesta = modificar(id, campo, nuevo_valor)
        print(len(respuesta) * "-")
        print(respuesta)
        print(len(respuesta) * "-")
        input("Presione enter para continuar...")
        os.system('cls')


def eliminar_libro():
    id = input("Ingrese el id del libro a eliminar : ")
    respuesta = eliminar(id)
    print(len(respuesta) * "-")
    print(respuesta)
    print(len(respuesta) * "-")
    input("Presione exit para continuar...")
    os.system('cls')


if __name__ == "__main__":
    inicio()
