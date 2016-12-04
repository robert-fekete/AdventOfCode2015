

def increment(literal):

    chars = list(literal)
    index = len(chars) - 1
    go = True
    while go and index >=0:
        next_char, go = step(chars[index])
        chars[index] = next_char
        index -= 1

    return "".join(chars)

def step(character):

    char_code = ord(character)
    char_code += 1
    if char_code > 122:
        return ('a', True)

    return (chr(char_code), False)

def check(literal):

    if any([c in literal for c in ['i','o','l']]):
        return False

    iterator = iter(literal)
    inc = 0
    cond1 = False
    pairs = []
    prev = iterator.next()
    for c in iterator:
        if c == prev and not c in pairs:
            pairs.append(c)
        if ord(prev) + 1 == ord(c):
            inc += 1
        else:
            inc = 0

        prev = c

        if inc > 1:
            cond1 = True

    return cond1 and len(pairs) > 1

def generate(literal):
    
    next_password = increment(literal)
    while not check(next_password):
        next_password = increment(next_password)

    return next_password

print generate("cqjxxyzz")

