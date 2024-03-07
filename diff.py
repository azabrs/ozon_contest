import sys

def fast_input():
	return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))

def fast_output(x):
    sys.stdout.write(str(x[0] - x[1]))

fast_output(fast_input())
