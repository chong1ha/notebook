"""
다이나믹 프로그래밍
[1463] 1로 만들기

2 -> 1
10 -> 3

X가 3으로 나누어 떨어지면, 3으로 나눈다
X가 2로 나누어 떨어지면, 2로 나눈다
1을 뺀다
연산을 사용하는 횟수의 최솟값

dp[4] = 2
dp[5] = 3 (2 + 1)
dp[6] = 2 
dp[7] = 3
dp[8] = 
dp[9] = 2
dp[10] = 3
"""

import sys

def main():
    
    n = int(sys.stdin.readline().strip())
    
    dp = [0] * 10000001
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1 
     
    for i in range(4, n+1):
        
        dp[i] = dp[i-1] + 1
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

    print(dp[n])


if __name__=="__main__":
    main()