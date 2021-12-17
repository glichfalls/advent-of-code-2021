
numbers = []

line_length = None

with open("input.txt") as lines:
    for line in lines:
        number = line.rstrip("\n")
        if not line_length:
            line_length = len(number)
        numbers.append(number)

gamma = ""
epsilon = ""

for n in range(0, line_length):
    bit0 = 0
    bit1 = 0
    for number in numbers:
        if number[n] == "0":
            bit0 += 1
        else:
            bit1 += 1
    if bit1 > bit0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print("gamma: " + gamma + ", " + str(gamma_int))
print("epsilon: " + epsilon + ", " + str(epsilon_int))
print("result: " + str(gamma_int * epsilon_int))
