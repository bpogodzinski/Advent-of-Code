def is_invalid_id(sequence):
    if sequence.startswith("0"):
        return True
    if len(sequence) % 2 == 0:
        middle_index = len(sequence) // 2
        first = sequence[:middle_index]
        last = sequence[middle_index:]
        if first == last:
            return True
    return False

data = None
invalid_ids = []

with open("input.txt", "r") as f:
    data = f.read().split(",")
for entry in data:
    range_start = entry.split("-")[0]
    range_end = entry.split("-")[1]
    for i in range(int(range_start), int(range_end) + 1):
        if is_invalid_id(str(i)):
            invalid_ids.append(i)

print(sum(invalid_ids))

