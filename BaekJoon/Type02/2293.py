"""
다이나믹 프로그래밍
[2293] 동전 1

3 10 (n줄, k의 가치)
1
2
5

10
"""

import sys


def main():
    
    n, k = map(int, sys.stdin.readline().strip().split())
    coin = [int(sys.stdin.readline().strip()) for _ in range(n)]
    
    coin.sort()
    
    dp = [0] * (k + 1)
    dp[0] = 1
        
    for c in coin:
        
        for i in range(c, k+1):
            dp[i] += dp[i - c]
            
    print(dp[k])
    
    
if __name__=="__main__":
    main()