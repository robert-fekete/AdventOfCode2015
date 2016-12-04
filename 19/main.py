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

    replacements = {}

    for replacement in replacement_strings:

        from_what, to_what = replacement.split(" => ")
        from_regex = re.compile(from_what)
        if from_regex not in replacements:
            replacements[from_regex] = []

        replacements[from_regex].append(to_what)


    queue = deque([])
    visited = []

    queue.append(('e', 0))

    while len(queue) > 0:

        molecule, steps = queue.popleft()

        if len(molecule) > len(required_molecule):
            continue
            
        if molecule in visited:
            continue

        visited.append(molecule)

        for i in xrange(len(molecule)):
            for regex in replacements:
                match = regex.match(molecule, i)
                if match is not None:
                    for to in replacements[regex]:
                        new_molecule = molecule[:match.start(0)] + to + molecule[match.end(0):]
                        # print molecule[:match.start(0)] + to + molecule[match.end(0):]

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
print solve_second(open(r'.\input.txt', 'r').read())
