import sys
import json

def fast_input(x):
    res = ""
    for _ in range(x):
        res += sys.stdin.readline().rstrip("\r\n") 
    return res

def fast_output(x):
    sys.stdout.write(str(x))
    sys.stdout.write("\n")
#size hack_size
def check_folder(dic):
    clear_size = 0
    hack_size = 0
    if 'folders' in dic:
        for folder in dic['folders']:
            temp = check_folder(folder)
            clear_size  += temp[0]
            hack_size   += temp[1]

    is_hack = 0
    if "files" in dic:
        for file in dic["files"]:
            if file.split('.')[-1] == 'hack':
                is_hack = 1
    else:
        return clear_size, hack_size
    if is_hack == 1:
        return 0, clear_size + hack_size + len(dic["files"])
    else:
        return len(dic['files']) + clear_size, hack_size

def test(n):
    #with open("input.json", "r") as read_file:
    l = fast_input(n)
    data = json.loads(l)
    res = check_folder(data)
    fast_output(res[1])

n = int(sys.stdin.readline().rstrip("\r\n"))
for _ in range(n):
    m = int(sys.stdin.readline().rstrip("\r\n"))
    test(m)