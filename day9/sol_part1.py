if __name__ == '__main__':
    lines = []
    with open("test_file") as file:
        lines = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]
    best = 0
    for i, (a, b) in enumerate(lines):
        for k in range(i + 1, len(lines)):
            best = max(best, abs(a - lines[k][0]+1) * abs(b - lines[k][1]+1))
    print(best)
