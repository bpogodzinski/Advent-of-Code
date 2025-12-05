def is_in_range(ranges, n):
    for r in ranges:
        start = r.split("-")[0]
        end = r.split("-")[1]
        if n >= int(start) and n <= int(end):
            return True
    return False

ranges = []
ingredients = []
tmp = ranges

with open("input.txt", "r") as file:
    for l in file:
        line = l.strip()
        if line == "":
            tmp = ingredients
            continue
        tmp.append(line)

fresh = []
for i in ingredients:
    if is_in_range(ranges, int(i)):
        fresh.append(i)

print(len(fresh))