"""
다이나믹 프로그래밍
[12865] 평범한 배낭

N개의 물건 = 무게 W와 가치 V
최대 K만큼의 무게만을 넣을 수 있는 배낭이 존재
최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값

냅색 알고리즘

물품의 수 N(1 ≤ N ≤ 100)
버틸수 있는 무게 K(1 ≤ K ≤ 100,000)
각 물건의 무게 W(1 ≤ W ≤ 100,000)
물건의 가치 V(0 ≤ V ≤ 1,000)

4 7
6 13
4 8
3 6
5 12

14
"""

import sys

def main():
    
    n, k = map(int, sys.stdin.readline().strip().split())
    wv = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        
        for j in range(1, k+1):
            w = wv[i][0]
            v = wv[i][1]
            
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
    
    print(dp[n][k])



if __name__=="__main__":
    main()