


lines = open('input.txt', 'r').read().strip().split("\n")
hp = int(lines[0].split(":")[1].strip())
damage = int(lines[1].split(":")[1].strip())
armor = int(lines[2].split(":")[1].strip())

max_damage = 13
max_armor = 10

options = []

for i in xrange(max_damage):
    for j in xrange(max_armor):

        player_turns = hp / max(i - armor, 1)
        boss_turns = 100 / max(damage - j, 1)
        if player_turns <= boss_turns:
            options.append((i, j))

print "\n".join(map(lambda p:"{0} - {1}".format(p[0], p[1]), options))