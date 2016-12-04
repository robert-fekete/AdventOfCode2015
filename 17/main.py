
def solve_rec(target_amount, current_amount, remaining_containers):

    if current_amount == target_amount:
        return 1

    if current_amount > target_amount:
        return 0

    total = 0
    for container in remaining_containers[:]:
        remaining_containers.remove(container)
        total += solve_rec(target_amount, current_amount + container, remaining_containers[:])

    return total

def solve_first(input, amount):

    numbers = map(int, input.strip().split('\n'))

    return solve_rec(amount, 0, numbers)

def solve_rec_min(target_amount, current_amount, current_containers, min_containers, number_of_solutions, remaining_containers):
    
    if current_amount == target_amount:
        if current_containers == min_containers:
            return (min_containers, number_of_solutions + 1)
        elif current_containers < min_containers:
            return (current_containers, 1)
        return (min_containers, number_of_solutions)

    if current_amount > target_amount:
        return (min_containers, number_of_solutions)

    for container in remaining_containers[:]:
        remaining_containers.remove(container)
        min_containers, number_of_solutions = solve_rec_min(target_amount, current_amount + container, current_containers + 1, min_containers, number_of_solutions, remaining_containers[:])


    return (min_containers, number_of_solutions)

def solve_second(input, amount):

    numbers = map(int, input.strip().split('\n'))

    return solve_rec_min(amount, 0, 0, len(numbers), 0, numbers)[1]


print solve_first("20\n15\n10\n5\n5\n", 25)
print solve_first(open(r'.\input.txt', 'r').read(), 150)
print solve_second("20\n15\n10\n5\n5\n", 25)
print solve_second(open(r'.\input.txt', 'r').read(), 150)