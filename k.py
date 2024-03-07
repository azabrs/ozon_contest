import sys
import time
start_time = time.time()
fo = open("output.txt", 'w')
f = open("input.txt", 'r')
def fast_input():
        
    return list(map(int, f.readline().rstrip("\r\n").split()))

def fast_output(x):
    fo.write(str(x))
    fo.write(" ")

def parce(dic, key, test_key):
    l = 0

    if test_key != 0 and (test_key not in dic):
        l += parce(dic, key, test_key - 1) + 1
        fast_output(1)
        return l + 1
    elif test_key == 0 and test_key == key - 1:
        fast_output(dic[key])
        return l + 1
    elif test_key == 0 or (test_key != key - 1 and test_key in dic):
        return l + 1
    fast_output(dic[key])
    return l

def k(seq, n):
    prev = seq[0]
    max_rep = cur_rep = 0
    dic_max_len = {}
    rise = 1 if len(seq) == 1 or seq[0] < seq[1] else 0
    diff =  0 
    diff_prev = -1
    count_rise = 0
    is_rise = 0
    count_down = 0
    for cur in range(1, len(seq)):
        if seq[cur] > prev and rise == 1:
            is_rise = 1
            rise = 1
            count_rise += 1
        elif rise == 1 and seq[cur] < prev:
            is_rise = 1
            count_down += 1
            rise = 0
        elif rise == 0 and seq[cur] > prev:
            if is_rise:
                diff = min(count_down, count_rise)
                
                #dic_max_len[diff_prev] = 0
                if (diff == diff_prev  and count_down >= count_rise) or diff_prev == -1:
                    cur_rep += 1
                else:
                    cur_rep = 1
                if diff not in dic_max_len or cur_rep > dic_max_len[diff]:
                    dic_max_len[diff] = cur_rep
                if count_down > count_rise:
                    cur_rep = 0
                diff_prev = diff
                count_down = count_rise = 0
            count_rise += 1
            rise = 1
            count_down = 0
        elif rise == 0 and seq[cur] < prev:
            count_down += 1
            rise = 0
        elif prev == seq[cur]:
            count_down = count_rise = 0
        prev = seq[cur]
    diff = min(count_down, count_rise)
    if (diff == diff_prev  and count_down >= count_rise) or diff_prev == -1:
        cur_rep += 1
    else:
        cur_rep = 1
    if diff not in dic_max_len or cur_rep > dic_max_len[diff]:
        dic_max_len[diff] = cur_rep 


    if 0 in dic_max_len:
        dic_max_len.pop(0)

    l = 0

    ordered_key = sorted(dic_max_len)

    for key in ordered_key:
        l += parce(dic_max_len, key, key - 1)
    finish = n 
    for i in range(l, finish):
        fast_output(0)

    return 0

n = int(f.readline().rstrip("\r\n"))
for _ in range(n):
    m = int(f.readline().rstrip("\r\n"))
    k(fast_input(), m)
    fast_output('\n')

            
print("--- %s seconds ---" % (time.time() - start_time))