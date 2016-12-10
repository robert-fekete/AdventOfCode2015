

def solve_first(row, column):
    max_count = row+column

    board = []
    for i in reversed(xrange(max_count)):
        board.append([0] * i)

    max_col = 1
    value = 2
    prev = 20151125
    board[0][0] = prev

    for _ in xrange(max_count - 2):
        row_iter = max_col
        for j in xrange(max_col + 1):
            board[row_iter][j] = (prev * 252533) % 33554393
            prev = board[row_iter][j]

            row_iter -= 1
        max_col += 1

    return board[row-1][column-1]


line = open('input.txt', 'r').read().strip()
row, column = map(int, line.strip('.').split(" row ")[1].split(", column "))
print row, column

print solve_first(4, 3)  # 21345942
print solve_first(row, column)
