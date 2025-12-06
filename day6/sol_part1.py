def retrieveOperators(line:list):
    item_to_fun = {
        '*': lambda a, b: a * b,
        '+': lambda a, b: a + b
    }
    for i in range(len(line)):
        line[i] = item_to_fun[line[i]]

def retrieveNumbers(lines):
    for i in range(len(lines)):
        for k in range(len(lines[0])):
            lines[i][k] = int(lines[i][k])

if __name__ == '__main__':
    with open("test_file") as file:
        lines = [list(filter(lambda x:x!='', line.strip().split(' '))) for line in file.readlines()]
    operator_line = lines.pop()
    #print(operator_line)
    retrieveOperators(operator_line)
    retrieveNumbers(lines)
    #print(lines)
    for i in range(len(lines[0])):
        for k in range(1, len(lines)):
            lines[k][i] = operator_line[i](lines[k][i], lines[k-1][i])
    for i in range(1, len(lines[-1])):
        lines[-1][i] += lines[-1][i-1]
    print(lines[-1][-1])
