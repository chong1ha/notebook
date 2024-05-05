'''
그리디
[14916] 거스름돈
'''

import sys

def main():
    
    n = int(sys.stdin.readline().strip())
    
    cnt = 0
    while True:
        
        if (n % 5) == 0:
            cnt += (n // 5)
            break
        
        n -= 2
        cnt += 1
        
        if (n < 0):
            print(-1)
            return
        
    print(cnt)
    
    
if __name__=="__main__":
    main()