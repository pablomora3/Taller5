import json
import os
import re
from collections import Counter
usernames = []
passwords = []
mails = []
data = {}
data['players'] = []
contraseña = ""

class Controller:

    #lectura del json y carga datos en listas
    @staticmethod
    def load_JSON_users():
        with open('existing_users.json') as file:
            data = json.load(file)

        for player in data['players']:
            usernames.append(player['username'])
            passwords.append(player['password'])
        
            mails.append(player['mail'])
    
    #Crear el usuario
    #Verifica si tiene espacios, si es alfanumeria, el tamaño del string, si tiene duplicados, si son solo numeros o solo letras
    #Crea un nuevo usuario y sobreescribe el json
    @staticmethod
    def create_new_user(user, passw, mail):
        contador = Counter(passw)
        duplicados = len([t[1] for t in list(contador.items()) if t[1] > 1])
        if user.isspace():
            print("El usuario no puede contener espacios")
        else:
            if passw.isalnum():
                if len(passw) >= 8:
                    if duplicados == 0:
                        if passw.isdigit() or passw.isalpha():
                            print("La contraseña debe ser alfanumerica, sin caracteres repetios y de 8 caracteres en adelante")
                        else:
                            if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',mail.lower()):
                                usernames.append(user)
                                passwords.append(passw)
                                mails.append(mail)
                                for u, p, m in zip(usernames, passwords, mails):
                                    data['players'].append({
                                    'username' : u,
                                    'password' : p,
                                    'mail' : m})

                                with open('existing_users.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                            else:
                                print("Correo electronico sin formato valido")
                    else:
                        print("La contraseña debe ser alfanumerica, sin caracteres repetios y de 8 caracteres en adelante")
                else:
                    print("La contraseña debe ser alfanumerica, sin caracteres repetios y de 8 caracteres en adelante")
            else:
                print("La contraseña debe ser alfanumerica, sin caracteres repetios y de 8 caracteres en adelante")

    #Verifica si el usuario ya existe, si no es asi llama al metodo crear usuario
    @staticmethod
    def validate_user_creation(usuario, password, mail):
        if usuario in usernames:
            print("El usuario ya existe")
        else:
            Controller.create_new_user(usuario, password, mail)
            Controller.load_JSON_users()

    #Lee todos los usuarios y los lista
    @staticmethod
    def load_all_users():
        print ("")
        for u in usernames:
            print(u)
        print ("")

    #Login del usuario verificando las condiciones de user y pass
    @staticmethod
    def login_JSON_user(user, passw):
        if user in usernames:
            contraseña = passwords[usernames.index(user)]
            if passw == str(contraseña):
                print ("")
                print("Credenciales correctos!")
                print ("")
            else:
                print ("")
                print("Contraseña equivocada")
                print ("")
        else:
            print ("")
            print("El usuario no existe")
            print ("")

    #Creando opciones del menu
    @staticmethod
    def imprimir():
        print("________________________")
        print("Bienvenido")
        print("________________________")
        print()
        print("1. Login")
        print("2. Registro")       
        print("3. Mostrar Usuarios")
        print("4. Salir")
        print()

    #Menu
    @staticmethod
    def Menu():
        Controller.load_JSON_users()

        while True:
            Controller.imprimir()
            opcion = input("Digite una opcion: ")

            if opcion == "1":
                usuario = input("Digite el usuario: ")
                password = input("Digite el password: ")
                Controller.login_JSON_user(usuario, password)
                input("Digite una tecla para continuar: ")

            if opcion == "2":
                usuario = input("Digite el usuario: ")
                password = input("Digite el password: ")
                mail = input("Digite el correo electronico: ")
                Controller.validate_user_creation(usuario, password, mail)
                input("Digite una tecla para continuar: ")

            if opcion == "3":
                Controller.load_all_users()

            if opcion == "4":
                break

Controller.Menu()

