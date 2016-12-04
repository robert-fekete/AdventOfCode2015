class Ingredient():

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

    def get_value(self):

        if self.capacity < 0:
            self.capacity = 0
        if self.durability < 0:
            self.durability = 0
        if self.flavor < 0:
            self.flavor = 0
        if self.texture < 0:
            self.texture = 0
        if self.calories < 0:
            self.calories = 0

        return self.capacity * self.durability * self.flavor * self.texture;
    
    def __str__(self):
        return ",".join(map(str, [self.capacity, self.durability, self.flavor, self.texture, self.calories]))

def parse(content):

    ingredients = []
    for line in content.split("\n"):

        name, others = line.split(": capacity ")
        capacity, others = others.split(", durability ")
        durability, others = others.split(", flavor ")
        flavor, others = others.split(", texture ")
        texture, calories = others.split(", calories ")

        ingredients.append(Ingredient(name, capacity, durability, flavor, texture, calories))

    return ingredients

ingredients = parse(open("input.txt", "r").read().strip())
I = {}
I[1] = ingredients[3]
I[5] = ingredients[0]
I[6] = ingredients[2]
I[8] = ingredients[1]

#capacity = 0
#durability = 0
#flavor = 0
#texture = 0
#calories =  0
#stat = dict()


#for i in ingredients:
#    capacity += i.capacity
#    flavor += i.flavor
#    durability += i.durability
#    texture += i.texture
#    calories += i.calories
#    stat[i.name] = 1

#dough = Ingredient("dough", capacity, durability, flavor, texture, calories)

#for i in xrange(100 - len(ingredients)):

#    new_doughs = [Ingredient(ing.name,
#                             dough.capacity + ing.capacity,
#                             dough.durability + ing.durability,
#                             dough.flavor + ing.flavor,
#                             dough.texture + ing.texture,
#                             dough.calories + ing.calories) for ing in ingredients]

#    best = new_doughs[0]
#    for d in new_doughs:
#        if float(best.get_value()) / best.calories < float(d.get_value())/d.calories:
#            best = d

#    dough = best
#    stat[best.name] += 1
#    for i in ingredients[:]:
#        if i.calories > 500 - dough.calories:
#            ingredients.remove(i)
#    if len(ingredients) == 0:
#        break


#print dough.get_value()
#print stat
#print dough.calories
#print "Capacity: " + str(dough.capacity)
#print "Durability: " + str(dough.durability)
#print "Flavor: " + str(dough.flavor)
#print "Texture: " + str(dough.texture)


nums = [7, 5, 3, 1]
D = {}
max = 100

for i in xrange(max + 1):
    
    possibilities = []
    for n in nums:
        if i == n:
            possibilities.append(tuple([n]))

        if D.has_key(i-n):
            for pos in D[i-n]:
                temp = list(pos)
                temp.append(n)
                temp.sort()
                temp = tuple(temp)
                if not temp in possibilities:
                    possibilities.append(temp)
    D[i] = possibilities

print "Options ready"
    
all_poss = []

for o in D[100]:
    poss = []
    for i in o:
        if i == 1:
            poss.append(5)
        elif i == 3:
            poss.extend([8, 6, 1])
        elif i == 5:
            poss.extend([6, 6, 6, 6, 1])
        elif i == 7:
            poss.extend([8, 8, 8, 8, 1, 1, 1])
    
    poss.sort()
    all_poss.append(tuple(poss))

def get_value(possibility, ingredients):

    cap = 0
    dur = 0
    fla = 0
    tex = 0
    for n in [1, 5, 6, 8]:
        num = list(possibility).count(n)
        ing = ingredients[n]
        cap += num * ing.capacity
        dur += num * ing.durability
        fla += num * ing.flavor
        tex += num * ing.texture
        
    if cap < 0: cap = 0
    if dur < 0: dur = 0
    if fla < 0: fla = 0
    if tex < 0: tex = 0

    return cap * dur * fla * tex

best_score = get_value(all_poss[0], I)
best = all_poss[0]
for p in all_poss:
    
    score = get_value(p, I)
    if best_score < score:
        best = p
        best_score = score

print best
print best_score

