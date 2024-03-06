import os, sys, time, random
import random

# Variables
run = True
menu = True
play = False
rules = False
credits = False
fight = False
autosave = False
# Personaje
class Character:
    def __init__(self, name, health, attack, defense, gold, level, experience, x, y, potions, inventory, equipment, experience_needed, standing):
        self.name = name
        self.health = health
        self.max_health = self.health
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.level = level
        self.experience = experience
        self.x = x
        self.y = y
        self.potions = potions
        self.inventory = inventory
        self.equipment = equipment
        self.experience_needed = experience_needed
        self.standing = standing
        
    def show_inventory(self):
        draw_line()
        print("Inventario:")
        draw_line()
        for index, item in enumerate(self.inventory, start=1):
            print(f"{index}. {item}")
        draw_line()
        print(f"Oro: {self.gold}")
        print(f"Pociones: {self.potions}")
        draw_line()
        print("Qué deseas hacer?")
        print("1. Equipar")
        print("2. Desequipar")
        print("3. Usar poción")
        print("4. Salir")
        draw_line()
        choice = input("-> ")
        if choice == "1":
            index = int(input("Número del objeto: "))
            self.equip(index)
        elif choice == "2":
            item = input("Nombre del objeto: ")
            self.unequip(item)
        elif choice == "3":
            self.use_potion()
        elif choice == "4":
            pass

    def equip(self, index):
        if index > 0 and index <= len(self.inventory):
            item = self.inventory[index-1]
            if item not in self.equipment:
                self.equipment.append(item)
                print(f"Has equipado {item}.")
                self.inventory.pop(index-1)
            else:
                print(f"{item} ya está equipado.")
        else:
            print("Opción no válida.")

    def unequip(self, item):
        if item in self.equipment:
            self.equipment.remove(item)
            print(f"Has desequipado {item}.")
        else:
            print(f"No tienes {item} equipado.")

# función para sumar la defensa de la armor a la defensa base del personaje y devolver el valor total
    def total_defense(self):
        total_defense = self.defense
        try:
            for armor in self.equipment:
                if armor in items and items[armor]["type"] == "armor":
                    total_defense += items[armor]["def"]
            return total_defense
        except:
            return self.defense        

    def use_potion(self):
        if self.potions > 0:
            self.health += 30
            self.potions -= 1
            print("Has bebido una poción. +30 de salud.")
        else:
            print("No tienes pociones.")

    def move(self, direction):
        draw_line()
        if direction == "1":
            if self.y > 1:
                draw_line()
                type_text("Caminas hacia el norte...")
                draw_line()
                self.y -= 1
                self.standing = False
                time.sleep(1.5)
            else:
                draw_big_line()
                print("Al norte no hay más que hielo y una muerte segura...")
                draw_big_line()
        elif direction == "2":
            if self.y < y_len:
                draw_line()
                type_text("Caminas hacia el sur...")
                draw_line()
                self.y += 1
                self.standing = False
                time.sleep(1.5)
            else:
                draw_big_line()
                print("Hay un gran abismo al sur imposible de cruzar...")
                draw_big_line()
        elif direction == "3":
            if self.x < x_len:
                draw_line()
                type_text("Caminas hacia el este...")
                draw_line()
                self.x += 1
                self.standing = False
                time.sleep(1.5)
            else:
                draw_big_line()
                print("El llano vacío y oscuro que se extiende\nal este no parece muy acogedor...")
                draw_big_line()
        elif direction == "4":
            if self.x > 0:
                draw_line()
                type_text("Caminas hacia el oeste...")
                draw_line()
                self.x -= 1
                self.standing = False
                time.sleep(1.5)
            else:
                draw_big_line()
                print("Al oeste quizás hayan tierras desconocidas\npero sin un barco no llegarás muy lejos...")
                draw_big_line()
        else:
            print("Dirección no válida.")

    def show_stats(self):
        print(f"Nombre: {self.name}")
        print(f"LVL: {self.level}")
        print(f"EXP: {self.experience}/{self.experience_needed}")
        print(f"HP: {self.health}/{self.max_health}")
        try:
            print(f"ATK: {self.attack} + {items[self.equipment[0]]['minAtk']}~{items[self.equipment[0]]['maxAtk']}")
        except:
            print(f"ATK: {self.attack}")
        try:
            print(f"DEF: {self.defense} + {items[self.equipment[1]]['def']}")
        except:
            print(f"DEF: {self.defense}")
        try:
            equipment = '\n\t'.join(self.equipment)
            print(f"Equipo: {equipment}")
        except:
            print("No tienes nada equipado.")

    def level_up(self):
        self.level += 1
        self.experience -= self.experience_needed
        self.experience_needed +=  int(float(1.5 * self.experience_needed))
        points = 2
        print(f"¡Has subido de nivel! Ahora eres nivel {self.level}.")
        print(f"Has ganado {points} puntos de habilidad.")
        while points > 0:
            draw_line()
            print("Puntos de habilidad restantes:", points)
            print("1. Aumentar salud máxima (+5).")
            print("2. Aumentar ataque (+2).")
            print("3. Aumentar defensa (+1).")
            draw_line()
            choice = input("Elige una opción: ")
            if choice == "1":
                self.max_health += 5
                self.health = self.max_health
                points -= 1
            elif choice == "2":
                self.attack += 2
                points -= 1
            elif choice == "3":
                self.defense += 1
                points -= 1
            else:
                print("Opción no válida.")
        print(f"HP: {self.max_health}")
        print(f"ATK: {self.attack}")   
        print(f"DEF: {self.defense}")
        
        
        """
        self.max_health += 10
        self.health = self.max_health
        self.attack += 2
        self.defense += 1
        """
        print(f"¡Has subido de nivel! Ahora eres nivel {self.level}.")

    def calculate_damage(self):
        # Check if the player's weapon is in the items dictionary and has attack values defined
        try:
            if self.equipment[0] in items and 'minAtk' in items[self.equipment[0]] and 'maxAtk' in items[self.equipment[0]]:
                weapon_damage = random.randint(items[self.equipment[0]]['minAtk'], items[self.equipment[0]]['maxAtk'])
            else:
                weapon_damage = 0
            total_damage = self.attack + weapon_damage
            return total_damage
        except:
            print("No tienes un arma equipada.")
            return self.attack

player = Character("", 30, 5, 3, 0, 1, 0, 1, 1, 3, [], ["Espada Corta", "Armadura de Cuero"], 100, True)

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = mobs[name]["health"]
        self.max_health = self.health
        self.attack = mobs[name]["attack"]
        self.defense = mobs[name]["defense"]
        self.gold = mobs[name]["gold"]
        self.experience = mobs[name]["experience"]
        self.weapon = mobs[name]["weapon"]
        self.armor = mobs[name]["armor"]
        self.drop_rate = mobs[name]["drop_rate"]
            
    def calculate_damage(self):
        # Check if the enemy's weapon is in the items dictionary and has attack values defined
        if self.weapon in items and 'minAtk' in items[self.weapon] and 'maxAtk' in items[self.weapon]:
            weapon_damage = random.randint(items[self.weapon]['minAtk'], items[self.weapon]['maxAtk'])
        else:
            weapon_damage = 0
        total_damage = self.attack + weapon_damage
        return total_damage
    
    def total_defense(self):
        total_defense = self.defense
        if self.armor in items and items[self.armor]["type"] == "armor":
            total_defense += items[self.armor]["def"]
        return total_defense
    
    # función para que el enemigo dropee un item; weapon o armor, de los que tiene equipado según el drop_rate definido en el diccionario de enemigos
    def drop_item(self):
        if random.random() < self.drop_rate:
            if self.weapon != "nothing":
                player.inventory.append(self.weapon)
                print(f"El {self.name} ha dejado caer {self.weapon}.")
            if self.armor != "nothing":
                player.inventory.append(self.armor)
                print(f"El {self.name} ha dejado caer {self.armor}.")
        else:
            print(f"El {self.name} no ha dejado caer nada.")
    

############################################## Items list ##############################################
# Haremos tantas espadas y armaduras como enemigos haya, para que cada uno tenga un set distinto que dropee
items_list = ["Espada Corta", "Garrote Astillado", "Garras Eldritch", "Susurro Fantasmal", "Daga de Cultista", "Espada Caída", "Túnica Desgarrada", "Escamas Abisales", "Vestimentas Etéreas", "Manto del Vacío", "Coraza del Paladín Caído", "nothing", "Lanza de Piedra", "Garras de Kruegger", "Muñeco Vuudú", "Ballesta Maldita", "Espada de Mil Gritos", "Dagas Gemelas del Caos", "Hacha del Cataclismo", "Maza del Núcleo Abisal", "Alabarda de Elyssium", "Espada de los Antiguos", "Loriga del Cazador de Mentes", "Coraza del Abismo Sin Estrellas", "Armadura de Elyssium", "Túnica de los Antiguos"]

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


######################################################################################################## 

############################################## Mapa ####################################################
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
########################################################################################################

############################################## Enemigos ################################################

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
    },
    "ninguno": {
        "health": 0,
        "attack": 0,
        "defense": 0,
        "gold": 0,
        "experience": 0,
        "weapon": "nothing",
        "armor": "nothing",
        "drop_rate": 0
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
########################################################################################################


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
def save(player):
    data = [player.name, 
            player.health, 
            player.attack, 
            player.defense, 
            player.gold, 
            player.level, 
            player.experience,
            player.x,
            player.y,
            player.potions,
            player.inventory,
            player.equipment,
            player.experience_needed]
    
    with open(f"{player.name}_save.txt", "w") as f:
        for item in data:
            f.write(str(item) + "\n")

# Cargar
def load():
    global menu, play, player
    try:
        name = input("Nombre EXACTO del personaje: ")
        with open(f"{name}_save.txt", "r") as f:
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
            equipment = lines[11]
            experience_needed = int(lines[12])
            standing = True
            draw_line()
            print("Cargando juego...")
            time.sleep(2)
            print("Juego cargado!")
            time.sleep(1)
            print("Estos son tus datos: ")
            time.sleep(1)
            draw_line()
            player = Character(name, health, attack, defense, gold, level, experience, x, y, potions, inventory, equipment, experience_needed, standing)
            print(f"Nombre: {player.name}")
            print(f"Nivel: {player.level}")
            print(f"Oro: {player.gold}")
            draw_line()
            time.sleep(1)
            print("Presiona enter para continuar...")
            input("-> ")
        clear()
        play = True
        menu = False
    except FileNotFoundError:
        print("Chanfle, no se encontró el archivo de guardado.")
        input("Presiona enter para continuar...")
        menu = True
        play = False

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
def draw_tabed_big_line():
    print("\t|~+X-------------------------------------------------------X+~|")
def draw_big_line():
    print("|~+X-------------------------------------------------------X+~|")
def draw_line():
    print("|~+X-----------------------------X+~|")

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
    
    
# función para mostrar el mapa conocido hasta ahora y posición actual
def show_map():
    global player
    for i in range(len(map)):
        for j in range(len(map[i])):
            if i == player.y and j == player.x:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()
    print(f"Estás en {biom[map[player.y][player.x]]['t']}")
    return
    
# función para mostrar introducción y título del juego
def intro_and_title():
    clear()
    draw_tabed_big_line()
    type_text(txt_intro, 0.02)
    draw_tabed_big_line()
    time.sleep(1)
    input("\n\t\t\t   -> Press Enter <-")
    clear()
    type_text_line(title, 0.1)
    input("\n\t\t\t-> Press Enter <-")
    clear()
    return

# función que maneja el inicio de un juego nuevo
def new_game():
    global menu, play, player
    #type_text("Escuchas una voz en lo profundo de tu mente...\n", 0.03)
    #type_text("\t R e c u e r d a  t u  n o m b r e .", 0.1)
    player.name = input("\n-> ")
    #clear()
    #type_text(f"Cierto... Me llamo {player.name}", 0.05)
    #time.sleep(1)
    #type_text("...¿verdad?", 0.1)
    #time.sleep(2)
    input("\n\n-> Press Enter <-\n")
    clear()
    #intro_and_title()
    #clear()
    menu = False
    play = True
    return

# función que maneja el menú principal
def main_menu():
    global menu, rules, credits
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
    global player, play, enemy
    # Batalla random
    if not player.standing:
        if biom[map[player.y][player.x]]["e"]:
            # Si hay enemigos en el bioma PLANICIE
            if current_tile == "plains":
                enemy_name = random.choices(e_list, weights=plains_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en las llanuras!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("Está tranquilo por aquí...")
                    draw_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
            
            # Si hay enemigos en el bioma BOSQUE        
            elif current_tile == "forest":
                enemy_name = random.choices(e_list, weights=forest_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en el bosque!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("El susurro de las hojas llena tu corazón de angustia...")
                    draw_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
                    
            # Si hay enemigos en el bioma PLAYA
            elif current_tile == "beach":
                enemy_name = random.choices(e_list, weights=beach_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en la playa!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("La calma de las olas inquieta tu mente...")
                    draw_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
                    
            # Si hay enemigos en el bioma MONTAÑAS
            elif current_tile == "mountains":
                enemy_name = random.choices(e_list, weights=mountains_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en las montañas!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("El viento hiela hasta tus huesos...")
                    draw_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
                    
            # Si hay enemigos en el bioma CIUDAD EN RUINAS
            elif current_tile == "ruined city":
                enemy_name = random.choices(e_list, weights=ruined_city_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en la ciudad en ruinas!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("El eco de la ciudad te hace sentir solo...")
                    draw_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
                    
            # Si hay enemigos en el bioma PUEBLO MALDITO
            elif current_tile == "cursed village":
                enemy_name = random.choices(e_list, weights=cursed_village_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en el pueblo maldito!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("El aire está cargado con una energía oscura...")
                    draw_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
                    
            # Si hay enemigos en el bioma BOSQUE OSCURO
            elif current_tile == "dark forest":
                enemy_name = random.choices(e_list, weights=dark_forest_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en el bosque oscuro!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_big_line()
                    print("No te puedes quitar la sensación de unos ojos clavados en ti...")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
                    
            # Si hay enemigos en el bioma RUINAS ELDRITCH
            elif current_tile == "eldritch ruins":
                enemy_name = random.choices(e_list, weights=eldritch_ruins_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en las ruinas eldritch!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("Las ruinas eldritch te hacen sentir pequeño...")
                    draw_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
                    
            # Si hay enemigos en el bioma PANTANO
            elif current_tile == "swamp":
                enemy_name = random.choices(e_list, weights=swamp_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en el pantano!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("El pantano te hace sentir atrapado...")
                    draw_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
        else:
            draw_line()
            print("Estás en un lugar seguro...")
            draw_line()
            input("\n-> Press Enter <-\n")
            clear()
            player.standing = True
            play = True
        

# Versión mejorada de la función battle() con el código actualizado de la clase Character y Enemy
def battle_v2(enemy_name):
    global menu, player, play
    global enemy
    enemy = Enemy(enemy_name)
    while player.health > 0 and enemy.health > 0:
        draw_line()
        print(f"{player.name}: {player.health}/{player.max_health}")
        print(f"{enemy_name}: {enemy.health}/{enemy.max_health}")
        draw_line()
        print("1.- Atacar")
        print("2.- Usar poción")
        print("3.- Huir")
        draw_line()
        option = input("-> ")
        draw_line()
        if option == "1":
            # Ataque del jugador
            damage = player.calculate_damage() - enemy.total_defense()
            if damage < 0:
                damage = 0
            enemy.health -= damage
            print(f"¡Le has quitado {damage} de salud al {enemy_name}!")
            time.sleep(2)
            if enemy.health <= 0:
                break
            # Ataque del enemigo
            damage = enemy.calculate_damage() - player.total_defense()
            if damage < 0:
                damage = 0
            player.health -= damage
            print(f"¡El {enemy_name} te ha quitado {damage} de salud!")
            time.sleep(2)
            clear()
        elif option == "2":
            if player.potions > 0:
                player.health += 30
                player.potions -= 1
                print("Has usado una poción y recuperado 30 puntos de salud.")
                time.sleep(2)
                clear()
            else:
                print("No tienes pociones...")
                time.sleep(2)
                clear()
        elif option == "3":
            probability = random.randint(1, 100)
            if probability > 70:
                clear()
                type_text("\tN O  E S C A P A R A S\n", 0.05)
                time.sleep(1)
                clear()
            clear()
            draw_line()
            print("Has conseguido huir...")
            draw_line()
            clear()
            play = True
            break
        else:
            print("Opción no válida")
            input("-> Press Enter <-")
            clear()
    if player.health <= 0:
        time.sleep(2)
        clear()
        draw_line()
        type_text("      Has muerto")
        time.sleep(1)
        type_text("Volverás al menú principal...")
        draw_line()
        input("-> Press Enter <-")
        clear()
        play = False
        menu = True
    elif enemy.health <= 0:
        print(f"¡Has derrotado al {enemy_name}!")
        time.sleep(1)
        print(f"Has ganado {enemy.gold} de oro y {enemy.experience} de experiencia.")
        player.gold += enemy.gold
        player.experience += enemy.experience
        
        if random.random() < enemy.drop_rate:
            # El enemigo ha dejado caer un item
            dropped_item = enemy.drop_item()
            if dropped_item != "nothing":
                print(f"{enemy_name} ha soltado {dropped_item}.")
            player.inventory.append(dropped_item)
            
        if random.random() < 0.1:
            player.potions += 1
            print("El enemigo ha dejado caer una poción.")
        # Subir de nivel
        if player.experience >= player.experience_needed:
            time.sleep(2)
            level_up()
            play = True
        else:
            time.sleep(2)
            clear()
            play = True

# versión mejorada y combinada de random_battle() y battle_v2()
def random_battle_v2():
    global player, play, enemy
    # Batalla random
    if not player.standing:
        if biom[map[player.y][player.x]]["e"]:
            if current_tile == "plains":
                enemy = random.choices(e_list, weights=plains_weight, k=1)[0]
                if enemy == "ninguno":
                    player.standing = True
                    print("Está tranquilo por aquí...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    enemy = Enemy(enemy)
                    print(f"¡Te has encontrado con un {enemy.name} en las llanuras!")
                    battle_v2()
            elif current_tile == "forest":
                enemy = random.choices(e_list, weights=forest_weight, k=1)[0]
                if enemy == "ninguno":
                    player.standing = True
                    print("El susurro de las hojas llena tu corazón de angustia...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    enemy = Enemy(enemy)
                    print(f"¡Te has encontrado con un {enemy} en el bosque!")
                    battle_v2()
            elif current_tile == "beach":
                enemy = random.choices(e_list, weights=beach_weight, k=1)[0]
                if enemy == "ninguno":
                    player.standing = True
                    print("La calma de las olas solo inquieta tu mente...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    enemy = Enemy(enemy)
                    print(f"¡Te has encontrado con un {enemy} en la playa!")
                    battle_v2()
            elif current_tile == "mountains":
                enemy = random.choices(e_list, weights=mountains_weight, k=1)[0]
                if enemy == "ninguno":
                    player.standing = True
                    print("El viento hiela hasta tus huesos...")
                    time.sleep(3)
                    clear()
                    play = True
                else:
                    enemy = Enemy(enemy)
                    print(f"¡Te has encontrado con un {enemy} en las montañas!")
                    battle_v2()
            elif current_tile == "ruined city":
                enemy = random.choices(e_list, weights=ruined_city_weight, k=1)[0]
                if enemy == "ninguno":
                    player.standing
# Función para subir de nivel y asignar puntos
def level_up():
    global player
    if player.experience >= player.experience_needed:
        clear()
        print("¡Has subido de nivel!")
        player.level += 1
        player.experience_needed += (player.level * 0)
        player.experience -= player.experience
        points = 2
        while points > 0:
            draw_line()
            print(f"Salud: {player.health}")
            print(f"Ataque: {player.attack}")
            print(f"Defensa: {player.defense}")
            print(f"Puntos restantes: {points}")
            draw_line()
            print("1.- Salud (+5)")
            print("2.- Ataque (+1)")
            print("3.- Defensa (+1)")
            draw_line()
            option = input("-> ")
            if option == "1":
                player.health += 5
                points -= 1
                clear()
            elif option == "2":
                player.attack += 1
                points -= 1
                clear()
            elif option == "3":
                player.defense += 1
                points -= 1
                clear()
            else:
                print("Opción no válida")
                time.sleep(1)
        print("¡Has asignado tus puntos!")
        time.sleep(2)
        print(f"Lvl: {player.level}")
        input("-> Press Enter <-")
        clear()

# función para moverse por el mapa
def move():
    global player, play, player
    draw_line()
    print("1.- Norte")
    print("2.- Sur")
    print("3.- Este")
    print("4.- Oeste")
    print("0.- Volver")
    draw_line()
    direction = input("-> ")
    try:
        player.move(direction)
        input("-> Press Enter <-")
    except Exception as e:
        print("Opción no válida")
        print(f"({e})")
        input("-> Press Enter <-")
        clear()

# función para tomar una poción
def drink_potion():
    global player
    if player.standing:
        if player.potions > 0:
            player.health += 30
            player.potions -= 1
            print(f"{player.health}/{player.max_health}")
            print(f"Te quedan {player.potions} pociones.")
            input("\n-> Press Enter <-")
        else:
            print("No tienes pociones...")
            input("\n-> Press Enter <-")

# función de play
def play_game():
    global play, menu, rules, credits, player, autosave
    if autosave:
        save() # autosave
    clear()
    random_battle()
    clear()
    draw_line()
    print("    Estás en " + biom[map[player.y][player.x]]["t"])
    draw_line()
    print(f"HP:{player.health}/{player.max_health} Lvl:{player.level}  Exp:{player.experience}/{player.experience_needed}")
    draw_line()
    print("1.- Investigar")
    print("2.- Moverse")
    print("3.- Mostrar mapa")
    print("4.- Mostrar inventario")
    print("5.- Mostrar stats")
    if biom[map[player.y][player.x]]["t"] == "Pueblo":
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
        player.show_inventory()
        clear()
        play = True
    elif option == "5":
        clear()
        draw_line()
        player.show_stats()
        draw_line()
        time.sleep(1)
        input("-> Press Enter <-\n")  
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
        save(player)
        clear()
        play = False
        menu = True
    else:
        print("Opción no válida")
        time.sleep(1)
        clear()
        play = True


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