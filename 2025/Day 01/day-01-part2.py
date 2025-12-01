from collections import deque, Counter

class Dial():
    
    dial = None
    answer = []
    zero_clicks = 0
    
    def __init__(self):
        self.dial = [x for x in range(50,100)]
        self.dial.extend([x for x in range(0,50)])
        self.dial = deque(self.dial)
        
    
    def rotate_left(self, n):
        for i in range(n):
            self.dial.rotate(1)
            if self.dial[0] == 0 and i != n-1:
                self.zero_clicks += 1
        self.answer.append(self.dial[0])

    def rotate_right(self, n):
        for i in range(n):
            self.dial.rotate(-1)
            if self.dial[0] == 0 and i != n-1:
                self.zero_clicks += 1
        self.answer.append(self.dial[0])
        
    def get_answer(self):
        return Counter(self.answer)[0] + self.zero_clicks

dial = Dial()

with open('input.txt', 'r') as f:
    for l in f:
        line = l.strip()
        side = line[0]
        num = int(line[1:])
        if side == 'L':
            dial.rotate_left(num)
        else:
            dial.rotate_right(num)

print(dial.get_answer())
