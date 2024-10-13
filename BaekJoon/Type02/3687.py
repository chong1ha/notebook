"""
다이나믹 프로그래밍
[3687] 성냥개비

(2 ≤ n ≤ 100)
숫자 1 = 2개
숫자 2 = 5개
숫자 3 = 5개
숫자 4 = 4개
숫자 5 = 5개
숫자 6 = 6개
숫자 7 = 3개
숫자 8 = 7개
숫자 9 = 6개
숫자 0 = 6개
가장 작은 수와 가장 큰 수를 출력

4
3
6
7
15

7 7
6 111
8 711
108 7111111

아무리 많아도 한자리수가 가질수있는 갯수는 7개 (최소 2개)
dp[1] = 0, 0
dp[2] = 1, 1
dp[3] = 7, 7
dp[4] = 4, 11
dp[5] = 2, 71
dp[6] = 6, 111
dp[7] = 8, 711
dp[8] = 10

"""

def main():
    
    n = int(input().strip())
    matchsticks = [int(input().strip()) for _ in range(n)] 
    
    min_dp = [float('inf')] * 101
    min_dp[:9] = [0, 0, 1, 7, 4, 2, 6, 8, 10]
    
    # min
    for cnt in range(9, 101):
        for i in range(2, 8):
            
            if i != 6:
                min_dp[cnt] = min(min_dp[cnt], min_dp[cnt-i]*10 + min_dp[i])
            else:
                min_dp[cnt] = min(min_dp[cnt], min_dp[cnt-i]*10)
    
    # max
    for m in matchsticks:
        
        if m == 0:
            print("0 0")
            continue
        
        max_v = ('7' if m % 2 else '1') + '1' * (m // 2 - 1)
        print(min_dp[m], max_v)
    

if __name__=="__main__":
    main()