def partition(sequence):
    partitions = []
    for i, c in enumerate(sequence):
        if i == 0:
            partitions.append(c)
            continue
        if i == len(sequence) // 2:
            break
        partitions.append(partitions[-1] + c)
    return partitions

def is_invalid_id(sequence):
    if sequence.startswith("0"):
        return True
    if int(sequence) < 10:
        return False
    
    sequence_length = len(sequence)
    for seq in partition(sequence):
        if seq * (sequence_length // len(seq)) == sequence:
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
