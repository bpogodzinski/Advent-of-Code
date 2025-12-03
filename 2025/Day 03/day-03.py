import itertools

max_joltage = []

with open("input.txt", "r") as f:
    for l in f:
        batteries = l.strip()
        combinations = [int(x[0] + x[1]) for x in itertools.combinations(batteries, 2)]
        max_joltage.append(max(combinations))

print(sum(max_joltage))
