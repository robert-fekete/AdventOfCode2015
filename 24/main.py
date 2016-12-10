from operator import mul


def get_groups(packages, target, length, acc1, acc2):

    if sum(acc1) > target:
        return

    if sum(acc1) == target:
        acc2.append(acc1)

    if sum(packages[:length]) + sum(acc1) < target:
        return

    if length == 0:
        return

    for package in packages:
        new_packages = packages[:]
        new_packages.remove(package)

        new_acc = acc1[:]
        new_acc.append(package)

        get_groups(new_packages, target, length - 1, new_acc, acc2)


def solve(packages, num_of_groups):

    packages.sort(reverse=True)
    results = []
    for i in xrange(1, len(packages)):
        get_groups(packages, sum(packages) / num_of_groups, i, [], results)

        if len(results) != 0:
            break

    results.sort(key=lambda groups: reduce(mul, groups, 1))
    return reduce(mul, results[0], 1)


print solve([i for i in xrange(1, 12) if i != 6], 3)
print solve([i for i in xrange(1, 12) if i != 6], 4)

numbers = map(int, open('input.txt', 'r').read().strip().split('\n'))
print solve(numbers, 3)
print solve(numbers, 4)