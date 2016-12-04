
def check(word):

    prev = ''
    prevprev = ''

    crit1 = False
    crit2 = False

    for letter in word:
        
        crit1 |= prev != '' and word.count(prev+letter) > 1
        crit2 |= prevprev == letter

        prevprev = prev
        prev = letter

    return crit1 and crit2

def check_crit2(prev, current):

    return prev == current

def check_crit3(prev, current):

    if prev == 'a':
        return current == 'b'
    if prev == 'c':
        return current == 'd'
    if prev == 'p':
        return current == 'q'
    if prev == 'x':
        return current == 'y'

    return False

f = open("input.txt", 'r')
lines = f.read().split("\n")

print check("qjhvhtzxzqqjkmpb")
print check("xxyxx")
print check("uurcxstgmygtbstg")
print check("wymbolrlwosnbxqx")

total = 0

for line in lines:
    if check(line):
        total+=1

print total