def getBestVal(seq:list, begin:int = 0, n:int = 12):
    '''
    seq[i] is the first element;
    so, the rest subsequence is supposed to have n - 1;
    it doesn't make sense to consider n-1 sequence
    if there are no enough elements remaining
    '''
    if n == 0:
        return 0
    best_digit, best_spot = 0, 0
    for i in range(begin, len(seq) - n + 1):
        if seq[i] > best_digit:
            best_spot, best_digit = i, seq[i]
    prefix = best_digit * 10 ** (n-1)
    return prefix + getBestVal(seq, best_spot + 1, n - 1)

if __name__ == '__main__':
    sequences = []
    with open("test_file") as file:
        sequences = [tuple(map(int, item.strip())) for item in file.readlines()]
    result = 0
    for sequence in sequences:
        result += getBestVal(sequence, 0, 12)
    print(result)
