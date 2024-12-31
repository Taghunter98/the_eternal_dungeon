import mechanics

class enemy:
    def __init__(self, name, health, damage, crit_damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.crit_damage = crit_damage
        #TODO self.attack_power = attack_power
        #TODO self.abilities = abilities
    
def attack(entity):
        roll = mechanics.dice()
        
        print(f"{entity} rolls {roll}.")
        return roll
        
def attack_amount(entity_name):
    entity = enemy_check(entity_name)
    entity_damage = attack(entity_name)
    damage = entity.damage
    crit_damage = entity.crit_damage
        
    # Check to see what type the entity is
        
    if entity_damage > 2:
        return damage
    
    elif entity_damage == 6:
        print("Critical hit!")
        return crit_damage
    else:
        print("You dodged the attack!")
        return 0
    
def enemy_check(entity):
    if entity == "Goblin":
        entity = enemy("Goblin", 30, 5, 10)
        return entity
    elif entity == "Ork":
        entity = enemy("Ork", 50, 10, 15)
        return entity
    elif entity == "Skeleton":
        entity = enemy("Skeleton", 25, 5, 15)
        return entity
    else:
        mechanics.error("Can't create enemy.")
    
