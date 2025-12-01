from collections import deque, Counter

answer = []
dial = [x for x in range(50,100)]
dial.extend([x for x in range(0,50)])
dq_dial = deque(dial)

def rotate_left(n):
    return dq_dial.rotate(n)

def rotate_right(n):
    return dq_dial.rotate(-n)

with open('input.txt', 'r') as f:
    for l in f:
        line = l.strip()
        side = line[0]
        num = int(line[1:])
        if side == 'L':
            rotate_left(num)
        else:
            rotate_right(num)
        answer.append(dq_dial[0])

c = Counter(answer)
print(c[0])
