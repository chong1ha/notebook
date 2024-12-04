"""
그리디
[1700] 멀티탭 스케줄링

2 7
2 3 2 3 1 2 7 = 2

2 9
1 2 3 1 2 3 1 2 3 = 4
"""

import sys


def main():
    
    n, k = map(int, sys.stdin.readline().strip().split())
    use_list = [int(x) for x in sys.stdin.readline().strip().split()]
    
    cnt = 0
    visit = set()
    future_use_index = {x: [] for x in set(use_list)}
    
    for i in range(k-1, -1, -1):
        future_use_index[use_list[i]].insert(0, i)
    
    for i in range(k):
        
        cur_device = use_list[i]
        
        if cur_device in visit:
            future_use_index[cur_device].pop(0)
            continue
        
        if len(visit) < n:
            visit.add(cur_device)
            future_use_index[cur_device].pop(0)
        else:
            
            last_index = -1
            last_device = None
            
            for j in visit:
                
                if not future_use_index[j]:
                    last_device = j
                    break
                
                next_use = future_use_index[j][0]
                if next_use > last_index:
                    last_index = next_use
                    last_device = j
            
            visit.remove(last_device)
            visit.add(cur_device)
            cnt += 1
            
            future_use_index[cur_device].pop(0)
        
    print(cnt)
            
    
if __name__=="__main__":
    main()