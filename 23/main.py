

def solve(lines, initial_a):
    
    reg = {}
    reg['a'] = initial_a
    reg['b'] = 0
    ic = 0
    while ic != len(lines):
        line = lines[ic]
        tokens = line.split(' ')
        
        if tokens[0] == "hlf":
            reg[tokens[1]] /= 2
        
        elif tokens[0] == "tpl":
            reg[tokens[1]] *= 3
            
        elif tokens[0] == "inc":
            reg[tokens[1]] += 1
            
        elif tokens[0] == "jmp":
            ic += int(tokens[1])
            continue
            
        elif tokens[0] == "jie":
            reg_name = tokens[1].strip(',')
            if reg[reg_name] % 2 == 0:
                ic += int(tokens[2])
                continue
        
        elif tokens[0] == "jio":
            reg_name = tokens[1].strip(',')
            if reg[reg_name] == 1:
                ic += int(tokens[2])
                continue
                
        ic += 1
        
    return reg['b']
    
    
lines = open('input.txt', 'r').read().strip().split('\n')
print solve("inc a\njio a, +2\ntpl a\ninc a".split("\n"), 0)  # 0
print solve(lines, 0)
print solve(lines, 1)