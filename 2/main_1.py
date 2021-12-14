
depth = 0
position = 0

with open("input.txt") as lines:
    for line in lines:
        instruction = line.split()
        if instruction[0] == "forward":
            position += int(instruction[1])
        if instruction[0] == "up":
            depth -= int(instruction[1])
        if instruction[0] == "down":
            depth += int(instruction[1])

print(f"result: {depth} * {position} = {depth * position}")
