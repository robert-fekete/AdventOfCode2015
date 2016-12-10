import heapq

def solve(initial_boss_hp, boss_damage, initial_hp, initial_mana, penalty = 0):

    spells = [
        (53, 4, 0, None, 0),  # Magic missile
        (73, 2, 2, None, 0),  # Drain
        (113, 0, 0, 0, 6),    # Shield
        (173, 0, 0, 1, 6),    # Poison
        (229, 0, 0, 2, 5)     # Recharge
    ]
    heap = []
    visited = {}
    
    heapq.heappush(heap, (0, initial_boss_hp, initial_hp, initial_mana, [0,0,0]))  # (shield, poison, recharge)
    
    while len(heap) > 0:
    
        total_mana, boss_hp, hp, mana, effects = heapq.heappop(heap)
        
        key = (total_mana, boss_hp, hp, mana, effects[0], effects[1], effects[2])
        if key in visited:
            continue
        visited[key] = True
        
        # Boss' turn
        initial_turn = total_mana == 0
        if not initial_turn:
        
            if effects[1] > 0:
                boss_hp -= 3
                effects[1] -= 1
                            
            if boss_hp <= 0:
                return total_mana
                
            if effects[2] > 0:
                mana += 101
                effects[2] -= 1
                    
            damage = boss_damage if effects[0] == 0 else max(boss_damage - 7, 1)
            hp -= damage
            
            if hp <= 0:
                continue
                
            hp -= penalty
            if hp <= 0:
                continue
            
        if effects[1] > 0:
            boss_hp -= 3
            effects[1] -= 1
                        
        if boss_hp <= 0:
            return total_mana
        
        if effects[0] > 0:
            effects[0] -= 2
            
        if effects[2] > 0:
            mana += 101
            effects[2] -= 1
            
        if mana < 53 and effects[2] == 0:
            continue
            
            
        for spell in spells:
            cost, damage, healing, effect, timer = spell
            new_effects = effects[:]
            
            if effect is not None:
                if new_effects[effect] == 0:
                    new_effects[effect] = timer
                else:
                    continue
                    
            if mana >= cost:
                heapq.heappush(heap, (total_mana + cost, boss_hp - damage, hp + healing, mana - cost, new_effects))
           
    return -1
    
lines = open('input.txt', 'r').read().strip().split('\n')
boss_hp = int(lines[0].split(": ")[1])
boss_damage = int(lines[1].split(": ")[1])
    
print solve(13, 8, 10, 250)
print solve(14, 8, 10, 250)
print solve(boss_hp, boss_damage, 50, 500)
print solve(boss_hp, boss_damage, 50, 500, 1)
