def getGraph(coords):
    y_by_x = dict()
    for x, y in coords:
        if x not in y_by_x:
            y_by_x[x] = [y]
        else:
            y_by_x[x].append(y)
    x_by_y = dict()
    for x, y in coords:
        if y not in x_by_y:
            x_by_y[y] = [x]
        else:
            x_by_y[y].append(x)
    for x in y_by_x:
        y_by_x[x].sort()
    for y in x_by_y:
        x_by_y[y].sort()
    result = dict()
    for x in y_by_x:
        prev_node = (x, y_by_x[x][0])
        if prev_node not in result:
            result[prev_node] = set()
        for _, y in enumerate(y_by_x[x], 1):
            current_node = (x, y)
            result[prev_node].add(current_node)
            if current_node not in result:
                result[current_node] = {prev_node}
            else:
                result[current_node].add(prev_node)
    for y in x_by_y:
        prev_node = (x_by_y[y][0], y)
        for _, x in enumerate(x_by_y[y], 1):
            current_node = (x, y)
            result[prev_node].add(current_node)
            result[current_node].add(prev_node)
    return result

def getPolygons(graph):
    pass
def insidePolygon(polygons, x1, y1, x2, y2):
    pass

if __name__ == '__main__':
    coords = []
    with open("test_file") as file:
        coords = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]
    best = 0
    for i, (x1, y1) in enumerate(coords):
        for _, (x2, y2) in enumerate(coords, i + 1):
            best = max(best, abs(x1 - x2 +1) * abs(y1 - y2 + 1))
    #Part 1:
    print('Part 1', best)
    print(len(coords))
    graph = getGraph(coords)
    print(graph)
    exit()
    polygons = getPolygons(graph)
    for i, (x1, y1) in enumerate(coords):
        for _, (x2, y2) in enumerate(coords, i + 1):
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            _best = max(best, (max_x - min_x + 1) * (max_y - min_y + 1))
            if (_best > best) and insidePolygon(polygons, x1, y1, x2, y2):
                best = _best
    print('Part 2', _best)
        


