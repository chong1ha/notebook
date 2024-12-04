"""
그리디
[15748] Rest Stops
"""

import sys


def main():
    
    inputs = sys.stdin.read().strip().split('\n')
    
    l, n, r_f, r_b = map(int, inputs[0].split())
    rest_stop_list = [tuple(map(int, x.split())) for x in inputs[1:n+1]]
    rest_stop_list.sort(key=lambda x: (-x[1], x[0]))
    
    diff = r_f - r_b
    
    cnt = 0
    cur_loc = 0
    for x, c in rest_stop_list:
        
        if cur_loc < x:
            dist = x - cur_loc
            cnt += diff * dist * c
            cur_loc = x
    
    print(cnt)
    
    
if __name__=="__main__":
    main()