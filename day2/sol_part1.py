def isStrInvalid(item: str):
    count = len(item) // 2
    if len(item) != count * 2:
        return False
    for i in range(0, count):
        if item[i] != item[i + count]:
            return False
    return True

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
