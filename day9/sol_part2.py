def lbs(arr, val):
    l, r = 0, len(arr) - 1
    while l < r:
        c = (l + r) // 2
        if arr[c] >= val:
            r = c
        else:
            l = c + 1
    return l

def rbs(arr, val):
    l, r = 0, len(arr) - 1
    while l < r:
        c = (l + r + 1) // 2
        if arr[c] <= val:
            l = c
        else:
            r = c - 1
    return l

def getXByY(coords):
    y_by_x = dict()
    for x, y in coords:
        if x not in y_by_x:
            y_by_x[x] = [y]
        else:
            y_by_x[x].append(y)
    return y_by_x

def getYByX(coords):
    x_by_y = dict()
    for x, y in coords:
        if y not in x_by_y:
            x_by_y[y] = [x]
        else:
            x_by_y[y].append(x)
    return x_by_y

def rearrangeItems(x_by_y, y_by_x):
    for x in y_by_x:
        y_by_x[x].sort()
    for y in x_by_y:
        x_by_y[y].sort()
    update_items_x = {}
    update_items_y = {}
    for x in y_by_x:
        for y_index in range(1, len(y_by_x[x])):
            # the begin and the end must be not included because nodes already exist there
            start_y_interval = y_by_x[x][y_index - 1] + 1
            end_y_interval = y_by_x[x][y_index]
            for y in range(start_y_interval, end_y_interval):
                if y not in x_by_y:
                    continue
                nearest_right_side = lbs(x_by_y[y], x)
                nearest_left_side = rbs(x_by_y[y], x)
                if (x_by_y[y][nearest_right_side] > x) and (x_by_y[y][nearest_left_side] < x):
                    if x in update_items_x:
                        update_items_x[x].append(y)
                    else:
                        update_items_x[x] = [y]
                    if y in update_items_y:
                        update_items_y[y].append(x)
                    else:
                        update_items_y[y] = [x]
    for x in update_items_x:
        y_by_x[x] += update_items_x[x]
        y_by_x[x].sort()
    for y in update_items_y:
        x_by_y[y] += update_items_y[y]
        x_by_y[y].sort()
### TEST START:
test_x_by_y = {
        -1: [10],
        0: [22, 0, 8, 13, 15],
        2: [0, 6, 10, 13],
        8: [0, 8, 6, 10]
        }
test_y_by_x = {
    0: [8, 0, 2],
    6: [2, 8],
    8: [0, 8],
    10:[2, -1, 8],
    13: [0, 2],
    15: [0],
    22: [0]
}

rearrangeItems(test_x_by_y, test_y_by_x)
expected_x_by_y = {
    -1: [10],
    0: [0, 8, 10, 13, 15, 22],
    2: [0, 6, 8, 10, 13],
    8: [0, 6, 8, 10]
}
expected_y_by_x = {
    0: [0, 2, 8],
    6: [2, 8],
    8: [0, 2, 8],
    10: [-1, 0, 2, 8],
    13: [0, 2],
    15: [0],
    22: [0]
}

assert test_x_by_y == expected_x_by_y
assert test_y_by_x == expected_y_by_x
# TEST END

def getOrientedGraph(coords):
    x_by_y = getXByY(coords)
    y_by_x = getYByX(coords)
    rearrangeItems(x_by_y, y_by_x)
    result = dict()
    for x in y_by_x:
       for i in range(1, len(y_by_x[x])):
           prev_node = (x, y_by_x[x][i-1])
           current_node = (x, y_by_x[x][i])
           result[prev_node] = [current_node]
    for y in x_by_y:
        for i in range(1, len(x_by_y[y])):
            prev_node = (x_by_y[y][i-1], y)
            current_node = (x_by_y[y][i], y)
            if prev_node in result:
                result[prev_node].append(current_node)
            else:
                result[prev_node] = [current_node]
    return result

def makeUnoriented(graph):
    backwards = dict()
    for node in graph:
        for _node in graph[node]:
            if _node not in backwards:
                backwards[_node] = [node]
            else:
                backwards[_node].append(node)
    for node in backwards:
        graph[node] = backwards[node]

def getPolygons(graph):
    polygons = []
    for node in graph:
        if len(graph[node]) > 1:
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
    graph = getOrientedGraph(coords)
    makeUnoriented(graph)
    polygons = getPolygons(graph)
    pexit()
    for i, (x1, y1) in enumerate(coords):
        for _, (x2, y2) in enumerate(coords, i + 1):
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            _best = max(best, (max_x - min_x + 1) * (max_y - min_y + 1))
            if (_best > best) and insidePolygon(polygons, x1, y1, x2, y2):
                best = _best
    print('Part 2', _best)
        


