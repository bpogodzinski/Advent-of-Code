def get_max_joltage(bank):
    max_joltage = []
    numbers_to_remove = len(bank) - 12

    for joltage in bank:
        while numbers_to_remove > 0 and max_joltage and max_joltage[-1] < joltage:
            numbers_to_remove -= 1
            max_joltage.pop()
        max_joltage.append(joltage)
    if numbers_to_remove > 0:
        max_joltage = max_joltage[:-numbers_to_remove]

    return int("".join(max_joltage))

answer = []

with open("input.txt", "r") as f:
    for l in f:
        bank = l.strip()
        answer.append(get_max_joltage(bank))

print(sum(answer))
