"""
다이나믹 프로그래밍
[1149] RGB 거리

3
1 100 200
1 201 101
202 102 1

102
"""

import sys


def main():
    
    n = int(sys.stdin.readline().strip())
    rgb_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    
    dp = [[0]*3 for _ in range(n)]
    dp[0] = rgb_list[0]
    
    for idx in range(1, n):
        
        dp[idx][0] = rgb_list[idx][0] + min(dp[idx-1][1], dp[idx-1][2])
        dp[idx][1] = rgb_list[idx][1] + min(dp[idx-1][0], dp[idx-1][2])
        dp[idx][2] = rgb_list[idx][2] + min(dp[idx-1][0], dp[idx-1][1])

    print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
    
    
if __name__=="__main__":
    main()
