def getRanges(lines):
    result = [None] * len(lines)
    for i in range(len(lines)):
        result[i] = tuple(map(int, lines[i].split('-')))
    return result

if __name__ == '__main__':
    sequences = []
    with open("test_file") as file:
        lines = [line.strip() for line in file.readlines()]
    delim_index = lines.index('')
    ranges = getRanges(lines[:delim_index])
    items_to_check = tuple(map(int, lines[delim_index+1:]))
    fresh_count = 0
    for i in items_to_check:
        for fro, to in ranges:
            if fro <= i <= to:
                fresh_count += 1
                break
    print(fresh_count)
