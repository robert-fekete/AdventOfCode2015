import math

class RainDeer():

    def __init__(self, speed, run_time, rest_time):
        self.speed = speed
        self.run_time = run_time
        self.rest_time = rest_time
        self.runs = True
        self.last_cycle_time = 0
        self.distance = 0
        self.points = 0

    def step(self):
        
        last_cycle_max = self.rest_time
        if self.runs:
            self.distance += self.speed
            last_cycle_max = self.run_time

        self.last_cycle_time += 1
        if self.last_cycle_time == last_cycle_max:
            self.runs = not self.runs
            self.last_cycle_time = 0

    def win_the_second(self):
        self.points += 1

    def __str__(self):

        return str(self.points)

def parse(content):

    rain_deers = []
    for line in content.split("\n"):
        name, others = line.split(" can fly ");
        speed, others = others.split(" km/s for ");
        run_time, others = others.split(" seconds, but then must rest for ");
        rest_time, others = others.split(" ");
        
        speed = int(speed)
        run_time = int(run_time)
        rest_time = int(rest_time)

        rain_deers.append(RainDeer(speed, run_time, rest_time))

    return rain_deers

def select_fastest(rain_deers):
    
    best = rain_deers[0]
    for rain_deer in rain_deers:
        if best[4] < rain_deer[4]:
            best = rain_deer

    return best

def calculate_distance(time, best):

    whole_cycle = math.floor(float(time)/ (best[2] + best[3]))
    remaining_time = time - whole_cycle * (best[2] + best[3])
    if remaining_time > best[2]:
        remaining_time = best[2]

    partial_distance = remaining_time * best[1]

    return whole_cycle * best[1] * best[2] + partial_distance

def select_best(rain_deers):

    best = rain_deers[0]
    for rain_deer in rain_deers:
        if best.distance < rain_deer.distance:
            best = rain_deer

    bests = []
    for rain_deer in rain_deers:
        if best.distance == rain_deer.distance:
            bests.append(rain_deer)

    return bests

def race_them(time, rain_deers):

    for i in xrange(time):
        for rain_deer in rain_deers:
            rain_deer.step()

        bests = select_best(rain_deers)
        for rain_deer in bests:
            rain_deer.win_the_second()

    winner = rain_deers[0]
    for rain_deer in rain_deers:
        if winner.points < rain_deer.points:
            winner = rain_deer

    return winner

time = 2503
rain_deers = parse(open("input.txt", "r").read().strip())
#best = select_fastest(rain_deers)

print race_them(time, rain_deers)
