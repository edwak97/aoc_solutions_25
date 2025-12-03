def getBestVal(seq:list):
    max_reducted_l = [None] * len(seq)
    max_reducted_r = [None] * len(seq)
    max_reducted_l[0], max_reducted_r[-1] = seq[0], seq[-1]
    for i in range(1, len(seq)):
        max_reducted_l[i] = max(max_reducted_l[i-1], seq[i])
    for i in range(len(seq) - 2, -1, -1):
        max_reducted_r[i] = max(max_reducted_r[i+1], seq[i])
    best_match = 0
    for i in range(len(seq) - 1):
        best_0_digit = max_reducted_l[i]
        best_1_digit = max_reducted_r[i+1]
        best_match = max(best_match, best_0_digit * 10 + best_1_digit)
    return best_match

if __name__ == '__main__':
    sequences = []
    with open("test_file") as file:
        sequences = [tuple(map(int, item.strip())) for item in file.readlines()]
    result = 0
    for sequence in sequences:
        result += getBestVal(sequence)
    print(result)
