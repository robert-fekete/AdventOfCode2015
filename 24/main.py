from operator import mul

def organize(packages, limit1, limit2, first, second, third, acc):
    
    if len(first) > limit2 or len(second) > limit2:
        return
        
    if sum(first) > limit1:
        return
        
    if sum(second) > limit1:
        return
        
    if sum(third) > limit1:
        return
        
    if len(packages) == 0:
        if len(second) < len(first) or len(third) < len(first):
            return
        acc.append((first, second, third))
        return
        
    organize(packages[1:], limit1, limit2, first + packages[:1], second, third, acc)
    organize(packages[1:], limit1, limit2, first, second + packages[:1], third, acc)
    organize(packages[1:], limit1, limit2, first, second, third + packages[:1], acc)

def solve(packages):
    
    results = []
    organize(packages, sum(packages) / 3, len(packages) / 3, [], [], [], results)
    results.sort(key=lambda groups: (len(groups[0]), reduce(mul, groups[0], 1)))
    
    for first, second, third in results:
        print "{0} - {1} - {2}".format(",".join(map(str, first)), ",".join(map(str, second)), ",".join(map(str, third)))
    return reduce(mul, results[0][0], 1)


print solve([i for i in xrange(1, 12) if i != 6])

numbers = map(int, open('input.txt', 'r').read().strip().split('\n'))
print solve(numbers)