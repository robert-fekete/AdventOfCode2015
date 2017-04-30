import re
from collections import deque, Counter
import heapq


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

    replacements = {}

    for replacement in replacement_strings:

        from_what, to_what = replacement.split(" => ")
        if from_what not in replacements:
            replacements[from_what] = []

        replacements[from_what].append(to_what)
        
    heap = []
    visited = {}

    heapq.heappush(heap, (len(required_molecule), 0, required_molecule))

    max_steps = 0
    while len(heap) > 0:

        length, steps, molecule = heapq.heappop(heap)
        
        if max_steps < steps:
            print "depth: {0}".format(steps)
            max_steps = steps
            # print len(queue)

        if molecule == 'e':
            return steps

        if length not in visited:
            visited[length] = {}

        if molecule in visited[length]:
            continue

        visited[length][molecule] = True

        atoms = tokenize(molecule)

        mol_list = list(molecule)
        for i in xrange(len(molecule)):
            for from_what in replacements:
                for to_what in replacements[from_what]:

                    if molecule[i:i+len(to_what)] == to_what:
                        new_molecule = mol_list[:i] + [from_what] + mol_list[i+len(to_what):]
                        new_molecule = "".join(new_molecule)
                        heapq.heappush(heap,(len(new_molecule), steps + 1, new_molecule))

    return -1


# print solve_first("H => HO\nH => OH\nO => HH\n\nHOH")  # 4
# print solve_first("H => HO\nH => OH\nO => HH\n\nHOHOHO")  # 7
# print solve_first("H => OO\n\nH2O")  # 1
# print solve_first("Mg => WUT\n\nMgMg")  # 2
# print solve_first(open(r'.\input.txt', 'r').read())
#
print solve_second("e => O\ne => H\nH => HO\nH => OH\nO => HH\n\nHOH")  # 3
print solve_second("e => O\ne => H\nH => HO\nH => OH\nO => HH\n\nHOHOHO")  # 6
print solve_second("e => Mg\nMg => MgMg\nMg => Ag\n\nAgAg")  # 4
print solve_second(open(r'.\input.txt', 'r').read())
