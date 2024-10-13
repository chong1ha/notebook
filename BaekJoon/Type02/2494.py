"""
다이나믹 프로그래밍
[2494] 숫자 맞추기

3
326
446

4
1 1
2 1
3 -2

d[n][k] = n번째 숫자나사가 k번 왼쪽 회전한 상태

오른쪽, 왼쪽으로 돌릴때(밑에 까지 움직임)

오른쪽 = dp[n+1][k] + 왼쪽 회전 수
왼쪽 = dp[n+1][(k+오른쪽 회전 수 ) % 10] + 오른쪽 회전 수
"""

def main():
    
    n = int(input().strip())
    target = list(map(int, list(input().strip())))  
    goal = list(map(int, list(input().strip())))   
    
    dp = [[0] * 10 for _ in range(n+1)]    
    path = [[0] * 10 for _ in range(n+1)]

    for i in range(n):
        i = n-1-i
        for j in range(10):
            d = (goal[i] - target[i] - j) % 10
            left = dp[i+1][(j+d) % 10] + d
            right = dp[i+1][j] + (10 - d)
            
            if left < right:  
                dp[i][j] = left
                path[i][j] = d
            else:  
                dp[i][j] = right
                path[i][j] = d - 10
            
    print(dp[0][0])
    i = 0 
    for j in range(n):
        c = path[j][i]  
        print(j+1, c)  
        if c > 0: 
            i = (i+c) % 10


if __name__=="__main__":
    main()