import sys

def fast_input():
	return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(x)
    sys.stdout.write("\n")

def high_load_system(tasks):
    state = "I"
    for task in tasks:
        match(state):
            case "I":
                if task == 'M':
                    state = task
                else:
                    return "NO"
            case "M":
                if task == "M":
                    return "NO"
                else:
                    state = task
            case "R":
                if task == 'C':
                    state = task
                else:
                    return "NO"
            case 'C':
                if task == 'M':
                    state = task
                else:
                    return "NO"
            case 'D':
                if task == 'M':
                    state = task
                else:
                    return "NO"
    return "YES" if state == 'D' else "NO"

n = int(fast_input())
for _ in range(n):
    fast_output(high_load_system(fast_input()))


