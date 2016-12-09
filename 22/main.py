import heapq

def solve(initial_boss_hp, boss_damage, initial_hp, initial_mana, penalty = 0):

    heap = []
    visited = {}
    
    heapq.heappush(heap, (0, initial_boss_hp, initial_hp, initial_mana, [0,0,0], []))  # (shield, poison, recharge)
    
    while len(heap) > 0:
    
        total_mana, boss_hp, hp, mana, effects, logs = heapq.heappop(heap)
        log = "Total mana: {0}\nBoss hp: {1}\nHP: {2}\nMana: {3}\nEffects: {4}-{5}-{6}\n\n".format(total_mana, boss_hp, hp, mana, effects[0], effects[1], effects[2])
        logs.append(log)
        
        key = (total_mana, boss_hp, hp, mana, effects[0], effects[1], effects[2])
        if key in visited:
            continue
        visited[key] = True
        
        initial_turn = total_mana == 0
        if not initial_turn:
            hp -= penalty
            if hp <= 0:
                continue
        
        if effects[1] > 0:
            boss_hp -= 3
            effects[1] -= 1
                        
        if boss_hp <= 0:
            print "\n".join(logs)
            return total_mana
            
        if effects[2] > 0:
            mana += 101
            effects[2] -= 1
                
        if mana < 53 and effects[2] == 0:
            continue
        
        if not initial_turn:
            damage = boss_damage if effects[0] == 0 else max(boss_damage - 7, 1)
            hp -= damage
            
        if hp <= 0:
            continue
            
        if effects[1] > 0:
            boss_hp -= 3
            effects[1] -= 1
                        
        if boss_hp <= 0:
            print "\n".join(logs)
            return total_mana
        
        if effects[0] > 0:
            effects[0] -= 2
            
        if effects[2] > 0:
            mana += 101
            effects[2] -= 1
            
        # Magic missile
        cost = 53
        if mana >= cost:
            heapq.heappush(heap, (total_mana + cost, boss_hp - 4, hp, mana - cost, effects[:], logs[:]))
        
        # Drain
        cost = 73
        if mana >= cost:
            heapq.heappush(heap, (total_mana + cost, boss_hp - 2, hp + 2, mana - cost, effects[:], logs[:]))
        
        # Shield
        cost = 113
        if effects[0] == 0 and mana >= cost:
            new_effects = effects[:]
            new_effects[0] = 6
            heapq.heappush(heap, (total_mana + cost, boss_hp, hp, mana - cost, new_effects, logs[:]))
        
        # Poison
        cost = 173
        if effects[1] == 0 and mana >= cost:
            new_effects = effects[:]
            new_effects[1] = 6
            heapq.heappush(heap, (total_mana + cost, boss_hp, hp, mana - cost, new_effects, logs[:]))
        
        # Recharge
        cost = 229
        if effects[2] == 0 and mana >= cost:
            new_effects = effects[:]
            new_effects[2] = 5
            heapq.heappush(heap, (total_mana + cost, boss_hp, hp, mana - cost, new_effects, logs[:]))
           
           
    return -1
    
lines = open('input.txt', 'r').read().strip().split('\n')
boss_hp = int(lines[0].split(": ")[1])
boss_damage = int(lines[1].split(": ")[1])
    
print "######### {0} ########".format(solve(13, 8, 10, 250))
print "######### {0} ########".format(solve(14, 8, 10, 250))
print "######### {0} ########".format(solve(boss_hp, boss_damage, 50, 500))
print "######### {0} ########".format(solve(boss_hp, boss_damage, 50, 500, 1))
        
                