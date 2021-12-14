
aim = 0
depth = 0
position = 0

with open("input.txt") as lines:
    for line in lines:
        instruction = line.split()
        if instruction[0] == "forward":
            position += int(instruction[1])
            depth += int(instruction[1]) * aim
        if instruction[0] == "up":
            aim -= int(instruction[1])
        if instruction[0] == "down":
            aim += int(instruction[1])

print(f"result: {depth} * {position} = {depth * position}")
