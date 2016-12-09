

def get_price(target, body_stuffs, ensure_has_body, rings, body, fingers, picker, default_value):
    
    if target == 0:
        return 0
    
    picked_price = default_value
    if len(body) == 0:
        for piece in body_stuffs:
            if piece[0] <= target:
                price = piece[1] + get_price(target - piece[0], [], ensure_has_body, rings, [piece], fingers, picker, default_value)
                picked_price = picker(price, picked_price)
                
        if ensure_has_body and picked_price != 500:
            return picked_price
        
    if len(fingers) < 2:
        for piece in rings:
            if piece[0] <= target:
                price = piece[1] + get_price(target - piece[0], body_stuffs, ensure_has_body, [ring for ring in rings if ring != piece], body, fingers + [piece], picker, default_value)
                picked_price = picker(price, picked_price)
            
    return picked_price

def solve_first(boss_armor, boss_damage, boss_hp, weapons, damage_rings, armors, armor_rings):

    max_damage = 13
    max_armor = 10

    options = []
    for i in xrange(max_damage + 1):
        for j in xrange(max_armor + 1):

            player_turns = boss_hp / max(i - boss_armor, 1)
            boss_turns = 100 / max(boss_damage - j, 1)
            if player_turns <= boss_turns:
                options.append((i, j))
                break

    min_price = 500
    for option in options:
        weapon_price = get_price(option[0], weapons, True, damage_rings, [], [], min, 500)
        armor_price = get_price(option[1], armors, False, armor_rings, [], [], min, 500)
        price = weapon_price + armor_price
        if price < min_price:
            min_price = price
            
    return min_price

def solve_second(boss_armor, boss_damage, boss_hp, weapons, damage_rings, armors, armor_rings):

    max_damage = 13
    max_armor = 10

    options = {}
    for i in xrange(4, max_damage + 1):
        options[i] = -1
        for j in xrange(max_armor + 1):

            player_turns = boss_hp / max(i - boss_armor, 1)
            boss_turns = 100 / max(boss_damage - j, 1)
            if player_turns > boss_turns and options[i] < j:
                options[i] = j
                
    max_price = 0
    for o in options:
        if options[o] != -1:
            weapon_price = get_price(o, weapons, True, damage_rings, [], [], max, 0)
            armor_price = get_price(options[o], armors, False, armor_rings, [], [], max, 0)
            price = weapon_price + armor_price
            
            if price > max_price:
                max_price = price
            
    return max_price

lines = open('input.txt', 'r').read().strip().split("\n")
boss_hp = int(lines[0].split(":")[1].strip())
boss_damage = int(lines[1].split(":")[1].strip())
boss_armor = int(lines[2].split(":")[1].strip())
            
weapons = [
    (4, 8),
    (5, 10),
    (6, 25),
    (7, 40),
    (8, 74)
]
damage_rings = [
    (1, 25),
    (2, 50),
    (3, 100)
]

armors = [
    (1, 13),
    (2, 31),
    (3, 53),
    (4, 75),
    (5, 102)
]

armor_rings = [
    (1, 20),
    (2, 40),
    (3, 80)
]
    
print solve_first(boss_armor, boss_damage, boss_hp, weapons, damage_rings, armors, armor_rings)
print solve_second(boss_armor, boss_damage, boss_hp, weapons, damage_rings, armors, armor_rings)