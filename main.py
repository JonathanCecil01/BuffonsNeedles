import random
import math
import sympy as sp
import matplotlib.pyplot as plt

x, y = sp.symbols('x y')

SCREEN_HEIGHT = 10
SCREEN_WIDTH = 10

class Line:
    def __init__(self, pos):
        #self.length = SCREEN_LENGTH
        self.pos = pos



class Needle:
    def __init__(self):
        self.start = [random.randint(0,SCREEN_WIDTH-2), random.randint(0,SCREEN_HEIGHT-2)]
        self.slope= math.tan(random.randint(-90, 90))
        dist = 4
        eq1 = sp.Eq((y-self.start[1])/(x-self.start[0]), self.slope)
        eq2 = sp.Eq((y - self.start[1]) ** 2 + (x - self.start[0]) ** 2, dist)
        self.end = sp.solve([eq1, eq2], (x, y))[0]


def intersection(line, needle : Needle):
    #print(needle.start)
    if needle.start[0]>=line.pos and needle.end[0]<+line.pos:
        return True
    elif needle.start[0]<=line.pos and needle.end[0]>=line.pos:
        return True
    else:
        return False

count = []
lines = []
flag = 0
for i in range(0, 5):
    lines.append(Line(i*2))

for line in lines:
    plt.plot([-2, SCREEN_WIDTH+2], [line.pos, line.pos], color = 'black')

#plt.show()

for i in range(0, 100):
    needle = Needle()
    for line in lines:
        if intersection(line, needle):
            plt.plot([needle.start[0], needle.end[0]], [needle.start[1], needle.end[1]])
            count.append(1)
            flag = 1
            break
    if flag!=1:
        plt.plot([needle.start[0], needle.end[0]], [needle.start[1], needle.end[1]])
        count.append(0)
    flag = 0

ones = 0
zeroes = 0
for i in count:
    if i==1:
        ones+=1
    else:
        zeroes+=1
print(count)
print(ones)
print(zeroes)
print("Estimtaion of pi = ", 2*len(count)/(ones))

plt.show()