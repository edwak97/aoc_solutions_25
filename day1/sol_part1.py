lines = []
with open("test_file") as file:
    lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = (lines[i][0], int(lines[i][1:]))

clock_range = 100
current_position = 50
result = 0
for direction, value in lines:
    value = value if direction == 'L' else -value
    current_position = (current_position + value) % clock_range
    if current_position == 0:
        result += 1
print(result)
