from collections import Counter

def is_removable(y, x, grid):
    adjacent_roll = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if y + i < 0 or y + i > len(grid) - 1:
                adjacent_roll.append(False)
                continue
            if x + j < 0 or x + j > len(grid[0]) - 1:
                adjacent_roll.append(False)
                continue
            
            if grid[y+i][x+j] == '@':
                adjacent_roll.append(True)
            else:
                adjacent_roll.append(False)
    return Counter(adjacent_roll)[True] < 4

grid = []
removed = 0
total_removed = 0

with open("input.txt", 'r') as f:
    for line in f:
        grid.append(list(line.strip()))
while True:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@':
                if is_removable(y, x, grid):
                    removed += 1
                    grid[y][x] = '.'
    total_removed += removed
    if removed == 0:
        break
    removed = 0

print(total_removed)