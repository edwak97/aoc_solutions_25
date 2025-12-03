def getBestVal(seq:list, begin:int = 0, n:int = 12):
    '''
    seq[i] is the first element;
    so, the rest subsequence is supposed to have n - 1;
    it doesn't make sense to consider n-1 sequence
    if there are no enough elements remaining
    '''
    if n == 0:
        return 0
    best_match, best_digit = 0, 0
    for i in range(begin, len(seq) - n + 1):
        best_digit = max(best_digit, seq[i])
    for i in range(begin, len(seq) - n + 1):
        #tiny optimization
        if seq[i] < best_digit:
            continue
        prefix = seq[i] * 10 ** (n - 1)
        best_match = max(best_match, prefix + getBestVal(seq, i + 1, n - 1))
    return best_match

if __name__ == '__main__':
    sequences = []
    with open("test_file") as file:
        sequences = [tuple(map(int, item.strip())) for item in file.readlines()]
    result = 0
    for sequence in sequences:
        result += getBestVal(sequence, 0, 12)
    print(result)
