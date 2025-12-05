def getRanges(lines):
    result = [None] * len(lines)
    for i in range(len(lines)):
        result[i] = list(map(int, lines[i].split('-')))
    return result

def calcGoodItems(ranges):
    ranges.sort(key = lambda x: x[0])
    base =  0
    for i in range(1, len(ranges)):
        if ranges[i][1] <= ranges[base][1]:
            ranges[i] = None
        elif ranges[i][0] <= ranges[base][1]:
            ranges[base][1] = ranges[i][1]
            ranges[i] = None
        else:
            base = i
    result = 0
    for item in ranges:
        if item:
            result += item[1] - item[0] + 1 
    # there are no exccessive intervals anymore:
    #print(ranges)
    return result

if __name__ == '__main__':
    sequences = []
    with open("test_file2") as file:
        lines = [line.strip() for line in file.readlines()]
    delim_index = lines.index('')
    print(calcGoodItems(getRanges(lines[:delim_index])))
