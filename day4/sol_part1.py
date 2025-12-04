def isOutOfBoundary(y, x, lines):
    return (y < 0) or (x < 0) or (y > len(lines) - 1) or (x > len(lines[0]) - 1)

eight_gang = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1, 1), (-1, 0)]

def getRollsAvailable(y:int, lines:list):
    result = 0
    for x in range(len(lines[0])):
        if lines[y][x] != '@':
            continue
        limit = 4
        for y_shift, x_shift in eight_gang:
            _y, _x = y + y_shift, x + x_shift
            limit -= 1 if (not isOutOfBoundary(_y, _x, lines)) and lines[_y][_x] == '@' else 0
        if limit > 0:
            result += 1
            #part2:
            lines[y][x] = '.'
    return result

if __name__ == '__main__':
    sequences = []
    with open("test_file") as file:
        lines = [list(line.strip()) for line in file.readlines()]
    result = 0
    current_harvest = True
    while current_harvest:
        current_harvest = 0
        for i in range(len(lines)):
            current_harvest += getRollsAvailable(i, lines)
        result += current_harvest
    print(result)
