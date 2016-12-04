
def parse(content):

    distances = []
    for line in content.split("\n"):
        new_line = line.replace(" would", "").replace(" gain", "").replace("lose ", "-").replace(" happiness units by sitting next to", "").replace(".", "")

        from_p, unit, to_p = new_line.split(" ")

        same_edges = [x for x in distances if x[0] == to_p and x[1] == from_p]
        if len(same_edges) == 0:
            distances.append([from_p, to_p, int(unit)])
        else:
            same_edges[0][2]+= int(unit)
    
    return distances

def populate_distance(distances):
    
    starting_point = "NorthPole"

    cities_set = set()
    for distance in distances:
        cities_set.add(distance[0])
        cities_set.add(distance[1])

    cities = list(cities_set)
    for i in xrange(0, len(cities)):
        node_index[cities[i]] = i+1
        distances.append((starting_point, cities[i], 0))

    cities.append(starting_point)
    node_index[starting_point] = 0

    for i in xrange(0, len(cities)):
        distance_matrix.append( [0] * len(cities))

    for distance in distances:
        
        from_city, to_city, d = distance
        from_node = node_index[from_city]
        to_node = node_index[to_city]
        
        distance_matrix[from_node][to_node] = d
        distance_matrix[to_node][from_node] = d
        
def alg1():

    global all_distance
    all_distance = {}

    cities = node_index.keys()
    calc_distance(cities, [])

    path = all_distance.keys()[0]
    d = all_distance[path]
    for k,v in all_distance.iteritems():
        if v > d:
            path = k
            d = v
    print path
    print d

def calc_distance(cities, path):

    if len(cities) == 0:
        full_path = tuple(path)
        d = 0
        prev = ""
        for city in full_path:
            if prev == "":
                prev = city
                continue
            from_node = node_index[prev]
            to_node = node_index[city]
            d += distance_matrix[from_node][to_node]
            prev = city

        first = node_index[full_path[0]]
        last = node_index[full_path[-1]]
        d += distance_matrix[first][last]
        all_distance[full_path] = d
        return

    for city in cities:

        temp = cities[:]
        temp.remove(city)
        temp_path = path[:]
        temp_path.append(city)

        calc_distance(temp, temp_path)

    return

def alg2():

    path = held_karp()

    for p in path:
        print get_key(p, node_index)

def held_karp():

    D = {}
    p = {}
    subsets = generate_subsets(range(1, len(distance_matrix)))

    for i in xrange(1, len(distance_matrix)):
        add_to_dic((i,), i, distance_matrix[0][i], D)
        add_to_dic((), i, i, p)

    for i in xrange(2, len(distance_matrix)):
        for s in [s for s in subsets if len(s) == i]:
            for c in s:
                
                temp = s[:]
                temp.remove(c)
                temp_tuple = tuple(temp)
                d = min([D[temp_tuple][x] + distance_matrix[x][c] for x in temp_tuple])


                add_to_dic(tuple(s), c, d, D)

    path = [0]
    nodes = range(1, len(distance_matrix))
    dist = min(D[tuple(nodes)].values())
    print "Min distance " + str(dist)

    while len(path) < len(distance_matrix):
        d = D[tuple(nodes)]

        min_node = d.keys()[0]
        min_value = d[min_node]
        for node, value in d.iteritems():
            full_value = value + distance_matrix[node][path[-1]]
            if full_value < min_value:
                min_value = full_value
                min_node = node

        nodes.remove(min_node)
        path.append(min_node)

    path.append(0)
    return path

def add_to_dic(key, x, value, dictionary):

    if not dictionary.has_key(key):
        dictionary[key] = {}
    
    dictionary[key][x] = value

def get_key(value, dictionary):

    for k,v in dictionary.iteritems():
        if v == value:
            return k

def generate_subsets(S):

    result = [[]]
    for x in S:
        result = result + [y + [x] for y in result]
    return result


node_index = {}
distance_matrix = []

input_file = 'input2.txt'
distances = parse(open(input_file,'r').read().strip())
populate_distance(distances)

alg1()
