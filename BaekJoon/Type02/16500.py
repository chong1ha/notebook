"""
다이나믹 프로그래밍
[16500] 문자열 판별

100 이하인 문자열 S(소문자로 이루어진 문자열)
A(단어목록)에 포함된 문자열의 개수 N(1 ≤ N ≤ 100)
셋째 줄부터 N개의 줄에는 A에 포함된 단어가 한 줄에 하나씩 

softwarecontest
2
software
contest

1 (A에 포함된 문자열로 S를 만들 수 있으면 1, 없으면 0을 출력)

dp[len(s)]
"""

import sys

def main():
    
    s = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    words = [sys.stdin.readline().strip() for _ in range(n)]
    
    N = len(s)
    dp = [0] * (N+1)
    dp[0] = 1
    
    for i in range(N+1):
        
        if dp[i]:
            for word in words:
                
                if s[i:i+len(word)] == word:
                    dp[i+len(word)] = 1
        
    print(1 if dp[N] else 0)


if __name__=="__main__":
    main()