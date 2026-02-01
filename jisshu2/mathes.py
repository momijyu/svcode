from math import sqrt
def square(x):
    return x ** x

def factorian(n):
    if n == 1:
        return 1
    else:
        return n * factorian(n-1)

def calc_dist(x1, y1, x2, y2):
    return sqrt(pow(x2-x1,2)+pow(y2-y1,2))

print(calc_dist(0,0,10,0))