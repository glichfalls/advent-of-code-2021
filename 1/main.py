
total = 0
current = None

with open("input.txt") as lines:
    for line in lines:
        number = line.rstrip("\n")
        if current is None or number > current:
            total += 1
        current = number

print(total)
