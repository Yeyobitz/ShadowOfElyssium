import os
import time

run = True
menu = True
play = False
rules = False

name = ""
health = 100
attack = 10
defense = 5
gold = 0
level = 1
experience = 0

def save():
    list = [name, 
            health, 
            attack, 
            defense, 
            gold, 
            level, 
            experience]
    
    f = open(f"{name}_save.txt", "w")
    
    for item in list:
        f.write(str(item) + "\n")
    f.close()
    
def load():
    global menu, play, name, health, attack, defense, gold, level, experience
    try:
        name = input("Nombre EXACTO del personaje: ")
        f = open(f"{name}_save.txt", "r")
        lines = f.readlines()
        name = lines[0].replace("\n", "")
        health = int(lines[1])
        attack = int(lines[2])
        defense = int(lines[3])
        gold = int(lines[4])
        level = int(lines[5])
        experience = int(lines[6])
        print("Cargando juego...")
        time.sleep(2)
        print("Juego cargado!")
        time.sleep(1)
        print("Estos son tus datos: ")
        time.sleep(1)
        print(f"Nombre: {name}")
        print(f"Salud: {health}")
        print(f"Ataque: {attack}")
        print(f"Defensa: {defense}")
        print(f"Oro: {gold}")
        print(f"Nivel: {level}")
        print(f"Experiencia: {experience}")
        time.sleep(1)
        print("Presiona enter para continuar...")
        input("-> ")
        f.close()
        clear()
        play = True
        menu = False     

    except Exception as e:
        print("Chanfle, no se encontró el archivo de guardado.")
        print(f"({e})")
        input("Presiona enter para continuar...")
        menu = True
        play = False
    

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
while run:
    while menu:
        clear()
        print("1.- Juego Nuevo")
        print("2.- Cargar Juego")
        print("3.- Reglas")
        print("4.- Salir")
        
        option = input("Ingrese una opción: ")
        
        if option == "1":
            clear()
            name = input("Oh valiente guerrero, o guerrera, qué se yo, decidme, cual es vuestro nombre?\n-> ")
            menu = False
            play = True
        elif option == "2":
            clear()
            load()
        elif option == "3":
            clear()
            menu = False
            rules = True
        elif option == "4":
            quit()
            
    while play:
        save()
        print(f"Bienvenido {name}!")
        option = input("-> ")
        if option == "0":
            play = False
            menu = True
            
    while rules:
        print("Reglas del juego...")
        print("Presiona 0 para salir...")
        option = input("-> ")
        if option == "0":
            clear()
            rules = False
            menu = True
        else:
            print("Opción no válida")
            time.sleep(1)
            clear()
            rules = True
            menu = False
    