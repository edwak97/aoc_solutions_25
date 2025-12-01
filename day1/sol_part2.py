lines = []
with open("test_file") as file:
    lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = (lines[i][0], int(lines[i][1:]))
#lines = [('R', 1000)]
clock_range = 100
def getZeros(fro, to):
    l, r = min(fro, to), max(fro, to)
    hundred_l = l // clock_range
    hundred_l = (hundred_l + 1) if clock_range*hundred_l < l else hundred_l
    hundred_r = r // clock_range
    if hundred_r < hundred_l:
        return 0
    return (hundred_r - hundred_l) if (fro == 0) else (hundred_r - hundred_l + 1)

current_position = 50
result = 0

for direction, value in lines:
    value = value if direction == 'L' else -value
    next_position = current_position + value
    zeros = getZeros(current_position, next_position)
    #print(f"{value}: {zeros}")
    result += zeros
    current_position = next_position % clock_range
print(result)
