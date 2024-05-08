"""
그리디
[1449] 수리공 항승
"""

import sys

def main():
    
    n, l = map(int, sys.stdin.readline().strip().split())
    leak_list = [int(x) for x in sys.stdin.readline().strip().split()]
    
    if len(leak_list) != n:
        return
    
    leak_list.sort()

    cnt = 0
    start = 0
    for i in leak_list:

        if start < i:
            start = i + l - 1
            cnt += 1

    print(cnt)
    
    
if __name__=="__main__":
    main()