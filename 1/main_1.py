
total = 0
previous = None

with open("input.txt") as lines:
    for line in lines:
        number = line.rstrip("\n")
        if previous is None or number > previous:
            total += 1
        previous = number

print(total)
