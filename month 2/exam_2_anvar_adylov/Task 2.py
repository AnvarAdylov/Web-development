import random as rnd
def damage_calculation(attacker, defender):
    damage = defender['defence'] - attacker['str'] - attacker['weapon']
    if damage > 0:
        damage = 0
    return damage
def display_damage(defender, attacker, damage):
    if damage < 0:
        print(attacker['name'] + " нанес %i ед. урона противнику " % (damage*(-1)) + defender['name'] )
    else:
        print(attacker['name'] + " нанес 0 ед. урона противнику " + defender['name'])
def display_dragon_info():
    print('Дракон %i/%i' % (dragon['hp'],dragon['max_hp']))
def display_hero_info():
    print('Герой %i/%i' % (hero['hp'],hero['max_hp']))
def dragon_turn():
    if rnd.randint(1,100) > 50:
        print("Дракон выбрал действие 'атака'")
        if hit_confirmation(dragon) == 1:
            damage_total = damage_calculation(dragon, hero)
            modify_health(hero,damage_total)  
            display_damage(hero,dragon, damage_total) 
        else:
            print("Промах!")
    else: 
        print("Дракон заснул")
def game():
    turn_number = 0
    while True:
        turn_number = turn_number + 1
        print("==================================================\n")
        turn_string = "Ход %i" %turn_number
        print(turn_string.center(50))
        print("==================================================\n")
        hero_turn()
        
        if dragon['hp'] == 0:
            print("Поздравляем! Дракон побежден героем")
            break
        dragon_turn()
        if hero['hp'] == 0:
            print("Game over! Дракон сьел героя")
            break

        display_hero_info()
        display_dragon_info()
def hit_confirmation(entity):
    hit_chance = entity['accuracy']
    chance = 100 - int(hit_chance*100)
    random_roll = rnd.randint(1,100)
    if chance >= random_roll:
        return 0
    else:
        return 1
def hero_turn():
    print("Герой выбрал действие 'атака'")
    if hit_confirmation(hero) == 1:
        damage_total = damage_calculation(hero,dragon)
        modify_health(dragon,damage_total)  
        display_damage(dragon,hero,damage_total) 
    else:
        print("Промах!")
def modify_health(entity, damage):
    if damage < 0:
        entity['hp'] = entity['hp'] + damage
        if entity['hp'] < 0: 
            entity['hp'] = 0
dragon = {
'name': "Дракон",    
'hp': 2000, # жизненная энергия, запас здоровья текущая
'max_hp': 2000, # жизненная энергия, запас здоровья максимальная
'defence': 120, # защита 
'str': 150, # сила
'weapon': 0, # оружие
'accuracy': 1.00 #точность
}
hero = {
'name': "Герой",    
'hp': 1000,
'max_hp': 1000,
'defence': 100,
'str': 120,
'weapon': 250,
'shield': 150, # щит
'accuracy' : 0.75
}
game()

