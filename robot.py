import sys

def fast_input(n):
	return [list(sys.stdin.readline().rstrip("\r\n")) for _ in range(n)]
#f = open('output.txt','w')
def fast_output(x):

    for i in x:
        sys.stdout.write(''.join(i))
        sys.stdout.write("\n")

def robot(n, m, rows):
    first_r = []
    second_r = []
    for row in range(len(rows)):
        if 'A' in rows[row]:
            first_r = [row, rows[row].index('A'),'a']
        if 'B' in rows[row]:
            second_r = [row, rows[row].index('B'), 'b']
    max_ind = max(first_r, second_r, key=lambda x: (x[1], x[0]))
    min_ind = min(first_r, second_r, key=lambda x: (x[1], x[0]))
    if (min_ind[0] + 1) % 2 == 1:
        rows[min_ind[0]][:min_ind[1]] = min_ind[2] * min_ind[1]
        for i in range(min_ind[0]):
            rows[i][0] = min_ind[2]
    else:
        for i in range(min_ind[0]):
            rows[i][min_ind[1]] = min_ind[2]
        rows[0][:min_ind[1]] = min_ind[2] * min_ind[1]


    if (max_ind[0] + 1) % 2 == 1:
        if max_ind[1] + 1 != m:
            rows[max_ind[0]][max_ind[1] + 1:m] = max_ind[2] * (m - max_ind[1] - 1)
        if max_ind[0] + 1 != n:
            for i in range(max_ind[0] + 1, n):
                rows[i][m - 1] = max_ind[2]
    else:
        for i in range(max_ind[0] + 1, n):
            rows[i][max_ind[1]] = max_ind[2]
        rows[n - 1][max_ind[1]:] = max_ind[2] * (m - max_ind[1])
    return rows

t = int(sys.stdin.readline().rstrip("\r\n"))
for _ in range(t):
    n, m = list(map(int, sys.stdin.readline().rstrip("\r\n").split()))
    fast_output(robot(n, m, fast_input(n)))
