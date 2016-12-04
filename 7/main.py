
def AND(args):

    return args[0] & args[1] & 65535

def SET(args):

    return args[0]

def OR(args):

    return args[0] | args[1] & 65535

def NOT(args):

    return ~(args[0] & 65535) + 65536

def LSHIFT(args):

    return (args[0] << args[1]) & 65535

def RSHIFT(args):

    return (args[0] & 65535) >> args[1]

def try_to_cast_to_int(parameter):

    try:
        return int(parameter)
    except ValueError:
        return parameter

def is_value_known(parameter):
    
    return wires.has_key(parameter) or type(parameter).__name__ == "int"

def get_values(parameters):

    values = []
    for parameter in parameters:
        if type(parameter).__name__ == "int":
            values.append(parameter)
        else:
            values.append(wires[parameter])

    return values

def parse(lines):

    instructions = []
    for line in lines:
        parts = line.split("->")
        result = parts[1].strip()
        value = parts[0].strip()

        no_words = value.count(" ") + 1
        if no_words == 1:
            instruction = ("SET", tuple([try_to_cast_to_int(value)]), result)

        elif no_words == 2:
            value_parts = value.split(" ")
            instruction = (value_parts[0], tuple([try_to_cast_to_int(value_parts[1])]), result)
        elif no_words == 3:
            value_parts = value.split(" ")
            instruction = (value_parts[1], (try_to_cast_to_int(value_parts[0]), try_to_cast_to_int(value_parts[2])), result)
        else:
            print "HEY"

        instructions.append(instruction)

    return instructions

instructions = parse(open("input.txt", 'r').read().strip().split("\n"))

gates = {
    "AND" : AND,
    "OR" : OR,
    "SET" : SET,
    "NOT" : NOT,
    "LSHIFT" : LSHIFT,
    "RSHIFT" : RSHIFT
    }

wires = {}
iter = 0

while len(instructions) > 0:

    iter += 1
    for instruction in instructions[:]:

        if all([is_value_known(parameter) for parameter in instruction[1]]):
            wires[instruction[2]] = gates[instruction[0]](get_values(instruction[1]))
            instructions.remove(instruction)


print iter
print wires["a"]