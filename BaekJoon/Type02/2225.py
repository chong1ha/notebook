"""
다이나믹 프로그래밍
[2225] 합분해

20 2 => 21
6 4 => 84

0부터 n까지 정수 k개를 더해 n을 만드는 방법

dp[0][0] = 1
dp[n][0] = 0
dp[0][k] = 1

dp[4][2] = (0, 4) (1, 3) (2, 2) (3, 1) (4, 0) = 5
dp[3][2] = (0, 3) (1, 2) (2, 1) (3, 0) = 4

dp[2][3] = (0, 0, 2) (0, 1, 1) (0, 2, 0) (2, 0, 0) (1, 0, 1) (1, 1, 0) = 6
dp[2][2] = (0, 2) (1, 1) (2, 0) = 3
dp[2][1] = (2) = 1

dp[1][1] = 1
dp[1][2] = 0

dp[n][k] = dp[n]
"""

import sys


def main():
    
    n, k = map(int, sys.stdin.readline().strip().split())
    
    # dp[0][0] ... dp[0][k]
    # .
    # .
    # .
    # dp[n][0] ... dp[n][k]
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for n in range(1, n+1):
        dp[n][0] = 0
    
    for k in range(1, k+1):
        dp[0][k] = 1
    
    for n in range(1, n+1):
        for k in range(1, k+1):
            # 나누는 것은 문제 요구사항 (오버플로)
            dp[n][k] = (dp[n-1][k] + dp[n][k-1]) % 1000000000
    
    print(dp[n][k])
    
if __name__=="__main__":
    main()