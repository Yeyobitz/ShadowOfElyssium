import os, sys, time, random
import random

# Variables
run = True
menu = True
play = False
rules = False
fight = False
standing = True

# Personaje
name = ""
health = 50
max_health = health
attack = 9999
defense = 3
gold = 0
level = 1
experience = 0
x = 1
y = 1
potions = 1
inventory = []
equipment = []
experience_needed = 1


# Mapa
#     x=0         x=1         x=2        x=3        x=4         x=5        x=6       x=7            x=8            x=9        
map = [
    ["plains",   "plains",   "plains",  "plains",  "forest",   "forest",   "forest", "mountains",   "mountains",  "mountains"],    # y=0
    ["plains",   "village",  "plains",  "forest",  "forest",   "evilWood", "forest", "mountains",   "ruined city","mountains"],    # y=1
    ["plains",   "plains",   "evilTown","swamp",   "evilWood", "evilWood", "forest", "ruined city", "mountains",  "mountains"],    # y=2
    ["plains",   "village",  "swamp",   "swamp",   "evilWood", "EldRuins", "evilWood","ruined city","mountains",  "beach"],        # y=3
    ["plains",   "plains",   "swamp",   "swamp",   "evilWood", "EldRuins", "forest", "mountains",   "beach",      "beach"],        # y=4
    ["plains",   "village",  "evilTown","swamp",   "forest",   "evilWood", "forest", "plains",      "plains",     "beach"],        # y=5
    ["forest",   "forest",   "swamp",   "evilTown","forest",   "forest",   "plains", "plains",      "plains",     "beach"],        # y=6
    ["forest",   "evilWood", "swamp",   "swamp",   "evilWood", "forest",   "plains", "ruined city", "plains",     "plains"],       # y=7
    ["mountains","forest",   "swamp",   "evilTown","evilWood", "EldRuins", "forest", "ruined city", "plains",     "plains"],       # y=8
    ["mountains","mountains","swamp",   "swamp",   "evilWood", "evilWood", "forest", "mountains",   "mountains",  "plains"]        # y=9
]

y_len = len(map)-1
x_len = len(map[0])-1

# Biomas
biom = {
    "plains":{
        "t": "ALTIPLANOS",
        "e": True
        },
    "forest":{
        "t": "BOSQUE",
        "e": True
    },
    "beach":{
        "t": "PLAYA",
        "e": True
    },
    "mountains":{
        "t": "MONTAÑAS",
        "e": True
    },
    "ruined city":{
        "t": "CIUDAD EN RUINAS",
        "e": True
    },
    "evilTown":{
        "t": "PUEBLO MALDITO",
        "e": True
    },
    "evilWood":{
        "t": "BOSQUE OSCURO",
        "e": True
    },
    "EldRuins":{
        "t": "RUINAS ELDRITCH",
        "e": True
    },
    "swamp":{
        "t": "PANTANO",
        "e": True
    },
    "village":{
        "t": "PUEBLO",
        "e": False
    }
    
}

current_tile = map[0][0]
name_of_tile = biom[current_tile]["t"]
ememy_tile = biom[current_tile]["e"]

# Enemigos
enemy = ""

e_list = [
    "Sujeto claramente transtornado",  # Aldeanos que han perdido la razón debido a la influencia eldritch.
    "Bestia poseída",  # Criaturas del bosque corrompidas por la energía oscura.
    "Espectro",  # Espíritus de aquellos que murieron en terror y no pueden encontrar la paz.
    "Cultista",  # Seguidores humanos de los Antiguos que buscan el caos y la destrucción.
    "Gárgola de Eldritch",  # Estatuas animadas por la magia oscura, guardianes de las ruinas eldritch.
    "Horror abisal",  # Criaturas que han emergido de las profundidades marinas, distorsionadas por fuerzas antiguas.
    "Pesadilla viviente",  # Encarnaciones de los temores más profundos de la humanidad, nacidos de la influencia eldritch.
    "Sombra de la locura",  # Sombras que han cobrado vida propia, acechando a aquellos con mentes fracturadas.
    "Cultista poseído",  # Cultistas que han sido completamente subyugados por los seres que adoran.
    "Acólito del Vacío",  # Jóvenes iniciados en los cultos eldritch, dedicados al estudio de lo oculto.
    "Médium Corrompido",  # Individuos que intentaron comunicarse con los Antiguos y fueron corrompidos.
    "Paladín Caído",  # Guerreros santos que sucumbieron a la tentación de poder oscuro.
    "Guardián de la Tumba",  # Custodios eternos de las tumbas y criptas, ahora corrompidos por la energía eldritch.
    "Cazador de Mentes",  # Criaturas elusivas que se alimentan del intelecto y la sanidad de sus víctimas.
    "Abominación de las Ruinas",  # Monstruosidades nacidas en las ruinas eldritch, deformadas y poderosas.
    "Avatar de la Desesperación",  # Manifestaciones físicas de la desesperación colectiva, alimentadas por el miedo.
    "Devorador de Almas",  # Entidades que cazan las almas de aquellos que se aventuran demasiado cerca de los portales.
    "Titán de los Antiguos",  # Gigantes de eras pasadas, despertados por la resonancia eldritch para sembrar el caos.
    "Engendro del Caos",  # Criaturas caóticas que existen solo para desordenar la realidad misma.
    "Emisario del Horizonte Estelar",  # Ser de otro mundo enviados como heraldos de los Antiguos.
    "Jefe Final: El Heredero de los Antiguos",  # La encarnación de la voluntad de los Antiguos, un enemigo casi divino.
    "ninguno"  # No hay enemigo
]

mobs = {
    "Sujeto claramente transtornado": {
        "health": 30,
        "attack": 3,
        "defense": 1,
        "gold": 5,
        "experience": 5
    },
    "Bestia poseída": {
        "health": 50,
        "attack": 5,
        "defense": 2,
        "gold": 10,
        "experience": 10
    },
    "Espectro": {
        "health": 40,
        "attack": 6,
        "defense": 0,  # No tiene defensa física pero podría tener inmunidad a ataques no mágicos
        "gold": 8,
        "experience": 12
    },
    "Cultista": {
        "health": 35,
        "attack": 4,
        "defense": 1,
        "gold": 7,
        "experience": 9
    },
    "Gárgola de Eldritch": {
        "health": 60,
        "attack": 7,
        "defense": 5,
        "gold": 15,
        "experience": 20
    },
    "Horror abisal": {
        "health": 70,
        "attack": 8,
        "defense": 3,
        "gold": 20,
        "experience": 25
    },
    "Pesadilla viviente": {
        "health": 45,
        "attack": 6,
        "defense": 2,
        "gold": 12,
        "experience": 15
    },
    "Sombra de la locura": {
        "health": 50,
        "attack": 5,
        "defense": 4,  # Su defensa es alta debido a su naturaleza etérea
        "gold": 10,
        "experience": 18
    },
    "Cultista poseído": {
        "health": 55,
        "attack": 7,
        "defense": 3,
        "gold": 14,
        "experience": 17
    },
    "Acólito del Vacío": {
        "health": 25,
        "attack": 4,
        "defense": 1,
        "gold": 6,
        "experience": 8
    },
    "Médium Corrompido": {
        "health": 40,
        "attack": 6,
        "defense": 2,
        "gold": 9,
        "experience": 11
    },
    "Paladín Caído": {
        "health": 65,
        "attack": 8,
        "defense": 6,
        "gold": 18,
        "experience": 22
    },
    "Guardián de la Tumba": {
        "health": 75,
        "attack": 9,
        "defense": 7,
        "gold": 22,
        "experience": 28
    },
    "Cazador de Mentes": {
        "health": 35,
        "attack": 5,
        "defense": 3,
        "gold": 11,
        "experience": 13
    },
    "Abominación de las Ruinas": {
        "health": 80,
        "attack": 10,
        "defense": 4,
        "gold": 25,
        "experience": 30
    },
    "Avatar de la Desesperación": {
        "health": 55,
        "attack": 7,
        "defense": 3,
        "gold": 14,
        "experience": 19
    },
    "Devorador de Almas": {
        "health": 60,
        "attack": 6,
        "defense": 5,
        "gold": 16,
        "experience": 21
    },
    "Titán de los Antiguos": {
        "health": 100,
        "attack": 12,
        "defense": 8,
        "gold": 30,
        "experience": 35
    },
    "Engendro del Caos": {
        "health": 90,
        "attack": 11,
        "defense": 4,
        "gold": 28,
        "experience": 33
    },
    "Emisario del Horizonte Estelar": {
        "health": 120,
        "attack": 15,
        "defense": 10,
        "gold": 50,
        "experience": 45
    },
    # Jefe Final
    "El Heredero de los Antiguos": {
        "health": 200,
        "attack": 20,
        "defense": 15,
        "gold": 100,
        "experience": 60
    }
}

# Pesos de los biomas para determinar la probabilidad de encontrar un enemigo
#                       Sujet-Besti-Espec-Culti-Gargo-Horro-Pesad-Sombra-Culti-Acol-Medium-Palad-Guard-Cazad-Abomi-Avata-Devor-Titan-Engen-Emisa-Jefe-Nada
plains_weight =         [0.15, 0.10, 0.00, 0.10, 0.00, 0.00, 0.00, 0.05, 0.05, 0.10, 0.05, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.30]
forest_weight =         [0.10, 0.15, 0.10, 0.05, 0.00, 0.00, 0.05, 0.00, 0.05, 0.05, 0.05, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.40]
dark_forest_weight =    [0.05, 0.10, 0.15, 0.10, 0.00, 0.05, 0.10, 0.05, 0.05, 0.00, 0.05, 0.00, 0.05, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.05, 0.00, 0.25]
swamp_weight =          [0.05, 0.10, 0.05, 0.05, 0.00, 0.15, 0.05, 0.05, 0.05, 0.05, 0.05, 0.00, 0.05, 0.10, 0.00, 0.05, 0.05, 0.00, 0.00, 0.00, 0.00, 0.30]
mountains_weight =      [0.05, 0.05, 0.05, 0.15, 0.10, 0.00, 0.00, 0.00, 0.10, 0.05, 0.00, 0.10, 0.10, 0.00, 0.00, 0.00, 0.00, 0.10, 0.05, 0.00, 0.00, 0.30]
beach_weight =          [0.10, 0.10, 0.00, 0.05, 0.00, 0.15, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00, 0.00, 0.05, 0.10, 0.00, 0.05, 0.00, 0.00, 0.05, 0.00, 0.35]
ruined_city_weight =    [0.05, 0.05, 0.10, 0.15, 0.10, 0.00, 0.05, 0.10, 0.15, 0.05, 0.05, 0.05, 0.00, 0.00, 0.10, 0.00, 0.00, 0.00, 0.00, 0.05, 0.00, 0.25]
village_weight =        [0.20, 0.10, 0.05, 0.10, 0.00, 0.00, 0.00, 0.05, 0.10, 0.10, 0.05, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.30]
cursed_village_weight = [0.05, 0.05, 0.10, 0.20, 0.00, 0.00, 0.10, 0.10, 0.20, 0.00, 0.05, 0.00, 0.00, 0.00, 0.05, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.20]
eldritch_ruins_weight = [0.00, 0.00, 0.05, 0.20, 0.15, 0.10, 0.05, 0.05, 0.10, 0.00, 0.05, 0.00, 0.00, 0.05, 0.10, 0.05, 0.05, 0.00, 0.05, 0.10, 0.05, 0.15]

#################################################################
######################## Lore del juego #########################
#################################################################

# Historia
"""
Esquema del Lore
Ambiente: El mundo de Elysium, un reino de fantasía medieval donde tierras antes pacíficas han sido corrompidas por la aparición de entidades de otro mundo, al estilo Lovecraft. Estas entidades han distorsionado la realidad y la naturaleza, introduciendo horrores que los habitantes de Elysium nunca han visto.

Conflicto: La barrera entre dimensiones se ha debilitado, permitiendo que criaturas eldritch se filtren en Elysium. Antiguos cultos adoran a estos seres, buscando aprovechar su poder para controlar las tierras.

Protagonista: Un héroe desconocido, que al igual que las entidades, acaba de aparecer. Su misión lo lleva a descubrir antiguos secretos y la verdadera naturaleza del cosmos y de sí mismo.

Antagonistas: Los Antiguos, poderosos y antiguos seres de más allá, y sus seguidores cultistas. Estas entidades desean remodelar Elysium a su imagen, propagando la locura y la desesperación.
"""

# Texto de inicio del juego
txt_intro = """Elysium...

Aquel reino una vez conocido como "El gran reino de la luz" 
ahora yace absorto en completa oscuridad.

La barrera entre dimensiones se ha
debilitado, permitiendo que seres y horrores ininarrables se 
infriltren en este plano. Han corrompido la tierra, 
distorsionado la realidad, la naturaleza y al mismo ser humano.

Despiertas un día y lo único que sabes es una cosa:
Debes encontrar la fuente de esta corrupción y detenerla
antes de que sea demasiado tarde...


"""
# Texto para las llanuras
txt_plains = """
Te encuentras en las llanuras de Elysium, un lugar aparentemente pacífico, pero sientes que algo siniestro se esconde bajo la superficie.
"""
# Texto para el bosque
txt_forest = """
El bosque de Elysium, otrora un lugar de gran belleza, ahora está torcido por una energía oscura. 
Un susurro te guía hacia un claro donde encuentras a Ilyana, la Alta Sacerdotisa. 
Ilyana te revela que la corrupción proviene de las ruinas eldritch al este y te da un amuleto para protegerte. 
Con nueva determinación, te adentras en el bosque oscuro hacia las ruinas eldritch.
"""
# Texto para la playa
txt_beach = """
Llegas a la playa de Elysium, donde el mar que antes era fuente de vida y comercio ahora arroja criaturas abisales a la costa. 
La arena está manchada con un musgo desconocido, brillando con una luz antinatural bajo la luna. 
Mientras exploras la orilla, te encuentras con restos de barcos antiguos, sus tripulaciones desaparecidas, quizás reclamadas por el mar o algo mucho peor.
"""
txt_mountains = ""
txt_ruined_city = ""
txt_cursed_village = ""
txt_dark_forest = ""
txt_eldritch_ruins = ""
txt_swamp = ""
txt_village = ""

# Texto placeholder
txt_placeholder = """Texto de relleno"""


#################################################################
######################### Funciones #############################
#################################################################


# Guardar
def save():
    list = [name, 
            health, 
            attack, 
            defense, 
            gold, 
            level, 
            experience,
            x,
            y,
            potions,
            inventory,
            equipment,
            experience_needed]
    
    f = open(f"{name}_save.txt", "w")
    
    for item in list:
        f.write(str(item) + "\n")
    f.close()

# Cargar
def load():
    global menu, play, name, health, attack, defense, gold, level, experience, x, y, potions, inventory, equipment, experience_needed
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
        x = int(lines[7])
        y = int(lines[8])
        potions = int(lines[9])
        inventory = lines[10]
        equipment = lines[11],
        experience_needed = int(lines[12])
        draw_line()
        print("Cargando juego...")
        time.sleep(2)
        print("Juego cargado!")
        time.sleep(1)
        print("Estos son tus datos: ")
        time.sleep(1)
        draw_line()
        print(f"Nombre: {name}")
        print(f"Salud: {health}")
        print(f"Ataque: {attack}")
        print(f"Defensa: {defense}")
        print(f"Oro: {gold}")
        print(f"Nivel: {level}")
        print(f"EXP: {experience}/{experience_needed}")        
        draw_line()
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
    
# Limpiar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dibujar línea
def draw_line():
    print("XXx<+><+><+><+><+><+><+><+><+><+><+><+><+><+><+><+>xXX")

# función para hacer que las palabras se escriban letra por letra rapidamente en pantalla
def type_text(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
# función para mostrar los stats del personaje
def show_stats():
    print(f"Nombre: {name}")
    print(f"Salud: {health}/{max_health}")
    print(f"Ataque: {attack}")
    print(f"Defensa: {defense}")
    print(f"Oro: {gold}")
    print(f"Nivel: {level}")
    print(f"Experiencia: {experience}")

def main_menu():
    global menu, play, rules, name
    clear()
    draw_line()
    print("1.- Juego Nuevo")
    print("2.- Cargar Juego")
    print("3.- Reglas")
    print("4.- Salir")
    draw_line()
    
    option = input("Ingrese una opción: ")
    
    if option == "1":
        clear()
        #type_text("Escuchas una voz en lo profundo de tu mente...\n", 0.03)
        #type_text("-Recuerda tu nombre.", 0.1)
        name = input("\n-> ")
        # menu, play y return deben estar al final, por ahora están aquí para pruebas
        menu = False
        play = True
        return
        clear()
        type_text(f"Cierto... Me llamo {name}", 0.05)
        time.sleep(1)
        type_text("...¿verdad?", 0.1)
        time.sleep(3)
        clear()
        type_text(txt_intro, 0.04)
        time.sleep(5)
        clear()
    elif option == "2":
        clear()
        load()
    elif option == "3":
        clear()
        menu = False
        rules = True
    elif option == "4":
        quit()
        
# Batalla aleatoria según el bioma
def random_battle():
    global standing, play, enemy
    # Batalla random
    if not standing:
        if biom[map[y][x]]["e"]:
            if current_tile == "plains":
                enemy = random.choices(e_list, weights=plains_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("Está tranquilo por aquí...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en las llanuras!")
                    battle()
                    standing = True
            elif current_tile == "forest":
                enemy = random.choices(e_list, weights=forest_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("El susurro de las hojas llena tu corazón de angustia...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en el bosque!")
                    battle()
                    standing = True
            elif current_tile == "beach":
                enemy = random.choices(e_list, weights=beach_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("La calma de las olas solo inquieta tu mente...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en la playa!")
                    battle()
                    standing = True
            elif current_tile == "mountains":
                enemy = random.choices(e_list, weights=mountains_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("El viento hiela hasta tus huesos...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en las montañas!")
                    battle()
                    standing = True
            elif current_tile == "ruined city":
                enemy = random.choices(e_list, weights=ruined_city_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("El eco de la ciudad en ruinas te hace sentir solo...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en la ciudad en ruinas!")
                    battle()
                    standing = True
            # en "village" no aparecen enemigos, es un lugar de compra/venta y descanzo
            elif current_tile == "village":
                standing = True
                print("Estás en un pueblo, no hay enemigos aquí...")
                time.sleep(3)
                clear()
                play = True
            elif current_tile == "cursed village":
                enemy = random.choices(e_list, weights=cursed_village_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("El aire está cargado con una energía oscura...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en el pueblo maldito!")
                    battle()
                    standing = True
            elif current_tile == "dark forest":
                enemy = random.choices(e_list, weights=dark_forest_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("No te puedes quitar la sensación de unos ojos clavados en ti...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en el bosque oscuro!")
                    battle()
                    standing = True
            elif current_tile == "eldritch ruins":
                enemy = random.choices(e_list, weights=eldritch_ruins_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("Las ruinas eldritch te hacen sentir pequeño...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en las ruinas eldritch!")
                    battle()
                    standing = True
            elif current_tile == "swamp":
                enemy = random.choices(e_list, weights=swamp_weight, k=1)[0]
                if enemy == "ninguno":
                    standing = True
                    print("El pantano te hace sentir atrapado...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    print(f"¡Te has encontrado con un {enemy} en el pantano!")
                    battle()
                    standing = True
        else:
            standing = True
            print("Estás en un lugar seguro...")
            time.sleep(3)
            clear()
            play = True                    
        
# Batalla contra el enemy que apareció en random_battle()
def battle():
    global name, health, attack, defense, gold, level, experience, potions, play
    global enemy
    enemy_health = mobs[enemy]["health"]
    enemy_max_health = mobs[enemy]["health"]
    enemy_attack = mobs[enemy]["attack"]
    enemy_defense = mobs[enemy]["defense"]
    enemy_gold = mobs[enemy]["gold"]
    enemy_experience = mobs[enemy]["experience"]
    while health > 0 and enemy_health > 0:
        draw_line()
        print(f"{name}: {health}/{max_health}")
        print(f"{enemy}: {enemy_health}/{enemy_max_health}")
        draw_line()
        print("1.- Atacar")
        print("2.- Usar poción")
        print("3.- Huir")
        draw_line()
        option = input("-> ")
        if option == "1":
            # Ataque del jugador
            damage = attack - enemy_defense
            if damage < 0:
                damage = 0
            enemy_health -= damage
            print(f"¡Le has quitado {damage} de salud al {enemy}!")
            time.sleep(2)
            if enemy_health <= 0:
                break
            # Ataque del enemigo
            damage = enemy_attack - defense
            if damage < 0:
                damage = 0
            health -= damage
            print(f"¡El {enemy} te ha quitado {damage} de salud!")
            time.sleep(2)
            clear()
        elif option == "2":
            if potions > 0:
                health += 30
                potions -= 1
                print("Has usado una poción y recuperado 30 puntos de salud.")
                time.sleep(2)
                clear()
            else:
                print("No tienes pociones...")
                time.sleep(2)
                clear()
        elif option == "3":
            probability = random.randint(1, 100)
            if probability > 50:
                type_text("N O  E S C A P A R A S\n", 0.05)
                time.sleep(2)
                clear()
            print("Has conseguido huir...")
            time.sleep(2)
            clear()
            play = True
            break
        else:
            print("Opción no válida")
            time.sleep(1)
            clear()
    if health <= 0:
        print("¡Has muerto!")
        time.sleep(1)
        print("Volverás al último punto de guardado...")
        time.sleep(2)
        clear()
        play = False
        menu = True
    elif enemy_health <= 0:
        print(f"¡Has derrotado al {enemy}!")
        time.sleep(1)
        print(f"Has ganado {enemy_gold} de oro y {enemy_experience} de experiencia.")
        gold += enemy_gold
        experience += enemy_experience
        if random.random() < 0.3:
            potions += 1
            print("El enemigo ha dejado caer una poción.")
        level_up()
        time.sleep(2)
        clear()
        play = True
        
# Función para subir de nivel al alcanzar cierta experiencia y aumentar los stats del jugador dependiendo de lo que él elija
# tendrá 3 puntos para subir entre +5 de salud, +1 de ataque y +1 de defensa
def level_up():
    global health, attack, defense, level, experience, experience_needed
    if experience >= experience_needed:
        print("¡Has subido de nivel!")
        level += 1
        experience_needed = 1 + (level * 0)
        experience -= experience
        points = 2
        while points > 0:
            draw_line()
            print(f"Salud: {health}")
            print(f"Ataque: {attack}")
            print(f"Defensa: {defense}")
            print(f"Puntos restantes: {points}")
            draw_line()
            print("1.- Salud (+5)")
            print("2.- Ataque (+1)")
            print("3.- Defensa (+1)")
            draw_line()
            option = input("-> ")
            if option == "1":
                health += 5
                points -= 1
                clear()
            elif option == "2":
                attack += 1
                points -= 1
                clear()
            elif option == "3":
                defense += 1
                points -= 1
                clear()
            else:
                print("Opción no válida")
                time.sleep(1)
                clear()
        print(f"Lvl: {level}")
        time.sleep(2)
        clear()



#################################################################
##################### Programa principal ########################
#################################################################

while run:
    while menu:
        main_menu()
    while play:
        save() # autosave
        clear()
        draw_line()
        print("Has llegado a " + biom[map[y][x]]["t"])
        time.sleep(1)
        random_battle()
        draw_line()
        print("1.- Mostrar stats")
        print("2.- Moverse")
        print("0.- Guardar y salir")
        draw_line()
        option = input("-> ")
        if option == "1":
            clear()
            show_stats()
            input("Presiona enter para continuar...")
            clear()
            play = True
        elif option == "2":
            clear()
            print("1.- Norte")
            print("2.- Este")
            print("3.- Sur")
            print("4.- Oeste")
            print("0.- Volver")
            draw_line()
            option = input("-> ")
            if option == "1":
                if y > 0:
                    y -= 1
                    standing = False
                else:
                    print("No hay nada más al norte...")
                    time.sleep(1)
                    clear()
                    play = True
            elif option == "2":
                if x < x_len:
                    x += 1
                    standing = False
                else:
                    print("No hay nada más al este...")
                    time.sleep(1)
                    clear()
                    play = True
            elif option == "3":
                if y < y_len:
                    y += 1
                    standing = False
                else:
                    print("No hay nada más al sur...")
                    time.sleep(1)
                    clear()
                    play = True
            elif option == "4":
                if x > 0:
                    x -= 1
                    standing = False
                else:
                    print("No hay nada más al oeste...")
                    time.sleep(1)
                    clear()
                    play = True
            elif option == "0":
                clear()
                play = True
            else:
                print("Opción no válida")
                time.sleep(1)
                clear()
                play = True
        elif option == "0":
            save()
            clear()
            play = False
            menu = True
        else:
            print("Opción no válida")
            time.sleep(1)
            clear()
            play = True
    while rules:
        print("Reglas del juego...")
        time.sleep(1)
        type_text(txt_placeholder, 0.08)
        time.sleep(1)
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
    