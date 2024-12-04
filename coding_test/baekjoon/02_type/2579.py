"""
다이나믹 프로그래밍
[2579] 계단 오르기

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있음
연속된 세 개의 계단을 모두 밟아서는 안됨 (단, 시작점은 계단에 포함 X)
마지막 도착 계단은 반드시 밟아야 함

(계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수)
(얻을 수 있는 총 점수의 최댓값을 출력)

6
10
20
15
25
10
20

75
"""

import sys

def main():
    
    cnt = int(sys.stdin.readline().strip())
    stairs = [int(sys.stdin.readline().strip()) for _ in range(cnt)]

    dp = [0] * 301
    
    if cnt == 1:
        dp[0] = stairs[0]
        print(dp[0])
        return
    
    if cnt == 2:
        dp[0] = stairs[0]
        dp[1] = stairs[0] + stairs[1]
        print(dp[1])
        return
    
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    
    for i in range(3, cnt):
        
        dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])
        
    print(dp[cnt-1])
        

if __name__=="__main__":
    main()