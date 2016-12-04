

def get_number_of_lights(board, x, y):

    lights = 0

    if x > 0:
        if y > 0:
            lights += 1 if board[y-1][x-1] == '#' else 0

        lights += 1 if board[y][x-1] == '#' else 0

        if y < len(board) - 1:
            lights += 1 if board[y+1][x-1] == '#' else 0
    if y > 0:
        lights += 1 if board[y-1][x] == '#' else 0

    if y < len(board) - 1:
        lights += 1 if board[y+1][x] == '#' else 0

    if x < len(board[0]) - 1:
        if y > 0:
            lights += 1 if board[y-1][x+1] == '#' else 0

        lights += 1 if board[y][x+1] == '#' else 0

        if y < len(board) - 1:
            lights += 1 if board[y+1][x+1] == '#' else 0

    return lights


def solve_first(input_string, number_of_steps):

    board = input_string.strip().split('\n')

    for _ in xrange(number_of_steps):
        new_board = [['.'] * len(board[0]) for _ in xrange(len(board))]
        for i, line in enumerate(board):
            for j, light in enumerate(line):
                lights = get_number_of_lights(board, j, i)
                if light == '.':
                    if lights == 3:
                        new_board[i][j] = '#'
                    else:
                        new_board[i][j] = '.'
                else:
                    if lights == 2 or lights == 3:
                        new_board[i][j] = '#'
                    else:
                        new_board[i][j] = '.'

        board = new_board

    return sum([sum([1 for light in line if light == '#']) for line in board])


def solve_second(input_string, number_of_steps):

    board = map(list, input_string.strip().split('\n'))
    board[0][0] = '#'
    board[0][-1] = '#'
    board[-1][0] = '#'
    board[-1][-1] = '#'

    for _ in xrange(number_of_steps):
        new_board = [['.'] * len(board[0]) for _ in xrange(len(board))]
        for i, line in enumerate(board):
            for j, light in enumerate(line):

                if (i == 0 and j == 0) or (i == 0 and j == len(board[0]) - 1) or (i == len(board) - 1 and j == 0) or \
                        (i == len(board) - 1 and j == len(board[0]) - 1):
                    new_board[i][j] = '#'
                    continue

                lights = get_number_of_lights(board, j, i)
                if light == '.':
                    if lights == 3:
                        new_board[i][j] = '#'
                    else:
                        new_board[i][j] = '.'
                else:
                    if lights == 2 or lights == 3:
                        new_board[i][j] = '#'
                    else:
                        new_board[i][j] = '.'

        # print "\n".join(["".join(line) for line in new_board])
        # print
        board = new_board

    return sum([sum([1 for light in line if light == '#']) for line in board])

print solve_first(".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..", 4)  # 4
print solve_first(open(r'.\input.txt', 'r').read(), 100)
print solve_second(".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..", 5)  # 17
print solve_second(open(r'.\input.txt', 'r').read(), 100)
