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
        print(attacker['name'] + " не смог пробить защиту противника " + defender['name'])
def display_dragon_info():
    print("╔══════════════════════════════════════════╗")
    print(dragon['name'].center(40))
    print(' HP: %i/%i' % (dragon['hp'],dragon['max_hp']))
    print(' Атака: %i' % (dragon['str']))
    print(' Защита: %i' % (dragon['defence']))
    print("╚══════════════════════════════════════════╝")
def display_hero_info():
    print("╔══════════════════════════════════════════╗")
    print(hero['name'].center(40))
    print(' HP: %i/%i' % (hero['hp'],hero['max_hp']))
    print(' Атака: %i' % (hero['str']))
    print(' Защита: %i' % (hero['defence']))
    print(' Зелья: %i' % (hero['potions']))
    print("╠══════════════════════════════════════════╣")
    print(" Навыки:")
    print(" attack - атаковать противника оружием ")
    print(" defend - закрыться щитом ")
    print(" pass - пропустить ход ")
    print(" potion - выпить зелье ")
    print(' Зелье восстанавливает %i ед. здоровья' % (hero['potion_power']))
    #print(" check - показать статусное окно противника")
    print("╚══════════════════════════════════════════╝")
def dragon_turn():
    if rnd.randint(1,100) > 50:
        if hit_confirmation(dragon) == 1:
            if rnd.randint(1,100)>50:
                fireball()
            else:
                print("Дракон выбрал действие 'атака'")
                damage_total = damage_calculation(dragon, hero)
                modify_health(hero,damage_total)  
                display_damage(hero,dragon, damage_total) 
        else:
            print("Промах!")
    else: 
        print("Дракон заснул")
def equip_shield():
    if hero['has_shield'] == False:
        hero['defence'] = hero['defence'] + hero['shield']
        hero['has_shield'] = True
def fireball():
    print(dragon['name'] + " плюется огненным шаром в " + hero['name'])
    damage_total = fireball_damage()
    if hero['has_shield']:
        print(hero['name'] + " отразил огненнй шар щитом")
        modify_health(dragon,damage_total)
        display_damage(dragon,hero,damage_total) 
    else:    
        modify_health(hero,damage_total)
        display_damage(hero,dragon,damage_total) 
def fireball_damage():
    damage = - dragon['str']*2
    return damage
def game():
    turn_number = 0
    display_hero_info()
    while True:
        turn_number = turn_number + 1
        print("==================================================\n")
        turn_string = "Ход %i" %turn_number
        print(turn_string.center(50))
        print("==================================================\n")
        hero_turn()
        if dragon['hp'] == 0:
            print("Поздравляем! Дракон побежден героем")
            display_hero_info()
            display_dragon_info()
            break
        dragon_turn()
        if hero['hp'] == 0:
            print("Game over! Дракон победил героя")
            display_hero_info()
            display_dragon_info()
            break
        remove_shield()
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
def hero_attack():
    print(hero['name'] + " выбрал действие 'атака'")
    if hit_confirmation(hero) == 1:
        damage_total = damage_calculation(hero,dragon)
        modify_health(dragon,damage_total)  
        display_damage(dragon,hero,damage_total) 
    else:
        print("Промах!")
def hero_defend():
    print(hero['name'] + " выбрал действие 'Закрыться щитом'")
    equip_shield()
def hero_inaction():
    print(hero['name'] + " выбрал бездействие")
def hero_potion():
    if hero['potions'] > 0:
        print(hero['name'] + "выпил зелье и восстановил " + hero['potion_power'] + 'ед. здоровья')
        modify_health(hero,hero['potion_power'])
        hero['potions'] = hero['potions'] - 1
    else:
        print("Закончились зелья!")
def hero_turn():
    while True:
        print("Выберите действие героя:")
        command = input('> ')
        if 'attack' == command.lower():
            hero_attack()
            break
        elif 'defend' == command.lower():
            hero_defend()
            break
        elif 'pass' == command.lower():
            hero_inaction()
            break
        elif 'potion' == command.lower():
            hero_potion()
            break
        else:
            print("Невозможное действие!")
def modify_health(entity, damage):
    if damage < 0:
        entity['hp'] = entity['hp'] + damage
        if entity['hp'] < 0: 
            entity['hp'] = 0
    else:
        entity['hp'] =  entity['hp'] + damage
        if entity['hp'] > entity['max_hp']:
            entity['hp'] = entity['max_hp']
def remove_shield():
    if hero['has_shield']:
        hero['defence'] = hero['defence'] - hero['shield']
        hero['has_shield'] = False
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
'accuracy' : 0.75,
'has_shield': False,
'potions':1,
'potion_power':500
}
game()


