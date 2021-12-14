total_measurements = 0
pointer = 0

with open("../2/input.txt") as lines:
    numbers = [int(line.rstrip("\n")) for line in lines]

length = len(numbers)

while pointer + 3 < length:
    s1 = numbers[pointer] + numbers[pointer + 1] + numbers[pointer + 2]
    s2 = numbers[pointer + 1] + numbers[pointer + 2] + numbers[pointer + 3]
    if s2 > s1:
        total_measurements += 1
    pointer += 1

print("total: " + str(total_measurements))
