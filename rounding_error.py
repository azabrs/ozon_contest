import sys
import math as ma

def fast_input(x):
	return [float(sys.stdin.readline().rstrip("\r\n")) for _ in range(x)]

def fast_output(x):
    if x < 0:
        x =  x * -1
    sys.stdout.write("{:.2f}".format(x))
    sys.stdout.write("\n")
def rounding_error(prices, p):
    res = 0.0
    for price in prices:
        temp = float(price) * (float(p) / 100)
        res = res + temp - int(temp + 0.0001)
    return res

n = int(sys.stdin.readline().rstrip("\r\n"))


for _ in range(n):
    m, p = list(map(int, sys.stdin.readline().rstrip("\r\n").split()))
    fast_output(rounding_error(fast_input(m), float(p)))


