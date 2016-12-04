
def generate(word):

    if len(word) == 0:
        return ""

    prev = 0
    next_word = ""
    character = word[0]
    for i in xrange(len(word)):
        if word[i] != character:
            next_word += str(i - prev) + str(character)
            prev = i
            character = word[i]

    next_word += str(len(word) - prev) + str(word[-1])

    return next_word

val = "1113122113"

for i in xrange(50):
    val = generate(val)

print len(val)