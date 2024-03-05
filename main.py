import os, sys, time, random
import random

# Variables
run = True
menu = True
play = False
rules = False
credits = False
fight = False
standing = True

# Personaje
"""class Character:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.max_health = self.health
        self.attack = 5
        self.defense = 3
        self.gold = 0
        self.level = 1
        self.experience = 0
        self.x = 1
        self.y = 1
        self.potions = 3
        self.inventory = []
        self.equipment = ["Espada Corta", "Armadura de Cuero"]
        self.experience_needed = 50

player = Character("")
"""
name = ""
health = 50
max_health = health
attack = 5
defense = 3
gold = 0
level = 1
experience = 0
x = 1
y = 1
potions = 3
inventory = []
equipment = ["Espada Corta", "Armadura de Cuero"]
experience_needed = 50


# Items list
# Haremos tantas espadas y armaduras como enemigos haya, para que cada uno tenga un set distinto que dropee

items_list = ["Espada Corta", "Garrote Astillado", "Garras Eldritch", "Susurro Fantasmal", "Daga de Cultista", "Espada Caída", "Túnica Desgarrada", "Escamas Abisales", "Vestimentas Etéreas", "Manto del Vacío", "Coraza del Paladín Caído", "nothing", "Lanza de Piedra", "Garras de Kruegger", "Muñeco Vuudú", "Ballesta Maldita", "Espada de Mil Gritos", "Dagas Gemelas del Caos", "Hacha del Cataclismo", "Maza del Núcleo Abisal", "Alabarda de Elyssium", "Espada de los Antiguos", "Loriga del Cazador de Mentes", "Coraza del Abismo Sin Estrellas", "Armadura de Elyssium", "Túnica de los Antiguos"]


# Items
items = {
    # Armas
    "Espada Corta": {
        "type": "weapon", 
        "minAtk": 1,
        "maxAtk": 2,
        "price": 5
    },
    "Garrote Astillado": {
        "type": "weapon", 
        "minAtk": 0,
        "maxAtk": 3,
        "price": 10
    },
    "Garras Eldritch": {
        "type": "weapon", 
        "minAtk": 2,
        "maxAtk": 3,
        "price": 15
    },
    "Susurro Fantasmal": {
        "type": "weapon", 
        "minAtk": 0, 
        "maxAtk": 5,
        "price": 20
    },
    "Daga de Cultista": {
        "type": "weapon", 
        "minAtk": 1,
        "maxAtk": 3,
        "price": 25
    },
    "Lanza de Piedra": {
        "type": "weapon", 
        "minAtk": 5,
        "maxAtk": 6,
        "price": 40
    },
    "Espada Caída": {
        "type": "weapon", 
        "minAtk": 4,
        "maxAtk": 7,
        "price": 50
    },
    "Garras de Kruegger": {
        "type": "weapon", 
        "minAtk": 6,
        "maxAtk": 9,
        "price": 100
    },
    "Muñeco Vuudú": {
        "type": "weapon", 
        "minAtk": 5,
        "maxAtk": 10,
        "price": 150
    },
    "Ballesta Maldita": {
        "type": "weapon", 
        "minAtk": 9,
        "maxAtk": 12,
        "price": 200
    },
    "Espada de Mil Gritos": {
        "type": "weapon", 
        "minAtk": 11,
        "maxAtk": 14,
        "price": 220
    },
    "Dagas Gemelas del Caos": {
        "type": "weapon", 
        "minAtk": 14,
        "maxAtk": 15,
        "price": 225
    },

    "Hacha del Cataclismo": {
        "type": "weapon", 
        "minAtk": 13,
        "maxAtk": 17,
        "price": 240
    },
    "Maza del Núcleo Abisal": {
        "type": "weapon", 
        "minAtk": 12,
        "maxAtk": 18,
        "price": 270
    },
    "Alabarda de Elyssium": {
        "type": "weapon", 
        "minAtk": 15,
        "maxAtk": 20,
        "price": 400
    },
    "Espada de los Antiguos": {
        "type": "weapon", 
        "minAtk": 18,
        "maxAtk": 23,
        "price": 800
    },

    # Armaduras
    "Túnica Desgarrada": {
        "type": "armor", 
        "def": 1,
        "price": 3
    },
    "Armadura de Cuero": {
        "type": "armor", 
        "def": 2,
        "price": 5
    },
    "Escamas Abisales": {
        "type": "armor", 
        "def": 3,
        "price": 15
    },
    "Manto del Vacío": {
        "type": "armor", 
        "def": 4,
        "price": 25
    },
    "Sueter a Rayas": {
        "type": "armor", 
        "def": 5,
        "price": 50
    },
    "Vestimentas Etéreas": {
        "type": "armor", 
        "def": 6,
        "price": 80
    },
    "Vestiduras del Ritual Prohibido": {
        "type": "armor", 
        "def": 7,
        "price": 120
    },
    "Coraza del Paladín Caído": {
        "type": "armor", 
        "def": 8,
        "price": 150
    },
    "Vestimentas de la Locura": {
        "type": "armor", 
        "def": 9,
        "price": 200
    },
    "Loriga del Cazador de Mentes": {
        "type": "armor",
        "def": 12,
        "price": 300
    },
    "Coraza del Abismo Sin Estrellas": {
        "type": "armor", 
        "def": 15,
        "price": 500
    },
    "Armadura de Elyssium": {
        "type": "armor",
        "def": 20,
        "price": 1000
    },
    "Túnica de los Antiguos": {
        "type": "armor",
        "def": 25,
        "price": 1500
    }
    

    
    # Añade aquí el resto de las armas y armaduras para cada enemigo...
}


# Mapa
#     x=0         x=1         x=2        x=3        x=4         x=5        x=6       x=7            x=8            x=9        
map = [
    ["plains",   "plains",   "plains",  "plains",  "forest",   "forest",   "forest", "mountains",   "mountains",  "mountains"],    # y=0
    ["plains",   "village",  "village",  "forest",  "forest",   "evilWood", "forest", "mountains",   "ruined city","mountains"],    # y=1
    ["plains",   "plains",   "evilTown","swamp",   "evilWood", "evilWood", "forest", "ruined city", "mountains",  "mountains"],    # y=2
    ["plains",   "village",  "swamp",   "swamp",   "evilWood", "EldRuins", "evilWood","ruined city","mountains",  "beach"],        # y=3
    ["plains",   "plains",   "swamp",   "swamp",   "evilWood", "EldRuins", "forest", "mountains",   "beach",      "beach"],        # y=4
    ["plains",   "village",  "evilTown","swamp",   "forest",   "evilWood", "forest", "plains",      "plains",     "beach"],        # y=5
    ["forest",   "forest",   "swamp",   "evilTown","forest",   "forest",   "plains", "plains",      "plains",     "beach"],        # y=6
    ["forest",   "evilWood", "swamp",   "swamp",   "evilWood", "forest",   "plains", "ruined city", "plains",     "plains"],       # y=7
    ["mountains","forest",   "swamp",   "evilTown","evilWood", "EldRuins", "EldAltar", "ruined city", "plains",     "plains"],       # y=8
    ["mountains","mountains","swamp",   "swamp",   "evilWood", "evilWood", "forest", "mountains",   "mountains",  "plains"]        # y=9
]

y_len = len(map)-1
x_len = len(map[0])-1

# Biomas
biom = {
    "plains":{
        "t": "los Llanos",
        "e": True
        },
    "forest":{
        "t": "el Bosque",
        "e": True
    },
    "beach":{
        "t": "la Playa",
        "e": True
    },
    "mountains":{
        "t": "las Montañas",
        "e": True
    },
    "ruined city":{
        "t": "la Ciudad en Ruinas",
        "e": True
    },
    "evilTown":{
        "t": "el Pueblo Maldito",
        "e": True
    },
    "evilWood":{
        "t": "un Bosque Oscuro",
        "e": True
    },
    "EldRuins":{
        "t": "las Ruinas Eldritch",
        "e": True
    },
    "swamp":{
        "t": "PANTANO",
        "e": True
    },
    "village":{
        "t": "un pueblo tranquilo",
        "e": False
    },
    "EldAltar":{
        "t": "el Altar Eldritch",
        "e": False
    }
    
}

current_tile = map[0][0]
name_of_tile = biom[current_tile]["t"]
ememy_tile = biom[current_tile]["e"]

# Enemigos
enemy = ""
enemy_health = 0
enemy_max_health = enemy_health
enemy_attack = 0
enemy_defense = 0
enemy_gold = 0
enemy_experience = 0
enemy_weapon = ""
enemy_armor = ""
enemy_drop_rate = 0

# Lista de enemigos
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
        "attack": 2,
        "defense": 1,
        "gold": 2,
        "experience": 5,
        "weapon": "Garrote Astillado",
        "armor": "Túnica Desgarrada",
        "drop_rate": 0.2
    },
    "Bestia poseída": {
        "health": 40,
        "attack": 5,
        "defense": 2,
        "gold": 3,
        "experience": 10,
        "weapon": "Garras Eldritch",
        "armor": "nothing",
        "drop_rate": 0.3
    },
    "Espectro": {
        "health": 50,
        "attack": 4,
        "defense": 1,
        "gold": 3,
        "experience": 12,
        "weapon": "Susurro Fantasmal",
        "armor": "nothing",
        "drop_rate": 0.1
    },
    "Cultista": {
        "health": 45,
        "attack": 4,
        "defense": 1,
        "gold": 5,
        "experience": 9,
        "weapon": "Daga de Cultista",
        "armor": "Túnica Desgarrada",
        "drop_rate": 0.2
    },
    "Gárgola de Eldritch": {
        "health": 65,
        "attack": 7,
        "defense": 5,
        "gold": 7,
        "experience": 20,
        "weapon": "Lanza de Piedra",
        "armor": "Escamas Abisales",
        "drop_rate": 0.3
    },
    "Horror abisal": {
        "health": 70,
        "attack": 10,
        "defense": 4,
        "gold": 10,
        "experience": 25,
        "weapon": "Espada Caída",
        "armor": "Vestimentas Etéreas",
        "drop_rate": 0.3
    },
    "Pesadilla viviente": {
        "health": 90,
        "attack": 9,
        "defense": 6,
        "gold": 16,
        "experience": 30,
        "weapon": "Garras de Kruegger",
        "armor": "Sueter a Rayas",
        "drop_rate": 0.1
    },
    "Sombra de la locura": {
        "health": 50,
        "attack": 9,
        "defense": 4,
        "gold": 15,
        "experience": 18,
        "weapon": "Susurro Fantasmal",
        "armor": "Túnica Desgarrada",
        "drop_rate": 0.2
    },
    "Cultista poseído": {
        "health": 55,
        "attack": 7,
        "defense": 3,
        "gold": 20,
        "experience": 17,
        "weapon": "Daga de Cultista",
        "armor": "Vestiduras del Ritual Prohibido",
        "drop_rate": 0.2
    },
    "Acólito del Vacío": {
        "health": 25,
        "attack": 4,
        "defense": 1,
        "gold": 6,
        "experience": 8,
        "weapon": "Susurro Fantasmal",
        "armor": "Vestiduras del Ritual Prohibido",
        "drop_rate": 0.1
    },
    "Médium Corrompido": {
        "health": 40,
        "attack": 6,
        "defense": 2,
        "gold": 9,
        "experience": 11,
        "weapon": "Muñeco Vuudú",
        "armor": "Vestimentas de la Locura",
        "drop_rate": 0.1
    },
    "Paladín Caído": {
        "health": 65,
        "attack": 8,
        "defense": 6,
        "gold": 18,
        "experience": 22,
        "weapon": "Espada Caída",
        "armor": "Coraza del Paladín Caído",
        "drop_rate": 0.3
    },
    "Guardián de la Tumba": {
        "health": 75,
        "attack": 9,
        "defense": 10,
        "gold": 22,
        "experience": 25,
        "weapon": "Espada Caída",
        "armor": "Escamas Abisales",
        "drop_rate": 0.2
    },
    "Cazador de Mentes": {
        "health": 30,
        "attack": 15,
        "defense": 1,
        "gold": 30,
        "experience": 30,
        "weapon": "Ballesta Maldita",
        "armor": "Loriga del Cazador de Mentes",
        "drop_rate": 0.1
    },
    "Abominación de las Ruinas": {
        "health": 80,
        "attack": 10,
        "defense": 4,
        "gold": 25,
        "experience": 30,
        "weapon": "Espada Caída",
        "armor": "Vestimentas Etéreas",
        "drop_rate": 0.3
    },
    "Avatar de la Desesperación": {
        "health": 55,
        "attack": 7,
        "defense": 3,
        "gold": 14,
        "experience": 19,
        "weapon": "Espada de Mil Gritos",
        "armor": "Vestimentas de la Locura",
        "drop_rate": 0.2
    },
    "Devorador de Almas": {
        "health": 60,
        "attack": 6,
        "defense": 5,
        "gold": 16,
        "experience": 21,
        "weapon": "Hacla del Cataclismo",
        "armor": "Túnica Desgarrada",
        "drop_rate": 0.2
    },
    "Titán de los Antiguos": {
        "health": 100,
        "attack": 15,
        "defense": 8,
        "gold": 30,
        "experience": 35,
        "weapon": "Maza del Núcleo Abisal",
        "armor": "Coraza del Abismo Sin Estrellas",
        "drop_rate": 0.2
    },
    "Engendro del Caos": {
        "health": 90,
        "attack": 11,
        "defense": 4,
        "gold": 28,
        "experience": 33,
        "weapon": "Dagas Gemelas del Caos", 
        "armor": "Vestimentas de la Locura",
        "drop_rate": 0.3
    },
    "Emisario del Horizonte Estelar": {
        "health": 120,
        "attack": 15,
        "defense": 10,
        "gold": 50,
        "experience": 45,
        "weapon": "Alabarada de Elyssium",
        "armor": "Armadura de Elyssium",
        "drop_rate": 0.5
    },
    # Jefe Final
    "Heredero de los Antiguos": {
        "health": 200,
        "attack": 20,
        "defense": 15,
        "gold": 100,
        "experience": 60,
        "weapon": "Espada de los Antiguos",
        "armor": "Túnica de los Antiguos",
        "drop_rate": 0.5,
        "boss": True
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
eldritch_ruins_weight = [0.00, 0.00, 0.05, 0.20, 0.15, 0.10, 0.05, 0.05, 0.10, 0.00, 0.05, 0.00, 0.00, 0.05, 0.10, 0.05, 0.05, 0.00, 0.05, 0.10, 0.00, 0.20]
eldritch_altar_weight = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.99]

#################################################################
######################## Lore del juego #########################
#################################################################

# Historia
"""
Esquema del Lore
Ambiente: El mundo de Elyssium, un reino de fantasía medieval donde tierras antes pacíficas han sido corrompidas por la aparición de entidades de otro mundo, al estilo Lovecraft. Estas entidades han distorsionado la realidad y la naturaleza, introduciendo horrores que los habitantes de Elyssium nunca han visto.

Conflicto: La barrera entre dimensiones se ha debilitado, permitiendo que criaturas eldritch se filtren en Elyssium. Antiguos cultos adoran a estos seres, buscando aprovechar su poder para controlar las tierras.

Protagonista: Un héroe desconocido, que al igual que las entidades, acaba de aparecer. Su misión lo lleva a descubrir antiguos secretos y la verdadera naturaleza del cosmos y de sí mismo.

Antagonistas: Los Antiguos, poderosos y antiguos seres de más allá, y sus seguidores cultistas. Estas entidades desean remodelar Elyssium a su imagen, propagando la locura y la desesperación.
"""

# ASCII Art

# Créditos
yeyobitz = """
 __   __                   _      _  _        
 \\ \\ / /___  _   _   ___  | |__  (_)| |_  ____
  \\ V // _ \\| | | | / _ \\ | '_ \\ | || __||_  /
   | ||  __/| |_| || (_) || |_) || || |_  / / 
   |_| \\___| \\__, | \\___/ |_.__/ |_| \\__|/___|
             |___/                            """# Game title
title = """
     ██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   █     █░    ▒█████    █████▒
   ▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░   ▒██▒  ██▒▓██   ▒ 
   ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒█░ █ ░█    ▒██░  ██▒▒████ ░ 
     ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░░█░ █ ░█    ▒██   ██░░▓█▒  ░ 
   ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░░██▒██▓    ░ ████▓▒░░▒█░    
   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒     ░ ▒░▒░▒░  ▒ ░    
   ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░       ░ ▒ ▒░  ░      
   ░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░     ░ ░ ░ ▒   ░ ░    
         ░   ░  ░  ░      ░  ░   ░        ░ ░      ░           ░ ░          
                               ░                                            
      ▓█████  ██▓   ▓██   ██▓  ██████   ██████  ██▓ █    ██  ███▄ ▄███▓     
      ▓█   ▀ ▓██▒    ▒██  ██▒▒██    ▒ ▒██    ▒ ▓██▒ ██  ▓██▒▓██▒▀█▀ ██▒     
      ▒███   ▒██░     ▒██ ██░░ ▓██▄   ░ ▓██▄   ▒██▒▓██  ▒██░▓██    ▓██░     
      ▒▓█  ▄ ▒██░     ░ ▐██▓░  ▒   ██▒  ▒   ██▒░██░▓▓█  ░██░▒██    ▒██      
      ░▒████▒░██████▒ ░ ██▒▓░▒██████▒▒▒██████▒▒░██░▒▒█████▓ ▒██▒   ░██▒     
      ░░ ▒░ ░░ ▒░▓  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░▓  ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░     
       ░ ░  ░░ ░ ▒  ░▓██ ░▒░ ░ ░▒  ░ ░░ ░▒  ░ ░ ▒ ░░░▒░ ░ ░ ░  ░      ░     
         ░     ░ ░   ▒ ▒ ░░  ░  ░  ░  ░  ░  ░   ▒ ░ ░░░ ░ ░ ░      ░        
         ░  ░    ░  ░░ ░           ░        ░   ░     ░            ░        
                     ░ ░                                                    """
txt_intro = """
                               Elyssium...
           
                    Aquel reino una vez conocido como 
                       "El Gran Reino de la luz" 
                      ahora cubierto en oscuridad.
               
                          Por alguna razón
              la barrera entre dimensiones se ha debilitado, 
             permitiendo que seres y horrores ininarrables se 
                infriltren en nuestro plano existencial.
                
                    Han distorsionado la realidad, 
                        corrompido la tierra,
                            la naturaleza 
                           y al ser humano.
           
                Podrás descubrir lo que se esconde más allá
                        de la sombre de Elyssium?
"""


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
    global menu, play, name, health, attack, defense, gold, level, experience, x, y, potions, inventory, weapon, armor, experience_needed
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
def draw_big_line():
    print("\t~+X-------------------------------------------------------X+~")
def draw_line():
    print("~+X-----------------------------X+~")

# funciones para hacer que el texto aparezca de forma bonita
def type_text_line(text, delay=0.5):
    lines = text.split("\n")
    for line in lines:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(delay)
    print()
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

# función para mostrar el mapa conocido hasta ahora y posición actual
def show_map():
    global x, y
    for i in range(len(map)):
        for j in range(len(map[i])):
            if i == y and j == x:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()
    print(f"Estás en {biom[map[y][x]]['t']}")
    return
    
# función para mostrar introducción y título del juego
def intro_and_title():
    clear()
    draw_big_line()
    type_text(txt_intro, 0.02)
    draw_big_line()
    time.sleep(1)
    input("\n\t\t\t   -> Press Enter <-")
    clear()
    type_text_line(title, 0.1)
    input("\n\t\t\t-> Press Enter <-")
    clear()
    return

# función que maneja el inicio de un juego nuevo
def new_game():
    global menu, play, name
    type_text("Escuchas una voz en lo profundo de tu mente...\n", 0.03)
    type_text("\t R e c u e r d a  t u  n o m b r e .", 0.1)
    name = input("\n-> ")
    clear()
    type_text(f"Cierto... Me llamo {name}", 0.05)
    time.sleep(1)
    type_text("...¿verdad?", 0.1)
    time.sleep(2)
    input("\n\n-> Press Enter <-\n")
    clear()
    intro_and_title()
    clear()
    menu = False
    play = True
    return

# función que maneja el menú principal
def main_menu():
    global menu, rules, credits, name
    clear()
    draw_line()
    print("1.- Juego Nuevo")
    print("2.- Cargar Juego")
    print("3.- Reglas")
    print("4.- Créditos")
    print("0.- Salir")
    draw_line()
    
    option = input("-> ")
    
    if option == "1":
        clear()
        new_game()
    elif option == "2":
        clear()
        load()
    elif option == "3":
        clear()
        menu = False
        rules = True
    elif option == "4":
        clear()
        menu = False
        credits = True
    elif option == "0":
        quit()
        
# función que maneja las reglas del juego
def rules_menu():
    draw_line()
    type_text("\tR E G L A S", 0.05)
    draw_line()
    type_text("Para interactuar con los menús\nescribe en la consola la opción\nque deseas y luego dale al Enter.", 0.05)
    draw_line()
    type_text("El objetivo del juego es descubrir\nla verdad detrás de la sombra que\nha caído sobre Elyssium.\n", 0.05)
    draw_line()
    input("\n-> Press Enter <-\n")
    return
    
# función que muestra los créditos del juego
def credits_menu():
    global credits
    type_text("Juego creado por: ", 0.05)
    type_text_line(yeyobitz,0.666)
    input("\n-> Press Enter <-\n")
    return
    
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
    global menu, name, health, attack, defense, gold, level, experience, potions, play
    global enemy
    enemy_health = mobs[enemy]["health"]
    enemy_max_health = mobs[enemy]["health"]
    enemy_attack = mobs[enemy]["attack"]
    enemy_defense = mobs[enemy]["defense"]
    enemy_gold = mobs[enemy]["gold"]
    enemy_experience = mobs[enemy]["experience"]
    enemy_weapon = mobs[enemy]["weapon"]
    enemy_armor = mobs[enemy]["armor"]
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
        
        if random.random() < mobs[enemy]["drop_rate"]:
            # El enemigo ha dejado caer un item
            dropped_item = mobs[enemy]["item"]
            if dropped_item != "nothing":
                print(f"{enemy} ha soltado {dropped_item}.")
            inventory.append(dropped_item)
            
        if random.random() < 0.3:
            potions += 1
            print("El enemigo ha dejado caer una poción.")
        # Subir de nivel
        if experience >= experience_needed:
            time.sleep(2)
            level_up()
            play = True
        else:
            time.sleep(2)
            clear()
            play = True
        
# Función para subir de nivel y asignar puntos
def level_up():
    global health, attack, defense, level, experience, experience_needed
    if experience >= experience_needed:
        clear()
        print("¡Has subido de nivel!")
        level += 1
        experience_needed += (level * 0)
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

# función para moverse por el mapa
def move():
    global x, y, standing, play
    draw_line()
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

# función para tomar una poción
def drink_potion():
    global health, max_health, potions
    if standing:
        if potions > 0:
            health += 30
            potions -= 1
            print(f"{health}/{max_health}")
            print(f"Te quedan {potions} pociones.")
            input("\n-> Press Enter <-")
        else:
            print("No tienes pociones...")
            input("\n-> Press Enter <-")

# función de play
def play_game():
    global play, menu, rules, credits
    save() # autosave
    clear()
    random_battle()
    clear()
    draw_line()
    print("    Estás en " + biom[map[y][x]]["t"])
    draw_line()
    print("1.- Investigar")
    print("2.- Moverse")
    print("3.- Mostrar mapa")
    print("4.- Mostrar stats")
    print("5.- Tomar poción")
    if biom[map[y][x]]["t"] == "Pueblo":
        print("6.- Comprar")
    print("9.- Mostrar reglas")
    print("0.- Guardar y salir")
    draw_line()
    option = input("-> ")
    if option == "1":
        #investigate() AÑADIIIIIIIIIIIR
        print("Investigar")
        clear()
        play = True
    elif option == "2":
        clear()
        move()
        play = True
    elif option == "3":
        clear()
        show_map()
        input("-> Press Enter <-\n")
        clear()
        play = True
    elif option == "4":
        clear()
        show_stats()
        input("-> Press Enter <-\n")  
        clear()
        play = True
    elif option == "5":
        clear()
        drink_potion() 
        clear()
        play = True
    elif option == "6":
        #shop() AAAAAAAAÑAAAADIIIIIIIIIIIIIIIIIIIR
        pass
    elif option == "9":
        clear()
        rules_menu()
        rules = False
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

# función para equipar un weapon o armor, si ya hay uno equipado, se pregunta si se quiere desequipar el actual
# usaremos el índice del item en el inventario para equiparlo
# y le sumaremos ataque o defensa al personaje según el diccionario de items
def equip(character, item_name):
    global inventory
    """Equipar un objeto a un personaje."""
    if item_name in items_list and item_name in items:
        # Verificar si el objeto es un arma o una armadura y equiparlo adecuadamente
        if items[item_name]['type'] == 'weapon':
            # Desequipar el arma actual si existe una
            if 'weapon' in character['equipment']:
                print(f"{character['name']} ha desequipado {character['equipment']['weapon']}.")
            character['equipment']['weapon'] = item_name
            print(f"{character['name']} ahora está equipado con {item_name}.")
        elif items[item_name]['type'] == 'armor':
            # Desequipar la armadura actual si existe una
            if 'armor' in character['equipment']:
                print(f"{character['name']} ha desequipado {character['equipment']['armor']}.")
            character['equipment']['armor'] = item_name
            print(f"{character['name']} ahora está equipado con {item_name}.")
    else:
        print(f"El objeto {item_name} no existe.")

# función para ver el inventario
def show_inventory():
    clear()
    draw_line()
    print("Inventario")
    draw_line()
    for item in inventory:
        print(item)
    draw_line()
    input("-> Press Enter <-\n")
    clear()
    return
#################################################################
##################### Programa principal ########################
#################################################################

while run:
    while menu:
        main_menu()
    while play:
        play_game()
    while rules:
        rules_menu()
        rules = False
        menu = True
    while credits:
        credits_menu()
        credits = False
        menu = True