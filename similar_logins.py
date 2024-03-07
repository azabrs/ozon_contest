import sys


def fast_input(n):
	return [sys.stdin.readline().rstrip("\r\n") for _ in range(n)]

def fast_output(x):
    sys.stdout.write(x)
    sys.stdout.write("\n")

def similar_logins(empls, cands):
    dic_cand = {}
    for i in cands:
        dic_cand[i] = '0'
    count = 0
    for empl in empls:
        
        count += 1
        if count == 96:
            print(123)
        if empl in dic_cand:
            dic_cand[empl] = '1'
            continue
        i = -1
        for i in range(len(empl) - 2):
            test = ''.join([empl[:i], empl[i + 1], empl[i], empl[i + 2:]]) 
            if test in dic_cand:
                dic_cand[test] = '1'
        i += 1
        if len(empl) > 1 and empl[:i] + empl[i + 1] + empl[i] in dic_cand:
            dic_cand[empl[:i] + empl[i + 1] + empl[i]] = '1'
    for i in cands:
        fast_output(dic_cand[i])  


similar_logins(fast_input(int(sys.stdin.readline().rstrip("\r\n"))), fast_input(int(sys.stdin.readline().rstrip("\r\n"))))

