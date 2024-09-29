"""
다이나믹 프로그래밍
[2201] 이친수 찾기

0 으로 시작 X
1이 연속 2번 나타나지 X

K번째 이친수 찾기

7

1010
"""

import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)

cache = {0: ['0'], 1: ['1'], 2: ['1', '0'], 3: ['1', '0', '0'], 4: ['1', '0', '1']}

an = [0, 1] 
sn = [0]   

cur = 1
for i in range(99):
    an.append(an[cur] + an[cur - 1])  
    cur += 1

cur = 1
for i in range(99):
    sn.append(sn[cur - 1] + an[cur])  
    cur += 1

def dp(n):
    if n in cache:
        return cache[n]

    length = 0
    for i in range(len(sn)):
        if n <= sn[i]:
            length = i
            break

    count = an[length] 
    prevCount = an[length - 1] 

    temp = dp(n - count - prevCount)

    aux = ['1', '0']
    for i in range(length - 2 - len(temp)):
        aux.append('0')

    cache[n] = aux + temp
    return cache[n]

def main():
    k = int(sys.stdin.readline().strip())
    result = "".join(dp(k))
    print(result)

if __name__ == "__main__":
    main()