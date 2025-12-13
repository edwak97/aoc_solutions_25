import sys

def lbs(arr, val, fun = lambda x:x):
    l, r = 0, len(arr) - 1
    while l < r:
        c = (l + r) // 2
        if fun(arr[c]) >= val:
            r = c
        else:
            l = c + 1
    return l

def rbs(arr, val, fun = lambda x: x):
    l, r = 0, len(arr) - 1
    while l < r:
        c = (l + r + 1) // 2
        if fun(arr[c]) <= val:
            l = c
        else:
            r = c - 1
    return l

def getYByX(coords):
    y_by_x = dict()
    for x, y in coords:
        if x not in y_by_x:
            y_by_x[x] = [y]
        else:
            y_by_x[x].append(y)
    for x in y_by_x:
        y_by_x[x].sort()
    return y_by_x

def getXByY(coords):
    x_by_y = dict()
    for x, y in coords:
        if y not in x_by_y:
            x_by_y[y] = [x]
        else:
            x_by_y[y].append(x)
    for y in x_by_y:
        x_by_y[y].sort()
    return x_by_y

def rearrangeItems(x_by_y, y_by_x, debug = False):
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
        if debug:
            print(f"x: {x} axis updated")
        y_by_x[x] += update_items_x[x]
        y_by_x[x].sort()
    for y in update_items_y:
        if debug:
            print(f"y: {y} axis updated")
        x_by_y[y] += update_items_y[y]
        x_by_y[y].sort()
### TEST START:
test_x_by_y = {
        -1: [10],
        0: [0, 8, 13, 15, 22],
        2: [0, 6, 10, 13],
        8: [0, 6, 8, 10, 14],
        13:[13]
        }
test_y_by_x = {
    0: [0, 2, 8],
    6: [2, 8],
    8: [0, 8],
    10:[-1, 2, 8],
    13: [0, 2, 13],
    14: [8],
    15: [0],
    22: [0]
}

rearrangeItems(test_x_by_y, test_y_by_x)
expected_x_by_y = {
    -1: [10],
    0: [0, 8, 10, 13, 15, 22],
    2: [0, 6, 8, 10, 13],
    8: [0, 6, 8, 10, 13, 14],
    13: [13]
}
expected_y_by_x = {
    0: [0, 2, 8],
    6: [2, 8],
    8: [0, 2, 8],
    10: [-1, 0, 2, 8],
    13: [0, 2, 8, 13],
    14: [8],
    15: [0],
    22: [0]
}

assert test_x_by_y == expected_x_by_y
assert test_y_by_x == expected_y_by_x
# TEST END

class Polyg:

    def __init__(self, polyg):
        self.val = polyg
        self.vertical_items = self.getVerticalItems(polyg)
        self.x_keys = sorted(tuple(self.vertical_items.keys()))

        self.horizontal_items = self.getHorizontalItems(polyg)
        self.y_keys = sorted(tuple(self.horizontal_items.keys()))

    def getVerticalItems(self, polygon):
        vertical_items = dict()
        for i in range(1, len(polygon)):
            x_i, y_i = polygon[i]
            _,   y_prev = polygon[i-1]

            y_prev, y_i = min(y_i, y_prev), max(y_i, y_prev)

            if y_i != y_prev:
                if x_i in vertical_items:
                    vertical_items[x_i].append((y_prev, y_i))
                else:
                    vertical_items[x_i] = [(y_prev, y_i)]
        for x in vertical_items:
            vertical_items[x].sort()
        return vertical_items

    def getHorizontalItems(self, polygon):
        horizontal_items = dict()
        for i in range(1, len(polygon)):
            x_i, y_i = polygon[i]
            x_prev, _ = polygon[i-1]

            x_prev, x_i = min(x_i, x_prev), max(x_i, x_prev)
            if x_i != x_prev:
                if y_i in horizontal_items:
                    horizontal_items[y_i].append((x_prev, x_i))
                else:
                    horizontal_items[y_i] = [(x_prev, x_i)]
        for y in horizontal_items:
            horizontal_items[y].sort()
        return horizontal_items

def getGraph(coords):
    x_by_y = getXByY(coords)
    y_by_x = getYByX(coords)
    rearrangeItems(x_by_y, y_by_x, True)
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
    makeUnoriented(result)

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
        if node in graph:
            graph[node] += backwards[node]
        else:
            graph[node] = backwards[node]

def dfs(graph, base_node, current_node, path, paths, checked_for_polygon):
    for node in graph[current_node]:
        if (node in checked_for_polygon):
            continue
        if (node == base_node) and (len(path) > 1) and (path[-2] != base_node):
            paths.append(path + (node,))
            continue
        if node in path:
            continue
        dfs(graph, base_node, node, path + (node,), paths, checked_for_polygon)

def getPolygons(graph):
    cycled_paths = []
    #this set contains items for which loops have been considered already
    checked_for_polygon = set()
    for base_node in graph:
        path = (base_node,)
        dfs(graph, base_node, base_node, path, cycled_paths, checked_for_polygon)
        checked_for_polygon.add(base_node)
    for i in range(len(cycled_paths)-1, -1, -1):
        if tuple(reversed(cycled_paths[i])) in cycled_paths:
            del cycled_paths[i]

    for i in range(len(cycled_paths)):
        cycled_paths[i] = Polyg(cycled_paths[i])

    return cycled_paths

def isInsidePolygon(polygon, x_min, y_min, x_max, y_max):
    #no line of the cycled path from x_min to x_max crosses vertical items
    #(except those on boundaries)
    left_boundary, right_boundary = polygon.x_keys[0], polygon.x_keys[-1]
    up_boundary, down_boundary = polygon.y_keys[-1], polygon.y_keys[0]
    if (x_min < left_boundary) or (x_max > right_boundary) or (y_max > up_boundary) or (y_min < down_boundary):
        return False
    for x, x_boundary in {(x_min, left_boundary), (x_max, right_boundary)}:
        if x == x_boundary:
            for y in {y_min, y_max}:
                interval_i = lbs(polygon.vertical_items[x], y, lambda x:x[1])
                y0, y1 = polygon.vertical_items[x][interval_i]
                if not (y0 <= y <= y1):
                    return False
    for y, y_boundary in {(y_min, up_boundary), (y_max, down_boundary)}:
        if y == y_boundary:
            for x in {x_min, x_max}:
                interval_i = lbs(polygon.horizontal_items[y], x, lambda x:x[1])
                x0, x1 = polygon.horizontal_items[y][interval_i]
                if not (x0 <= x <= x1):
                    return False
    for x_i in range(1, len(polygon.x_keys) - 1):
        x = polygon.x_keys[x_i]
        # the vertical item of polygon MUST NOT cross y_min or y_max line
        for y_line in {y_min, y_max}:
            interval_i = lbs(polygon.vertical_items[x], y_line, lambda x:x[1])
            y0, y1 = polygon.vertical_items[x][interval_i]
            if (y0 < y_line < y1):
                return False
    for y_i in range(1, len(polygon.y_keys)-1):
        y = polygon.y_keys[y_i]
        for x_line in {x_min, x_max}:
            interval_i = lbs(polygon.horizontal_items[y], x_line, lambda x:x[1])
            x0, x1 = polygon.horizontal_items[y][interval_i]
            if (x0 < x_line < x1):
                return False
    return True

def isInsideSomePolygon(polygons, x_min, y_min, x_max, y_max):
    for polygon in polygons:
        if isInsidePolygon(polygon, x_min, y_min, x_max, y_max):
            return True
    return False

def readCoords(name):
    coords = None
    with open(name) as file:
        coords = tuple([tuple(map(int, line.strip().split(','))) for line in file.readlines()]) 
    return coords

if __name__ == '__main__':
    coords = readCoords("test_file")
    best = 0
    for i, (x1, y1) in enumerate(coords):
        for k in range(i + 1, len(coords)):
            x2, y2 = coords[k]
            best = max(best, abs(x1 - x2 + 1) * abs(y1 - y2 + 1))
    print('Part 1', best)
    debug = (len(sys.argv) > 1) and ('debug' in sys.argv)
    graph = getGraph(coords)
    polygons = getPolygons(graph)
    best = 0
    #coords = [(2,3), (9,5)
    #print('verticals',polygons[0].vertical_items)
    #print('horizontals',polygons[0].horizontal_items)
    for i, (x1, y1) in enumerate(coords):
        for k in range(i + 1, len(coords)):
            x2, y2 = coords[k]
            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)
            _best = (x_max - x_min + 1) * (y_max - y_min + 1)
            if debug:
                print(f"Analazying rect ({x_min}, {y_min}), ({x_max}, {y_max}) with possible s = {_best}:")
            if (_best > best) and isInsideSomePolygon(polygons, x_min, y_min, x_max, y_max):
                if debug:
                    print('rect is ok')
                best = _best
            if debug:
                print('-----------\n')
    print('Part 2', best)
        


