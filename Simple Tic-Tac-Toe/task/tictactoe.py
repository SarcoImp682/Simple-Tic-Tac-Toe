# write your code here
griddle = '         '

grid = [[griddle[0], griddle[1], griddle[2]],
        [griddle[3], griddle[4], griddle[5]],
        [griddle[6], griddle[7], griddle[8]]]


def grid_print():
    print('---------')
    print(f'| {grid[0][0]} {grid[0][1]} {grid[0][2]} |')
    print(f'| {grid[1][0]} {grid[1][1]} {grid[1][2]} |')
    print(f'| {grid[2][0]} {grid[2][1]} {grid[2][2]} |')
    print('---------')


grid_print()
loop_num = 1
full_break = False

while True:
    if loop_num % 2 != 0:
        player = 'X'
    else:
        player = 'O'

    co_ords = input('Enter the coordinates:')
    co_list = co_ords.split()
    if co_ords[0].isdigit() and co_ords[2].isdigit():
        row = int(co_ords[0]) - 1
        column = int(co_ords[2]) - 1
        if 4 > int(co_ords[0]) > 0 and 4 > int(co_ords[2]) > 0:
            if grid[row][column] == ' ':
                grid[row][column] = player
            else:
                print('This cell is occupied! Choose another one!')
                loop_num -= 1
        else:
            print('Coordinates should be from 1 to 3!')
            loop_num -= 1
    else:
        print('You should enter numbers!')
        loop_num -= 1
    grid_print()
    if grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
        if grid[1][1] == 'X':
            print('X wins')
            break
        if grid[1][1] == 'O':
            print('O wins')
            break

    if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0]:
        if grid[1][1] == 'X':
            print('X wins')
            break
        if grid[1][1] == 'O':
            print('O wins')
            break

    for x in range(0, 3):
        rvalues = [row[x] for row in grid]
        rvalues_set = set(rvalues)
        if len(rvalues_set) == 1:
            if 'X' in rvalues_set:
                print('X wins')
                full_break = True
                break
            if 'O' in rvalues_set:
                print('O wins')
                full_break = True
                break

    if full_break == True:
        break

    for y in range(0, 3):
        cvalues = grid[y]
        cvalues_set = set(cvalues)
        if len(cvalues_set) == 1:
            if 'X' in cvalues_set:
                print('X wins')
                full_break = True
                break
            if 'O' in cvalues_set:
                print('O wins')
                full_break = True
                break

    if full_break == True:
        break

    loop_num += 1
    if loop_num == 10:
        print('Draw')
        break
