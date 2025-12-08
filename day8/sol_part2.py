def updateJunction(box_to_junction, new_junction, old_junction):
    for i, junction in enumerate(box_to_junction):
        if junction == old_junction:
            box_to_junction[i] = new_junction
if __name__ == '__main__':
    lines = []
    with open("test_file") as file:
        lines = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]
    distances = []
    box_to_junction = [i for i in range(len(lines))]
    for i in range(len(lines)):
        for k in range(i+1, len(lines)):
            dist = (lines[i][0] - lines[k][0])**2 + (lines[i][1] - lines[k][1])**2 + (lines[i][2] - lines[k][2])**2
            distances.append((dist, i, k))
    distances.sort(key = lambda x:x[0])
    i = 0
    couple = None
    for _, box0, box1 in distances:
        if box_to_junction[box0] != box_to_junction[box1]:
            couple = (box0, box1)
            updateJunction(box_to_junction, box_to_junction[box0], box_to_junction[box1])
        i += 1
    print(lines[couple[0]][0] * lines[couple[1]][0])
