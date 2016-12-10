import re
from collections import deque


def solve_first(input_string):

    parts = [part for part in input_string.strip().split('\n') if part != ""]
    replacement_strings = parts[:-1]
    molecule = parts[-1]

    replacements = {}

    for replacement in replacement_strings:

        from_what, to_what = replacement.split(" => ")
        from_regex = re.compile(from_what)
        if from_regex not in replacements:
            replacements[from_regex] = []

        replacements[from_regex].append(to_what)

    results = set([])
    for i in xrange(len(molecule)):
        for regex in replacements:
            match = regex.match(molecule, i)
            if match is not None:
                for to in replacements[regex]:
                    results.add(molecule[:match.start(0)] + to + molecule[match.end(0):])

    return len(results)


def solve_second(input_string):

    parts = [part for part in input_string.strip().split('\n') if part != ""]
    replacement_strings = parts[:-1]
    required_molecule = parts[-1]
    Ys = len(re.findall("Y", required_molecule))
    Rns = len(re.findall("Rn", required_molecule))
    Ars = len(re.findall("Ar", required_molecule))
    
    print "numbers"
    print Ys
    print Rns
    print Ars

    replacements = {}

    for replacement in replacement_strings:

        from_what, to_what = replacement.split(" => ")
        if from_what not in replacements:
            replacements[from_what] = []

        replacements[from_what].append(to_what)
        
    queue = deque([])
    visited = []

    queue.append(('e', 0))

    max_steps = 0
    while len(queue) > 0:

        molecule, steps = queue.popleft()
        
        if max_steps < steps:
            print steps
            max_steps = steps
            print len(queue)

        
        if molecule in visited:
            continue

        visited.append(molecule)
        
        if len(molecule) > len(required_molecule):
            continue
            
            
        tYs = len(re.findall("Y", molecule))
        if tYs > Ys:
            continue
            
        tRns = len(re.findall("Rn", molecule))
        if tRns > Rns:
            continue
            
        tArs = len(re.findall("Ar", molecule))
        if tArs > Ars:
            continue
            

        mol_list = list(molecule)
        for i in xrange(len(molecule)):
            if molecule[i] in replacements:
                fromm = molecule[i]
                for to in replacements[fromm]:
                    new_molecule = mol_list[:i] + [to] + mol_list[i+1:]
                    # print molecule[:match.start(0)] + to + molecule[match.end(0):]

                    new_molecule = "".join(new_molecule)
                    if new_molecule == required_molecule:
                        return steps + 1
                    queue.append((new_molecule, steps + 1))
                    
            elif molecule[i:i+2] in replacements:
                fromm = molecule[i:i+2]
                for to in replacements[fromm]:
                    new_molecule = mol_list[:i] + list(to) + mol_list[i+2:]
                    # print molecule[:match.start(0)] + to + molecule[match.end(0):]

                    new_molecule = "".join(new_molecule)
                    if new_molecule == required_molecule:
                        return steps + 1
                    queue.append((new_molecule, steps + 1))
                

    return -1


print solve_first("H => HO\nH => OH\nO => HH\n\nHOH")  # 4
print solve_first("H => HO\nH => OH\nO => HH\n\nHOHOHO")  # 7
print solve_first("H => OO\n\nH2O")  # 1
print solve_first("Mg => WUT\n\nMgMg")  # 2
print solve_first(open(r'.\input.txt', 'r').read())

print solve_second("e => O\ne => H\nH => HO\nH => OH\nO => HH\n\nHOH")  # 3
print solve_second("e => O\ne => H\nH => HO\nH => OH\nO => HH\n\nHOHOHO")  # 6
print solve_second("e => Mg\nMg => MgMg\nMg => Ag\n\nAgAg")  # 4
print solve_second(open(r'.\input.txt', 'r').read())
