import mechanics

class enemy:
    def __init__(self, name, health, damage, crit_damage, gold):
        self.name = name
        self.health = health
        self.damage = damage
        self.crit_damage = crit_damage
        self.gold = gold
    
def attack(entity):
        roll = mechanics.dice()
        
        print(f"{entity} rolls {roll}.")
        return roll
        
def attack_amount(entity_name):
    entity = enemy_check(entity_name)
    damage = entity.damage
    crit_damage = entity.crit_damage
    
    mechanics.print_enemy_title(entity)
    entity_damage = attack(entity_name)
    mechanics.sleep(1)
        
    # Check to see what type the entity is
        
    if entity_damage > 2:
        return damage
    
    elif entity_damage == 6:
        print("\nCritical hit!")
        return crit_damage
    else:
        print("\nYou dodged the attack!")
        return 0
    
def enemy_check(entity):
    # All enemies
    enemies = {
        "Goblin": enemy("Goblin", 30, 5, 10, 25),
        "Ork": enemy("Ork", 50, 10, 15, 50),
        "Skeleton": enemy("Skeleton", 20, 5, 15, 25),
        "Troll": enemy("Troll", 100, 15, 20, 150)
    }
    if entity in enemies:
        return enemies.get(entity)
    else:
        mechanics.error("Can't create enemy.")
