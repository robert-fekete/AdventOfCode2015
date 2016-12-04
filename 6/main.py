
def parse(content):

    squares = []
    for line in content.split("\n"):
        squares.append(parse_line(line))

    return squares

def parse_line(line):

    parts = line.split(",")
    first_parts = parts[0].split(" ")
    second_parts = parts[1].split(" ")

    action = " ".join(first_parts[0:-1])
    action_id = 1
    if action == "turn off":
        action_id = 2
    elif action == "toggle":
        action_id = 3

    x1 = int(first_parts[-1])
    y1 = int(second_parts[0])
    x2 = int(second_parts[2])
    y2 = int(parts[2])

    return [action_id, (x1, y1), (x2,y2)]

def generate():

    matrix = list()
    max = 1000

    temp_line = list()
    for i in xrange(0, max):
        temp_line.append(0)

    for i in xrange(0, max):
        matrix.append(temp_line[:])

    return matrix

def set_lamp(instruction):

    lines = matrix[instruction[1][0] : instruction[2][0] + 1]

    for i in xrange(instruction[1][1], instruction[2][1] + 1):
        for line in lines:
            if instruction[0] == 1:
                line[i] += 1
            elif instruction[0] == 2:
                line[i] -= 1
                if line[i] < 0:
                    line[i] = 0
            elif instruction[0] == 3:
                line[i] += 2

def count():

    total = 0
    for line in matrix:
        for lamp in line:
            if lamp:
                total+=lamp

    return total

instructions = parse(open("input.txt", 'r').read().strip())
matrix = generate()

for inst in instructions:
    set_lamp(inst)

print count()

