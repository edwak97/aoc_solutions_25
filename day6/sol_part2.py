def retrieveOperators(line:list):
    item_to_fun = {
        '*': lambda a, b: a * b,
        '+': lambda a, b: a + b,
    }
    for i in range(len(line)-1, -1, -1):
        if line[i] in {' ', '\n'}:
            del line[i]
        else:
            line[i] = item_to_fun[line[i]]

def getValFromSequence(sequence):
    result = 0
    for i in range(len(sequence)):
        result += int(sequence[i]) * 10 ** (len(sequence) - i - 1)
    return result

def processValues(vals, operator):
    for i in range(1, len(vals)):
        vals[i] = operator(vals[i], vals[i-1])
    return vals[-1]

def processLines(lines, operator_line):
    max_index = 0
    for i in range(len(lines)):
        # get rid of \n:
        del lines[i][-1]
        max_index = max(len(lines[i]), max_index)
    max_index -= 1
    result = 0
    for operator_i in range(len(operator_line)-1, -1, -1):
        values_to_process = [] 
        while max_index > -1:
            current_sequence = []
            for i in range(len(lines)):
                if len(lines[i]) == (max_index + 1):
                    if lines[i][-1] != ' ':
                        current_sequence.append(lines[i][-1])
                    del lines[i][-1]
            max_index -= 1
            if current_sequence == []:
                break
            values_to_process.append(getValFromSequence(current_sequence))
        result += processValues(values_to_process, operator_line[operator_i])
    return result
 
if __name__ == '__main__':
    with open("test_file") as file:
        lines = [list(line) for line in file.readlines()]
    operator_line = list(lines.pop())
    retrieveOperators(operator_line)
    print(processLines(lines, operator_line))

