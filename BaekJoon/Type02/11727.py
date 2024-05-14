"""
다이나믹 프로그래밍
[11727] 2×n 타일링 2
"""

import sys

def main():
    
    n = int(sys.stdin.readline().strip())
    
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(3)
        return
    elif n == 3:
        print(5)
        return
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5
    
    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
            
    print(dp[n])
    

if __name__=="__main__":
    main()
