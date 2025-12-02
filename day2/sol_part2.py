def getMultipliers(item:int):
    '''
    the item is quite small, so, it's ok
    '''
    result = []
    for i in range(1, item // 2 + 1):
        if item % i == 0:
            result.append(i)
    return result

def isPatternInvalid(item: str, pattern:int):
    for i in range(0, pattern):
        for k in range(i + pattern, len(item), pattern):
            if item[i] != item[k]:
                return False
    return True

def isStrInvalid(item: str):
    patterns = getMultipliers(len(item))
    for pattern in patterns:
        if isPatternInvalid(item, pattern):
            return True
    return False

def getItemsInvalidSum(fro:int, to:int):
    result = 0
    for i in range(fro, to + 1):
        result += i if isStrInvalid(str(i)) else 0
    return result

if __name__ == '__main__':
    ranges = []
    with open("test_file") as file:
        ranges = file.readlines()[0].strip().split(',')
        for i in range(len(ranges)):
            ranges[i] = ranges[i].split('-')
            ranges[i] = (int(ranges[i][0]), int(ranges[i][1]))

    result = 0
    for fro, to in ranges:
        result += getItemsInvalidSum(fro, to)
    print(result)
