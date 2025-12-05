

ranges = []

with open("input.txt", "r") as file:
    for l in file:
        line = l.strip()
        if line == "":
            break
        start = line.split("-")[0]
        end = line.split("-")[1]
        ranges.append([int(start), int(end)])

ranges.sort(key=lambda x: x[0])

merged = [ranges.pop(0)]

for start, end in ranges:
    last_start, last_end = merged[-1]
    if start <= last_end:
        merged[-1][1] = max(end, last_end)
    else:
        merged.append([start, end])


print(sum([m[1] - m[0] + 1 for m in merged]))