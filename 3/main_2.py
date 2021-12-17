

def get_bits(nums, pos):
    bits = [[], []]
    for num in nums:
        bits[0 if num[pos] == "0" else 1].append(num)
    print(pos, bits)
    return bits


def get_nums_with_most_common_bit(bits):
    return bits[0] if len(bits[0]) > len(bits[1]) else bits[1]


def get_nums_with_least_common_bit(bits):
    return bits[1] if len(bits[0]) > len(bits[1]) else bits[0]


numbers = []
length = None
with open("input.txt") as lines:
    for line in lines:
        if length is None:
            length = len(line.rstrip("\n"))
        numbers.append(line.rstrip("\n"))


oxygen = numbers
co2 = numbers
for x in range(0, length):
    if len(oxygen) > 1:
        oxygen = get_nums_with_most_common_bit(get_bits(oxygen, x))
    if len(co2) > 1:
        co2 = get_nums_with_least_common_bit(get_bits(co2, x))


print(oxygen, co2)

result = int(oxygen[0], 2) * int(co2[0], 2)

print("result: "  + str(result))
