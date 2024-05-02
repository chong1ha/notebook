'''
그리디
[11047] 동전 0
'''

import sys

def main():
    
    n, k = map(int, sys.stdin.readline().strip().split())
    
    money_arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
    money_arr.sort(reverse=True)
    
    cnt = 0
    for money in money_arr:
        
        if k >= money:
            q, r = divmod(k, money)
            cnt += q
            k = r
 
        if k == 0:
            break
        
    print(cnt)
    

    
    
    
    
if __name__ == "__main__":
    main()