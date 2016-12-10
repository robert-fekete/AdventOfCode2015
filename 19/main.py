import re
from collections import deque, Counter


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

def tokenize(molecule):

    tokens = {}
    i = 1
    prev_i = 0
    while i < len(molecule):
        if molecule[i].isupper():
            token = molecule[prev_i:i]
            if token not in tokens:
                tokens[token] = 0
            tokens[token] += 1

            prev_i = i
        i+=1

    return tokens

def solve_second(input_string):

    parts = [part for part in input_string.strip().split('\n') if part != ""]
    replacement_strings = parts[:-1]
    required_molecule = parts[-1]
    required_atoms = tokenize(required_molecule)

    replacements = {}

    for replacement in replacement_strings:

        from_what, to_what = replacement.split(" => ")
        if from_what not in replacements:
            replacements[from_what] = []

        replacements[from_what].append(to_what)
        
    queue = deque([])
    visited = {}

    queue.append(('e', 0))

    max_steps = 0
    while len(queue) > 0:

        molecule, steps = queue.popleft()
        
        if max_steps < steps:
            print steps
            max_steps = steps
            print len(queue)


        molecule_length = len(molecule)
        if molecule_length not in visited:
            visited[molecule_length] = {}

        if molecule in visited[molecule_length]:
            continue

        visited[molecule_length][molecule] = True

        if molecule_length > len(required_molecule):
            continue
            
        atoms = tokenize(molecule)
        if "Y" in atoms and atoms["Y"] > required_atoms["Y"]:
            continue

        if "Rn" in atoms and atoms["Rn"] > required_atoms["Rn"]:
            continue

        if "Ar" in atoms and atoms["Ar"] > required_atoms["Ar"]:
            continue
            

        mol_list = list(molecule)
        for i in xrange(len(molecule)):
            if molecule[i] in replacements:
                fromm = molecule[i]
                for to in replacements[fromm]:
                    new_molecule = mol_list[:i] + [to] + mol_list[i+1:]

                    new_molecule = "".join(new_molecule)
                    if new_molecule == required_molecule:
                        return steps + 1
                    queue.append((new_molecule, steps + 1))
                    
            elif molecule[i:i+2] in replacements:
                fromm = molecule[i:i+2]
                for to in replacements[fromm]:
                    new_molecule = mol_list[:i] + list(to) + mol_list[i+2:]

                    new_molecule = "".join(new_molecule)
                    if new_molecule == required_molecule:
                        return steps + 1
                    queue.append((new_molecule, steps + 1))
                

    return -1


# print solve_first("H => HO\nH => OH\nO => HH\n\nHOH")  # 4
# print solve_first("H => HO\nH => OH\nO => HH\n\nHOHOHO")  # 7
# print solve_first("H => OO\n\nH2O")  # 1
# print solve_first("Mg => WUT\n\nMgMg")  # 2
# print solve_first(open(r'.\input.txt', 'r').read())
#
# print solve_second("e => O\ne => H\nH => HO\nH => OH\nO => HH\n\nHOH")  # 3
# print solve_second("e => O\ne => H\nH => HO\nH => OH\nO => HH\n\nHOHOHO")  # 6
# print solve_second("e => Mg\nMg => MgMg\nMg => Ag\n\nAgAg")  # 4
print solve_second(open(r'.\input.txt', 'r').read())
