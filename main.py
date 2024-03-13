import os, sys, time, random
print("Starting script...")
os.system('chcp 65001' if os.name == 'nt' else 'clear')

# rest of your code
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
    def __init__(self, name, health, attack, defense, speed, gold, level, experience, x, y, potions, inventory, equipment, experience_needed):
        self.name = name
        self.health = health
        self.max_health = self.health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.gold = gold
        self.level = level
        self.experience = experience
        self.x = x
        self.y = y
        self.potions = potions
        self.inventory = inventory
        self.equipment = equipment
        self.experience_needed = experience_needed
        self.standing = True
        self.keys = 0
        self.defeated_emissary_coords = []
        
    def show_inventory(self):
        try:
            draw_line()
            print("Inventario:")
            draw_line()
            for i, item in enumerate(self.inventory, start=1):
                print(f"{i}. {item}  ATK {items[item]['minAtk']}-{items[item]['maxAtk']}" if 'minAtk' in items[item] and 'maxAtk' in items[item] else f"{i}. {item}  DEF {items[item]['def']}" if 'def' in items[item] else f"{i}. {item}")
            draw_line()
            print(f"Oro: {self.gold} | Pociones: {self.potions} | Orbes: {self.keys}")
            draw_line()
            print("Qué deseas hacer?")
            print("1. Equipar")
            print("2. Mostrar Estado")
            print("3. Usar poción")
            print("0. Salir")
            draw_line()
            choice = input("-> ")
            draw_line()
            try:
                choice = int(choice)
                if choice == 1:
                    
                    index = int(input("Número del objeto: "))
                    self.equip(index)
                elif choice == 2:
                    clear()
                    self.show_stats()
                    clear()
                elif choice == 3:
                    self.use_potion()
                    clear()
                elif choice == 0:
                    pass
                else:
                    print("Opción no válida.")
                    input("-> Press Enter <-")
                    clear()
            except ValueError:
                print("Opción no válida.")
                input("-> Press Enter <-")
                clear()
        except Exception as e:
            print("Ha ocurrido un error al mostrar el inventario.")
            print(f"({e})")
            input("-> Press Enter <-")
            clear()
    def __str__(self):
        return f"Nombre: {self.name}\nSalud: {self.health}\nAtaque: {self.attack}\nDefensa: {self.defense}\nVelocidad: {self.speed}\nOro: {self.gold}\nNivel: {self.level}\nExperiencia: {self.experience}/{self.experience_needed}\nPosición: ({self.x}, {self.y})"

    def equip(self, index):
        try:
            if index > 0 and index <= len(self.inventory):
                item = self.inventory[index-1]
                if item in self.equipment:
                    print(f"{item} ya está equipado.")
                elif "weapon" in items[item]["type"]:
                    if self.equipment[0] != "nothing":
                        self.inventory.append(self.equipment[0])
                        self.inventory.pop(index-1)
                    self.equipment[0] = item
                    print(f"Has equipado {item}.")
                elif "armor" in items[item]["type"]:
                    if self.equipment[1] != "nothing":
                        self.inventory.append(self.equipment[1])
                        self.inventory.pop(index-1)
                    self.equipment[1] = item
                    print(f"Has equipado {item}.")
                else:
                    print("Objeto no equipable.")
            draw_line()
            input("-> Press Enter <-")
        except Exception as e:
            print("Ha ocurrido un error al equipar el objeto.")
            print(f"({e})")
            input("-> Press Enter <-")

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
            self.health = min(self.max_health, self.health + 30)
            self.potions -= 1
            print("Has bebido una poción. +30 de salud.")
        else:
            print("No tienes pociones.")

    def move(self):
        draw_line()
        print("1.- Norte   ↑")
        print("2.- Sur     ↓")
        print("3.- Este    →")
        print("4.- Oeste   ←")
        print("")
        print("9.- Mapa    M")
        print("")
        print("0.- Volver")
        draw_line()
        direction = input("-> ")
        try:
            if direction == "1":
                if self.y > 0:
                    draw_line()
                    type_text("Caminas hacia el norte...")
                    draw_line()
                    self.y -= 1
                    self.standing = False
                    if player.standing == False:
                        random_battle()
                        clear()
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
                    if player.standing == False:
                        random_battle()
                        clear()
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
                    if player.standing == False:
                        random_battle()
                        clear()
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
                    if player.standing == False:
                        random_battle()
                        clear()
                    time.sleep(1.5)
                else:
                    draw_big_line()
                    print("Al oeste quizás hayan tierras desconocidas\npero sin un barco no llegarás muy lejos...")
                    draw_big_line()
            elif direction == "9" or direction.lower() == "m":
                clear()
                draw_line()
                show_map()
                draw_line()
                input("-> Press Enter <-")
                clear()
            elif direction == "0":
                pass
            
        except Exception as e:
            print("Opción no válida")
            print(f"({e})")
            input("-> Press Enter <-")
            clear()

    def show_stats(self):
        clear()
        draw_line()
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
        print(f"SPD: {self.speed}")
        try:
            equipment = '\n\t'.join(self.equipment)
            print(f"Equipo: {equipment}")
        except:
            print("No tienes nada equipado.")
        draw_line()
        input("-> Press Enter <-")
        self.show_inventory()

    def level_up(self):
        try:
            self.level += 1
            self.experience -= self.experience_needed
            self.experience_needed += int(float(1.2 * self.experience_needed))
            points = 3
            print(f"¡Has subido de nivel! Ahora eres nivel {self.level}.")
            print(f"Has ganado {points} puntos de habilidad.")
            while points > 0:
                draw_line()
                print("Puntos de habilidad restantes:", points)
                print("1. Aumentar salud máxima (+5).")
                print("2. Aumentar ataque (+1).")
                print("3. Aumentar defensa (+1).")
                print("4. Aumentar velocidad (+1).")
                draw_line()
                choice = input("Elige una opción: ")
                if choice == "1":
                    self.max_health += 20
                    self.health = self.max_health
                    points -= 1
                elif choice == "2":
                    self.attack += 2
                    points -= 1
                elif choice == "3":
                    self.defense += 1
                    points -= 1
                elif choice == "4":
                    self.speed += 1
                    points -= 1
                else:
                    print("Opción no válida.")
            print(f"HP: {self.max_health}")
            print(f"ATK: {self.attack}")   
            print(f"DEF: {self.defense}")
            print(f"SPD: {self.speed}")
            draw_line()
            input("-> Press Enter <-")
            clear()
        except Exception as e:
            print("Ha ocurrido un error al subir de nivel.")
            print(f"({e})")
            input("-> Press Enter <-")
        
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


try:
    player = Character("", 100, 999, 999, 999, 100, 1, 0, 1, 1, 3, [], ["Espada Corta", "Armadura de Cuero"], 10)
except Exception as e:
    print(f"An error occurred while creating the player: {str(e)}")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = mobs[name]["health"]
        self.max_health = self.health
        self.attack = mobs[name]["attack"]
        self.defense = mobs[name]["defense"]
        self.speed = mobs[name]["speed"]
        self.gold = mobs[name]["gold"]
        self.experience = mobs[name]["experience"]
        self.weapon = mobs[name]["weapon"]
        self.armor = mobs[name]["armor"]
        self.drop_rate = mobs[name]["drop_rate"]
        self.level = 1
            
    def calculate_damage(self):
        try:
            # Check if the enemy's weapon is in the items dictionary and has attack values defined
            if self.weapon in items and 'minAtk' in items[self.weapon] and 'maxAtk' in items[self.weapon]:
                weapon_damage = random.randint(items[self.weapon]['minAtk'], items[self.weapon]['maxAtk'])
            else:
                weapon_damage = 0
            total_damage = self.attack + weapon_damage
            return total_damage
        except:
            # Handle any exception that occurs
            print("An error occurred while calculating enemy total damage.")
            return 0
    def total_defense(self):
        try:
            total_defense = self.defense
            if self.armor in items and items[self.armor]["type"] == "armor":
                total_defense += items[self.armor]["def"]
            return total_defense
        except:
            print("An error occurred while calculating enemy total defense.")
            return 0
    
    # función para que el enemigo dropee un item; weapon o armor, de los que tiene equipado según el drop_rate definido en el diccionario de enemigos
    def drop_item(self):
        try:
            if random.random() < self.drop_rate:
                if self.weapon != "nothing":
                    player.inventory.append(self.weapon)
                    print(f"El {self.name} ha dejado caer {self.weapon}.")
                if self.armor != "nothing":
                    player.inventory.append(self.armor)
                    print(f"El {self.name} ha dejado caer {self.armor}.")
            else:
                print(f"El {self.name} no ha dejado caer nada.")
        except Exception as e:
            print(f"An error occurred while dropping item: {str(e)}")
    
    
    # función para subir del nivel al enemigo dependiendo del nivel del jugador
    # el atk, def, hp y vel del enemigo suben cada uno entre 0 a 2 puntos por cada nivel del jugador al momento de la pelea
    def level_up(self):
        try:
            level_difference = 3*(player.level - 1)
            for _ in range(level_difference):
                self.level += 1
                choice = random.randint(0, 3)
                if choice == 0:
                    self.attack += 1
                elif choice == 1:
                    self.defense += 1
                elif choice == 2:
                    self.health += 20
                elif choice == 3:
                    self.speed += 1
        except Exception as e:
            print(f"An error occurred while leveling up the enemy: {str(e)}")
        self.max_health = self.health
        self.experience += int(self.experience * 0.2 * level_difference)
        self.gold += int(self.gold * 0.2 * level_difference)
        

############################################## Items list ##############################################
# Haremos tantas espadas y armaduras como enemigos haya, para que cada uno tenga un set distinto que dropee
items_list = ["Espada Corta", "Garrote Astillado", "Garras Eldritch", "Susurro Fantasmal", "Daga de Cultista", "Espada Caída", "Túnica Desgarrada", "Escamas Abisales", "Vestimentas Etéreas", "Manto del Vacío", "Coraza del Paladín Caído", "nothing", "Lanza de Piedra", "Garras de Kruegger", "Muñeco Vuudú", "Ballesta Maldita", "Espada de Mil Gritos", "Dagas Gemelas del Caos", "Hacha del Cataclismo", "Maza del Núcleo Abisal", "Alabarda de Elyssium", "Espada de los Antiguos", "Loriga del Cazador de Mentes", "Coraza del Abismo Sin Estrellas", "Armadura de Elyssium", "Túnica de los Antiguos"]

items = {
    # Armas
    "Espada Corta": {
        "type": "weapon", 
        "minAtk": 4,
        "maxAtk": 7,
        "price": 25
    },
    "Garrote Astillado": {
        "type": "weapon", 
        "minAtk": 1,
        "maxAtk": 9,
        "price": 50
    },
    "Garras Eldritch": {
        "type": "weapon", 
        "minAtk": 3,
        "maxAtk": 8,
        "price": 88
    },
    "Susurro Fantasmal": {
        "type": "weapon", 
        "minAtk": 0, 
        "maxAtk": 15,
        "price": 154
    },
    "Daga de Cultista": {
        "type": "weapon", 
        "minAtk": 6,
        "maxAtk": 8,
        "price": 125
    },
    "Lanza de Piedra": {
        "type": "weapon", 
        "minAtk": 7,
        "maxAtk": 13,
        "price": 199
    },
    "Espada Caída": {
        "type": "weapon", 
        "minAtk": 11,
        "maxAtk": 15,
        "price": 325
    },
    "Garras de Kruegger": {
        "type": "weapon", 
        "minAtk": 13,
        "maxAtk": 14,
        "price": 500
    },
    "Muñeco Vuudú": {
        "type": "weapon", 
        "minAtk": 5,
        "maxAtk": 20,
        "price": 666
    },
    "Ballesta Maldita": {
        "type": "weapon", 
        "minAtk": 11,
        "maxAtk": 18,
        "price": 888
    },
    "Espada de Mil Gritos": {
        "type": "weapon", 
        "minAtk": 19,
        "maxAtk": 24,
        "price": 1150
    },
    "Dagas Gemelas del Caos": {
        "type": "weapon", 
        "minAtk": 21,
        "maxAtk": 21,
        "price": 1666
    },

    "Hacha del Cataclismo": {
        "type": "weapon", 
        "minAtk": 18,
        "maxAtk": 28,
        "price": 2888
    },
    "Maza del Núcleo Abisal": {
        "type": "weapon", 
        "minAtk": 22,
        "maxAtk": 30,
        "price": 3500
    },
    "Alabarda de Elyssium": {
        "type": "weapon", 
        "minAtk": 25,
        "maxAtk": 35,
        "price": 5000
    },
    "Espada de los Antiguos": {
        "type": "weapon", 
        "minAtk": 33,
        "maxAtk": 33,
        "price": 9999
    },

    # Armaduras
    "Túnica Desgarrada": {
        "type": "armor", 
        "def": 2,
        "price": 100
    },
    "Armadura de Cuero": {
        "type": "armor", 
        "def": 4,
        "price": 200
    },
    "Escamas Abisales": {
        "type": "armor", 
        "def": 6,
        "price": 300
    },
    "Manto del Vacío": {
        "type": "armor", 
        "def": 8,
        "price": 400
    },
    "Sueter a Rayas": {
        "type": "armor", 
        "def": 10,
        "price": 500
    },
    "Vestimentas Etéreas": {
        "type": "armor", 
        "def": 12,
        "price": 600
    },
    "Vestiduras del Ritual Prohibido": {
        "type": "armor", 
        "def": 14,
        "price": 800
    },
    "Coraza del Paladín Caído": {
        "type": "armor", 
        "def": 16,
        "price": 1000
    },
    "Vestimentas de la Locura": {
        "type": "armor", 
        "def": 20,
        "price": 1500
    },
    "Loriga del Cazador de Mentes": {
        "type": "armor",
        "def": 21,
        "price": 2000
    },
    "Coraza del Abismo Sin Estrellas": {
        "type": "armor", 
        "def": 22,
        "price": 3000
    },
    "Armadura de Elyssium": {
        "type": "armor",
        "def": 23,
        "price": 5000
    },
    "Túnica de los Antiguos": {
        "type": "armor",
        "def": 25,
        "price": 9999
    }
    

    
    # Añade aquí el resto de las armas y armaduras para cada enemigo...
}


# Constants for map biomes
PLAINS = 'plains'
FOREST = 'forest'
TOWER = 'tower'
MOUNTAIN = 'mountains'
VILLAGE = 'village'
ELD_TOWN = 'EldTown'
ELD_RUIN = 'EldRuins'
ELD_ALTAR = 'EldAltar'
BEACH = 'beach'
SWAMP = 'swamp'

def is_valid_placement(map, row, col, biome, min_distance=1):
    #Ensure placement is within map bounds and respects biome constraints
    for r in range(max(0, row - min_distance), min(10, row + min_distance + 1)):
        for c in range(max(0, col - min_distance), min(10, col + min_distance + 1)):
            if map[r][c] == biome:
                return False
    return True

def place_biome(map, biome, count=1, near_biome=None, min_distance=1):
    #Place biomes considering biome constraints and avoiding out-of-bounds errors.
    attempts = 0
    while count > 0 and attempts < 1000:
        row, col = random.randint(0, 9), random.randint(0, 9)
        if map[row][col] == PLAINS and (near_biome is None or any(map[max(0, min(9, r))][max(0, min(9, c))] == near_biome for r in range(row-1, row+2) for c in range(col-1, col+2) if 0 <= r < 10 and 0 <= c < 10)) and is_valid_placement(map, row, col, biome, min_distance):
            map[row][col] = biome
            count -= 1
        attempts += 1
        
def place_mountains(map):
    mountain_count = 0
    for i in range(10):
        if random.random() < 0.3 and mountain_count < 10:
            map[0][i] = MOUNTAIN
            mountain_count += 1
        if random.random() < 0.3 and mountain_count < 10:
            map[9][i] = MOUNTAIN
            mountain_count += 1
        if random.random() < 0.3 and mountain_count < 10:
            map[i][0] = MOUNTAIN
            mountain_count += 1
        if random.random() < 0.3 and mountain_count < 10:
            map[i][9] = MOUNTAIN
            mountain_count += 1

def place_beaches(map):
    beach_count = 0
    for i in range(10):
        for j in range(10):
            if map[i][j] == PLAINS and (i == 0 or i == 9 or j == 0 or j == 9) and beach_count < 15:
                map[i][j] = BEACH
                beach_count += 1
                
def place_biome_plus(map, center_biome, surrounding_biome):
    # Place center_biome at a random location
    while True:
        row, col = random.randint(4, 5), random.randint(4, 5)  # Avoid edges to ensure space for surrounding_biome
        if map[row][col] == PLAINS:
            map[row][col] = center_biome
            break

    # Place surrounding_biome at the four adjacent locations
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, left, down, up
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        map[new_row][new_col] = surrounding_biome


def generate_rpg_map():
    #Generate a 10x10 RPG map with specified biomes, applying boundary checks
    rpg_map = [[PLAINS for _ in range(10)] for _ in range(10)]
    try:
        place_mountains(rpg_map)
        place_beaches(rpg_map)
        place_biome_plus(rpg_map, ELD_ALTAR, ELD_TOWN)
        place_biome(rpg_map, FOREST, count=40)
        place_biome(rpg_map, SWAMP, count=20, near_biome=PLAINS)
        place_biome(rpg_map, VILLAGE, count=4, min_distance=3)
        place_biome(rpg_map, TOWER, count=10, near_biome=FOREST, min_distance=2)
        eld_ruin_count = 0
        while eld_ruin_count < 4:            
            eld_ruin_count += sum(row.count(ELD_RUIN) for row in rpg_map)
            place_biome(rpg_map, ELD_RUIN,near_biome=MOUNTAIN, min_distance=2)
    except Exception as e:
        print(f"An error occurred during map generation: {e}")
        return None

    return rpg_map

map = generate_rpg_map()
    
def show_map():
    try:
        for y in range(10):
            for x in range(10):
                if x == player.x and y == player.y:
                    print("⮿ ", end=" ")
                else:
                    if map[y][x] == "plains":
                        print("卩", end=" ")
                    elif map[y][x] == "forest":
                        print("千", end=" ")
                    elif map[y][x] == "beach":
                        print("乃", end=" ")
                    elif map[y][x] == "mountains":
                        print("爪", end=" ")
                    elif map[y][x] == "EldTown":
                        print("乂", end=" ")
                    elif map[y][x] == "tower":
                        print("ㄒ", end=" ")
                    elif map[y][x] == "EldRuins":
                        print("尺", end=" ")
                    elif map[y][x] == "swamp":
                        print("丂", end=" ")
                    elif map[y][x] == "village":
                        print("ᐯ ", end=" ")
                    elif map[y][x] == "EldAltar":
                        print("卂", end=" ")
            print()
        draw_line()
        print("---> ⊙  <--- Tu posición.")
        print(f"Estás en {biom[map[player.y][player.x]]['t']}.")
        draw_line()
        print("1. Leyenda del mapa.")
        print("0. Salir.")
        draw_line()
        choice = input("-> ")
        if choice == "1":
            print("Legend:")
            print("ᐯ  - Town")
            print("卩 - Plains")
            print("千 - Forest")
            print("乃 - Beach")
            print("丂 - Swamp")
            print("爪 - Mountains")
            print("ㄒ - Tower")
            print("尺 - Eldritch Ruins")
            print("乂 - Eldritch Village")
            print("卂 - Eldritch Altar")
        elif choice == "0":
            pass
    except Exception as e:
        print(f"An error occurred while showing the map: {str(e)}")

try:
    y_len = len(map)-1
    x_len = len(map[0])-1
except Exception as e:
    print(f"An error occurred while getting the map length: {str(e)}")
    
    
# Biomas
biom = { 
    "village":{
        "t": "un Pueblo tranquilo",
        "e": False
    },
    "plains":{
        "t": "las Planicies",
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
    "swamp":{
        "t": "el Pantano",
        "e": True
    },
    "mountains":{
        "t": "las Montañas",
        "e": True
    },
    "tower":{
        "t": "una Torre oscura",
        "e": True
    },
    "EldRuins":{
        "t": "las Ruinas Eldritch",
        "e": True
    },
    "eldTown":{
        "t": "el Pueblo Eldritch",
        "e": True
    },
    "EldAltar":{
        "t": "el Altar Eldritch",
        "e": False
    }
    
}

# función de tienda
# las tiendas se generarán solamente en las "villages"
# las tiendas mostrarán 3 objetos completamente aleatorios, excepto las últimas 4 armas y últimas 3 armaduras
def shop():
    try:
        clear()
        draw_line()
        print("     Bienvenido viajero")
        draw_line()
        print("1. Comprar")
        print("2. Vender")
        print("0. Salir")
        draw_line()
        choice = input("-> ")
        if choice == "1":
            clear()
            draw_line()
            type_text("     Qué deseas comprar?")
            draw_line()
            print("1. Armas")
            print("2. Armaduras")
            print("3. Pociones")
            print("0. Salir")
            draw_line()
            choice = input("-> ")
            if choice == "1":
                clear()
                draw_line()
                print("Así que quieres hacer más daño, eh?")
                draw_line()
                print("Armas:")
                for i in range(3):
                    item = random.choice(items_list[:-4])
                    print(f"{i+1}. {item}  ATK {items[item]['minAtk']}-{items[item]['maxAtk']}  ${items[item]['price']}")
                draw_line()
                print("0. Salir")
                draw_line()
                choice = input("-> ")
                if choice == "1":
                    if player.gold >= items[random.choice(items_list[:-4])]["price"]:
                        player.inventory.append(random.choice(items_list[:-4]))
                        player.gold -= items[random.choice(items_list[:-4])]["price"]
                        print(f"Has comprado {player.inventory[-1]}.")
                    else:
                        print("No tienes suficiente oro.")
                elif choice == "2":
                    if player.gold >= items[random.choice(items_list[:-4])]["price"]:
                        player.inventory.append(random.choice(items_list[:-4]))
                        player.gold -= items[random.choice(items_list[:-4])]["price"]
                        print(f"Has comprado {player.inventory[-1]}.")
                    else:
                        print("No tienes suficiente oro.")
                elif choice == "3":
                    if player.gold >= items[random.choice(items_list[:-4])]["price"]:
                        player.inventory.append(random.choice(items_list[:-4]))
                        player.gold -= items[random.choice(items_list[:-4])]["price"]
                        print(f"Has comprado {player.inventory[-1]}.")
                    else:
                        print("No tienes suficiente oro.")
                elif choice == "0":
                    pass
            elif choice == "2":
                clear()
                draw_line()
                print("La defensa es la mejor arma, o no?")
                draw_line()
                print("Armaduras:")
                for i in range(3):
                    item = random.choice(items_list[-4:])
                    print(f"{i+1}. {item}  DEF {items[item]['def']}  ${items[item]['price']}")
                draw_line()
                print("0. Salir")
                draw_line()
                choice = input("-> ")
                if choice == "1":
                    if player.gold >= items[random.choice(items_list[-4:])]["price"]:
                        player.inventory.append(random.choice(items_list[-4:]))
                        player.gold -= items[random.choice(items_list[-4:])]["price"]
                        print(f"Has comprado {player.inventory[-1]}.")
                    else:
                        print("No tienes suficiente oro.")
                elif choice == "2":
                    if player.gold >= items[random.choice(items_list[-4:])]["price"]:
                        player.inventory.append(random.choice(items_list[-4:]))
                        player.gold -= items[random.choice(items_list[-4:])]["price"]
                        print(f"Has comprado {player.inventory[-1]}.")
                    else:
                        print("No tienes suficiente oro.")
                elif choice == "3":
                    if player.gold >= items[random.choice(items_list[-4:])]["price"]:
                        player.inventory.append(random.choice(items_list[-4:]))
                        player.gold -= items[random.choice(items_list[-4:])]["price"]
                        print(f"Has comprado {player.inventory[-1]}.")
                    else:
                        print("No tienes suficiente oro.")
                elif choice == "0":
                    pass
            elif choice == "3":
                if player.gold >= 77:
                    player.potions += 1
                    player.gold -= 77
                    print("Has comprado una poción.")
                else:
                    print("No tienes suficiente oro.")
            elif choice == "0":
                pass
        elif choice == "2":
            clear()
            draw_line()
            print("Déjame ver que tienes...")
            draw_line()
            print("Inventario:")
            for item in player.inventory:
                print(f"- {item}")
            draw_line()
            print("0. Salir")
            draw_line()
            choice = input("-> ")
            if choice == "1":
                if player.inventory:
                    player.gold += items[player.inventory[-1]]["price"]
                    print(f"Has vendido {player.inventory[-1]} por {items[player.inventory[-1]]['price']} monedas de oro.")
                    player.inventory.pop()
                else:
                    print("No tienes nada que vender.")
            elif choice == "0":
                pass
        elif choice == "0":
            pass
    except Exception as e:
        print(f"An error occurred while shopping: {str(e)}")
        input("-> Press Enter <-")
        clear()


try:
    current_tile = map[0][0]
    name_of_tile = biom[current_tile]["t"]
    ememy_tile = biom[current_tile]["e"]
except Exception as e:
    print(f"An error occurred while getting the current tile: {str(e)}")

############################################## Enemigos ################################################

# Lista de enemigos
enemy_list = [
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
        "health": 70,
        "attack": 8,
        "defense": 5,
        "gold": 15,
        "experience": 20,
        "weapon": "Garrote Astillado",
        "armor": "Túnica Desgarrada",
        "drop_rate": 0.1,
        "speed": 6
        },
    "Bestia poseída": {
        "health": 80,
        "attack": 9,
        "defense": 2,
        "gold": 10,
        "experience": 25,
        "weapon": "Garras Eldritch",
        "armor": "Armadura de Cuero",
        "drop_rate": 0.2,
        "speed": 10
    },
    "Espectro": {
        "health": 50,
        "attack": 5,
        "defense": 10,
        "gold": 5,
        "experience": 30,
        "weapon": "Susurro Fantasmal",
        "armor": "nothing",
        "drop_rate": 0.2,
        "speed": 8
    },
    "Cultista": {
        "health": 100,
        "attack": 8,
        "defense": 5,
        "gold": 50,
        "experience": 50,
        "weapon": "Daga de Cultista",
        "armor": "Túnica Desgarrada",
        "drop_rate": 0.1,
        "speed": 7
    },
    "Gárgola de Eldritch": {
        "health": 130,
        "attack": 5,
        "defense": 10,
        "gold": 80,
        "experience": 70,
        "weapon": "Lanza de Piedra",
        "armor": "Escamas Abisales",
        "drop_rate": 0.1,
        "speed": 10
    },
    "Horror abisal": {
        "health": 188,
        "attack": 14,
        "defense": 5,
        "gold": 100,
        "experience": 100,
        "weapon": "Susurro Fantasmal",
        "armor": "Escamas Abisales",
        "drop_rate": 0.1,
        "speed": 2
    },
    "Pesadilla viviente": {
        "health": 200,
        "attack": 10,
        "defense": 8,
        "gold": 120,
        "experience": 120,
        "weapon": "Garras de Kruegger",
        "armor": "Sueter a Rayas",
        "drop_rate": 0.1,
        "speed": 13
    },
    "Sombra de la locura": {
        "health": 20,
        "attack": 15,
        "defense": 15,
        "gold": 15,
        "experience": 18,
        "weapon": "Susurro Fantasmal",
        "armor": "Túnica Desgarrada",
        "drop_rate": 0.2,
        "speed": 15
    },
    "Cultista poseído": {
        "health": 200,
        "attack": 13,
        "defense": 10,
        "gold": 200,
        "experience": 200,
        "weapon": "Daga de Cultista",
        "armor": "Vestiduras del Ritual Prohibido",
        "drop_rate": 0.2,
        "speed": 10
    },
    "Acólito del Vacío": {
        "health": 200,
        "attack": 10,
        "defense": 13,
        "gold": 200,
        "experience": 200,
        "weapon": "Susurro Fantasmal",
        "armor": "Vestiduras del Ritual Prohibido",
        "drop_rate": 0.2,
        "speed": 10
    },
    "Médium Corrompido": {
        "health": 250,
        "attack": 13,
        "defense": 13,
        "gold": 300,
        "experience": 250,
        "weapon": "Muñeco Vuudú",
        "armor": "Vestimentas de la Locura",
        "drop_rate": 0.1,
        "speed": 13
    },
    "Paladín Caído": {
        "health": 300,
        "attack": 7,
        "defense": 15,
        "gold": 300,
        "experience": 300,
        "weapon": "Espada Caída",
        "armor": "Coraza del Paladín Caído",
        "drop_rate": 0.3,
        "speed": 10
    },
    "Guardián de la Tumba": {
        "health": 325,
        "attack": 14,
        "defense": 10,
        "gold": 350,
        "experience": 325,
        "weapon": "Espada Caída",
        "armor": "Escamas Abisales",
        "drop_rate": 0.2,
        "speed": 12
    },
    "Cazador de Mentes": {
        "health": 250,
        "attack": 15,
        "defense": 5,
        "gold": 300,
        "experience": 350,
        "weapon": "Ballesta Maldita",
        "armor": "Loriga del Cazador de Mentes",
        "drop_rate": 0.1,
        "speed": 15
    },
    "Abominación de las Ruinas": {
        "health": 400,
        "attack": 15,
        "defense": 12,
        "gold": 400,
        "experience": 400,
        "weapon": "Espada Caída",
        "armor": "Vestimentas Etéreas",
        "drop_rate": 0.2,
        "speed": 10
    },
    "Avatar de la Desesperación": {
        "health": 200,
        "attack": 20,
        "defense": 15,
        "gold": 450,
        "experience": 400,
        "weapon": "Espada de Mil Gritos",
        "armor": "Vestimentas de la Locura",
        "drop_rate": 0.2,
        "speed": 15
    },
    "Devorador de Almas": {
        "health": 300,
        "attack": 18,
        "defense": 18,
        "gold": 450,
        "experience": 450,
        "weapon": "Hacla del Cataclismo",
        "armor": "Túnica Desgarrada",
        "drop_rate": 0.2,
        "speed": 15
    },
    "Titán de los Antiguos": {
        "health": 400,
        "attack": 15,
        "defense": 20,
        "gold": 450,
        "experience": 450,
        "weapon": "Maza del Núcleo Abisal",
        "armor": "Coraza del Abismo Sin Estrellas",
        "drop_rate": 0.2,
        "speed": 15
    },
    "Engendro del Caos": {
        "health": 450,
        "attack": 20,
        "defense": 20,
        "gold": 500,
        "experience": 500,
        "weapon": "Dagas Gemelas del Caos", 
        "armor": "Vestimentas de la Locura",
        "drop_rate": 0.3,
        "speed": 18
    },
    "Emisario del Horizonte Estelar": {
        "health": 750,
        "attack": 25,
        "defense": 20,
        "gold": 750,
        "experience": 750,
        "weapon": "Alabarada de Elyssium",
        "armor": "Armadura de Elyssium",
        "drop_rate": 0.5,
        "speed": 18
    },
    # Jefe Final
    "Heredero de los Antiguos": {
        "health": 1000,
        "attack": 30,
        "defense": 20,
        "gold": 1000,
        "experience": 1000,
        "weapon": "Espada de los Antiguos",
        "armor": "Túnica de los Antiguos",
        "drop_rate": 0.5,
        "boss": True,
        "speed": 20
    },
    "ninguno": {
        "health": 0,
        "attack": 0,
        "defense": 0,
        "gold": 0,
        "experience": 0,
        "weapon": "nothing",
        "armor": "nothing",
        "drop_rate": 0,
        "speed": 0,
        "boss": False
    }
        
}

# función para pelear contra el Emisario del Horizonte Estelar (Semi Jefe final)
# el Emisario del Horizonte Estelar es el enemigo más fuerte del juego, y es el penúltimo enemigo
# Aparecerá solamente en las "Eldritch Ruins"
# Aparecerá 1 sola vez por cada "Eldritch Ruins" que se visite
# Al derrotarlo soltará una llave que permitirá abrir la puerta que lleva al Jefe Final

# Pesos de los biomas para determinar la probabilidad de encontrar un enemigo
#                       Sujet-Besti-Espec-Culti-Gargo-Horro-Pesad-Sombra-Culti-Acol-Medium-Palad-Guard-Cazad-Abomi-Avata-Devor-Titan-Engen-Emisa-Jefe-Nada
village_weight =        [0.20, 0.10, 0.05, 0.10, 0.00, 0.00, 0.00, 0.01, 0.10, 0.10, 0.05, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.30]
plains_weight =         [0.38, 0.20, 0.10, 0.10, 0.00, 0.00, 0.00, 0.02, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.20] # YES
forest_weight =         [0.10, 0.30, 0.20, 0.15, 0.00, 0.00, 0.00, 0.03, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.22] # YES
beach_weight =          [0.00, 0.00, 0.00, 0.05, 0.00, 0.30, 0.20, 0.05, 0.05, 0.00, 0.10, 0.00, 0.00, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.20] # YES
swamp_weight =          [0.00, 0.00, 0.00, 0.00, 0.00, 0.15, 0.05, 0.08, 0.00, 0.00, 0.20, 0.00, 0.05, 0.10, 0.10, 0.05, 0.00, 0.00, 0.00, 0.00, 0.00, 0.22] # YES
mountains_weight =      [0.00, 0.00, 0.00, 0.00, 0.15, 0.00, 0.00, 0.10, 0.10, 0.10, 0.00, 0.00, 0.00, 0.25, 0.10, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.20] # YES
tower_weight =          [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.10, 0.10, 0.05, 0.10, 0.00, 0.20, 0.20, 0.10, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.15] # YES
eld_ruins_weight_befo = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00] # before Emissary
eld_ruins_weight_aftr = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.10, 0.05, 0.00, 0.05, 0.00, 0.00, 0.05, 0.25, 0.10, 0.15, 0.00, 0.00, 0.00, 0.00, 0.25] # after Emissary
eldritch_town_weight =  [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.05, 0.05, 0.00, 0.00, 0.20, 0.20, 0.20, 0.30, 0.00, 0.00, 0.20] # YES
eldritch_altar_weight = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.20, 0.00, 0.80]
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

txt_intro2 = """Despiertas en un pueblo desconocido,
sin recuerdos de tu pasado.

Deberías investigar un poco
antes de aventurarte en el mundo..."""


#################################################################
######################### Funciones #############################
#################################################################


# Guardar
def save(player):
    global map
    data = [player.name, 
            player.health, 
            player.attack, 
            player.defense,
            player.speed, 
            player.gold, 
            player.level, 
            player.experience,
            player.x,
            player.y,
            player.potions,
            player.inventory,
            player.equipment,
            player.experience_needed,
            player.standing,
            player.keys,
            player.defeated_emissary_coords,
            map
            ]
    
    try:
        with open(f"{player.name}_save.txt", "w") as f:
            for item in data:
                f.write(str(item) + "\n")
    except Exception as e:
        print(f"Error saving data: {e}")

# Cargar
def load():
    global menu, play, player, map
    try:
        save_files = [file.replace("_save.txt", "") for file in os.listdir() if file.endswith("_save.txt")]
        if len(save_files) == 0:
            print("No se encontraron partidas guardadas.")
            input("Presiona enter para continuar...")
            menu = True
            play = False
            return
        draw_line()
        print("      Partidas guardadas")
        draw_line()
        for i, file in enumerate(save_files):
            print(f"{i+1}. {file}")
        draw_line()
        choice = input("Escriba el número del personaje\n-> ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(save_files):
            print("Opción inválida.")
            input("Presiona enter para continuar...")
            menu = True
            play = False
            return
        name = save_files[int(choice)-1]
        with open(f"{name}_save.txt", "r") as f:
            lines = f.readlines()
            name = lines[0].replace("\n", "")
            health = int(lines[1])
            attack = int(lines[2])
            defense = int(lines[3])
            speed = int(lines[4])
            gold = int(lines[5])
            level = int(lines[6])
            experience = int(lines[7])
            x = int(lines[8])
            y = int(lines[9])
            potions = int(lines[10])
            inventory = [item.strip("[]'") for item in lines[11].strip().split(', ')]
            equipment = [item.strip("[]'") for item in lines[12].strip().split(', ')]
            experience_needed = int(lines[13])
            player.standing = bool(lines[14].strip())
            player.keys = int(lines[15])
            player.defeated_emissary_coords = [eval(coord) for coord in lines[16].strip().split(', ')]
            
            print(map)
            draw_line()
            print("Cargando juego...")
            time.sleep(2)
            print("Juego cargado!")
            time.sleep(1)
            print("Estos son tus datos: ")
            time.sleep(1)
            draw_line()
            player = Character(name, health, attack, defense, speed, gold, level, experience, x, y, potions, inventory, equipment, experience_needed)                    
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
        print("Chanfle, ocurrió un error al cargar la partida.")
        print(f"({e})")
        input("Presiona enter para continuar...")
        menu = True
        play = False
    
# Limpiar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dibujar línea
def draw_tabed_big_line():
    print("\t~+X-------------------------------------------------------X+~")
def draw_big_line():
    print("~+X-------------------------------------------------------X+~")
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
    
    
# función para mostrar introducción y título del juego
def intro_and_title():
    clear()
    draw_big_line()
    type_text(txt_intro2, 0.01)
    draw_big_line()
    time.sleep(1)
    input("\n\t\t\t   -> Press Enter <-")
    clear()
    return

def get_village_coordinates():
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile == "village":
                return x, y
    return 0, 0

def get_eldritch_ruins_coordinates():
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile == "eldritch_ruins":
                return x, y
    return 0, 0

def check_if_emissary_is_defeated_in_this_coords():
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile == "eldritch_ruins":
                return x, y
    return 0, 0

def fight_emissary():
    try:
        clear()
        type_text("Una misteriosa figura humanoide se alza frente a ti.", 0.04)
        time.sleep(0.5)
        type_text("Se te revela como el Emisario de los Señores Antiguos.", 0.04)
        time.sleep(0.5)
        type_text("Su presencia es abrumadora, y sientes que la realidad misma se retuerce a su alrededor.", 0.04)
        time.sleep(0.5)
        type_text("Estás seguro de que quieres enfrentarte a él?", 0.04)
        time.sleep(1)
        print("\n1. Sí\n0. No")
        draw_line()
        time.sleep(1)
        choice = input("-> ")
        if choice == "1" or choice.lower() == "si" or choice.lower() == "yes":
            clear()
            type_text("Que así sea.",0.02)
            clear()
            time.sleep(2)
            enemy = Enemy("Emisario del Horizonte Estelar")
            battle_v2(enemy)
            if player.health > 0:
                clear()
                type_text("El Emisario deja caer un misterioso orbe", 0.05)
                type_text("Al recogerlo sientes estar más cerca de tu destino...", 0.05)
                type_text("Parece poder insertarse en algún sitio...\n", 0.05)
                input("-> Press Enter <-")
                # añade esta coordenada a la lista de coordenadas donde se ha derrotado al Emisario
                player.keys += 1
                coords = check_if_emissary_is_defeated_in_this_coords()
                player.defeated_emissary_coords.append(coords)
                player.standing = True
                clear()
        elif choice == "0" or choice.lower() == "no":
            type_text("Quizás sea mejor preparase antes...", 0.05)
            pass
    except Exception as e:
        print(f"An error occurred while fighting the Emissary: {str(e)}")
        input("-> Press Enter <-")
        clear()

# función que maneja el inicio de un juego nuevo
def new_game():
    global menu, play, player
    # creamos un nuevo mapa para esta partida:
    global map
    map = generate_rpg_map()
    # Asignamos player.x y player.y a una village
    player.x, player.y = get_village_coordinates()
    #type_text("Escuchas una voz en lo profundo de tu mente...\n", 0.03)
    #type_text("\t R e c u e r d a  t u  n o m b r e .", 0.08)
    while True:
        player.name = input("\n-> ")
        if len(player.name) >= 2:
            break
        else:
            print("El nombre debe tener al menos 2 caracteres.\n")
            draw_line()
    #clear()
    #type_text(f"Cierto... Me llamo {player.name}", 0.05)
    #time.sleep(1)
    #type_text("...verdad?", 0.1)
    #time.sleep(2)
    #input("\n\n-> Press Enter <-\n")
    #clear()
    #intro_and_title()
    clear()
    menu = False
    play = True
    return

# función que maneja el menú principal
def main_menu():
    global menu, rules, credits
    try:
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
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            main_menu()
    except Exception as e:
        print("Ha ocurrido un error:", str(e))
        main_menu()
        
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
    
    
def investigar_enemigo():
    global enemy
    draw_big_line()
    print(f"Nombre: {enemy.name}")
    print(f"HP:     {enemy.health}/{enemy.max_health}")
    print(f"ATK:    {enemy.attack}")
    print(f"DEF:    {enemy.defense}")
    print(f"SPD:    {enemy.speed}")
    print(f"WEAPON: {enemy.weapon}")
    print(f"ARMOR:  {enemy.armor}")
    print(f"EXP:    {enemy.experience}")
    print(f"Oro:    {enemy.gold}")
    draw_big_line()
    input("\n-> Press Enter <-\n")
    clear()
    return
# Batalla aleatoria según el bioma
def random_battle():
    global player, play, enemy
    # Batalla random
    if not player.standing:
        if biom[map[player.y][player.x]]["e"]:
            clear()
            # Si hay enemigos en el bioma PLANICIE
            if current_tile == "plains":
                enemy_name = random.choices(enemy_list, weights=plains_weight, k=1)[0]
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
                enemy_name = random.choices(enemy_list, weights=forest_weight, k=1)[0]
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
                enemy_name = random.choices(enemy_list, weights=beach_weight, k=1)[0]
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
                enemy_name = random.choices(enemy_list, weights=mountains_weight, k=1)[0]
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
                                        
            # Si hay enemigos en el bioma PUEBLO MALDITO
            elif current_tile == "EldTown":
                enemy_name = random.choices(enemy_list, weights=eldritch_town_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} en el pueblo Eldritch!")
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
            elif current_tile == "tower":
                enemy_name = random.choices(enemy_list, weights=tower_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con un {enemy_name} la torre oscura!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_big_line()
                    print("La oscuridad de la torre te llena por dentro...")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    clear()
                    player.standing = True
                    play = True
                    
            elif current_tile == "EldRuins":
                enemy_name = random.choices(enemy_list, weights=eld_ruins_weight_befo, k=1)[0]
                if enemy_name != "ninguno":
                    if enemy_name == "Emisario del Horizonte Estelar":
                        if (player.x, player.y) in player.defeated_emissary_coords:
                            enemy_name = random.choices(enemy_list, weights=eld_ruins_weight_aftr, k=1)[0]
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
                        else:
                            fight_emissary()
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
                enemy_name = random.choices(enemy_list, weights=swamp_weight, k=1)[0]
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
            # Si tiene las 4 llaves aparecerá el jefe en EldAltar:
            if player.inventory.count("Llave") == 4:
                enemy_name = random.choices(enemy_list, weights=eldritch_altar_weight, k=1)[0]
                if enemy_name != "ninguno":
                    enemy = Enemy(enemy_name)
                    draw_big_line()
                    print(f"¡Te has encontrado con el jefe final en el altar eldritch!")
                    draw_big_line()
                    input("\n-> Press Enter <-\n")
                    battle_v2(enemy_name)
                else:
                    draw_line()
                    print("El altar eldritch te hace sentir pequeño...")
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
        
def battle_v2(enemy_name):
    global menu, player, play
    global enemy
    enemy = Enemy(enemy_name)
    # nivelamos al enemigo al nivel del jugador
    enemy.level_up()
    clear()
    while player.health > 0 and enemy.health > 0:
        try:
            draw_line()
            print(f"{player.name}: {player.health}/{player.max_health}")
            print(f"{enemy_name}: {enemy.health}/{enemy.max_health}")
            draw_line()
            print("1.- Ataque fuerte")
            print("2.- Ataque rápido")
            print("3.- Usar poción")
            print("4.- Investigar")
            print("0.- Huir")
            draw_line()
            option = input("-> ")
            draw_line()
            if option == "1":
                # Ataque del jugador
                if player.speed >= enemy.speed or random.random() < 0.7:  # 70% de probabilidad de acertar
                    damage = player.calculate_damage() * 2 - enemy.total_defense()
                    if damage < 0:
                        damage = 0
                    enemy.health -= damage
                    print(f"¡Le has quitado {damage} de salud al {enemy_name}!")
                    time.sleep(2)
                    if enemy.health <= 0:
                        break
                else:
                    print("¡Has fallado el ataque!")
                    time.sleep(2)
                # Ataque del enemigo
                if enemy.speed > player.speed or random.random() < 0.7:  # 70% de probabilidad de ataque rápido
                    damage = enemy.calculate_damage() - player.total_defense()
                else:
                    damage = enemy.calculate_damage() * 2 - player.total_defense()
                if damage < 0:
                    damage = 0
                player.health -= damage
                print(f"¡El {enemy_name} te ha quitado {damage} de salud!")
                time.sleep(2)
                clear()
            elif option == "2":
                # Ataque del jugador
                if player.speed >= enemy.speed or random.random() < 0.9:  # 90% de probabilidad de acertar
                    damage = player.calculate_damage() - enemy.total_defense()
                    if damage < 0:
                        damage = 0
                    enemy.health -= damage
                    print(f"¡Le has quitado {damage} de salud al {enemy_name}!")
                    time.sleep(2)
                    if enemy.health <= 0:
                        break
                else:
                    print("¡Has fallado el ataque!")
                    time.sleep(2)
                # Ataque del enemigo
                if enemy.speed > player.speed or random.random() < 0.5:  # 50% de probabilidad de ataque rápido
                    damage = enemy.calculate_damage() - player.total_defense()
                else:
                    damage = enemy.calculate_damage() * 2 - player.total_defense()
                if damage < 0:
                    damage = 0
                player.health -= damage
                print(f"¡El {enemy_name} te ha quitado {damage} de salud!")
                time.sleep(2)
                clear()
            elif option == "3":
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
            elif option == "4":
                investigar_enemigo()
            elif option == "0":
                if random.randint(1, 100) <= 70:
                    clear()
                    draw_line()
                    print("Has conseguido huir...")
                    draw_line()
                    clear()
                    play = True
                    break
                else:
                    clear()
                    type_text("\tN O  E S C A P A R A S\n", 0.05)
                    if random.random() < 0.7:  # 70% de probabilidad de ataque rápido
                        damage = enemy.calculate_damage() - player.total_defense()
                    else:
                        damage = enemy.calculate_damage() * 2 - player.total_defense()
                    if damage < 0:
                        damage = 0
                    player.health -= damage
                    print(f"¡El {enemy_name} te ha quitado {damage} de salud!")
                    time.sleep(2)
                    clear()

                    time.sleep(1)
                    clear()
                    pass
            else:
                print("Opción no válida")
                input("-> Press Enter <-")
                clear()
        except Exception as e:
            print(f"Error: {e}")
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
        main_menu()
    elif enemy.health <= 0:
        print(f"¡Has derrotado al {enemy_name}!")
        time.sleep(1)
        print(f"Has ganado {enemy.gold} de oro y {enemy.experience} de experiencia.")
        player.gold += enemy.gold
        player.experience += enemy.experience
        try:
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
            while player.experience >= player.experience_needed:
                time.sleep(2)
                player.level_up()
                play = True
            else:
                time.sleep(2)
                clear()
                play = True
        except Exception as e:
            print(f"Error: {e}")
            input("-> Press Enter <-")
            clear()

# función de play
def play_game():
    global play, menu, rules, credits, player, autosave
    try:
        save(player) # autosave
        player.standing = True
        draw_line()
        print("    Estás en " + biom[map[player.y][player.x]]["t"])
        draw_line()
        print(f"HP:{player.health}/{player.max_health} Lvl:{player.level}  Exp:{player.experience}/{player.experience_needed}")
        draw_line()
        print("1.- Moverse")
        print("2.- Reflexionar")
        print("3.- Mostrar inventario")
        if biom[map[player.y][player.x]]["t"] == "village":
            print("T.- Tienda")
        print("9.- Mostrar reglas")
        print("0.- Guardar y salir")
        draw_line()
        option = input("-> ")
        if option == "1":
            clear()
            player.move()
            play = True
        elif option == "2":
            #reflexionar() AÑADIIIIIIIIIIIR
            print("reflexionar")
            input("-> Press Enter <-")
            clear()
            play = True
        elif option == "3":
            clear()
            player.show_inventory()
            player.standing = True
            clear()
            play = True
        elif option == "t".lower() and biom[map[player.y][player.x]]["t"] == "village":
            shop()
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
    except Exception as e:
        print("Error:", str(e))
        time.sleep(1)
        clear()
        play = True

#################################################################
##################### Programa principal ########################
#################################################################
type_text_line(title, 0.1)
input("\n\t\t\t-> Press Enter <-")
clear()

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