"""
다이나믹 프로그래밍
[2201] 이친수 찾기

0 으로 시작 X
1이 연속 2번 나타나지 X

K번째 이친수 찾기

7

1010
(시간초과)
"""

import sys


def main():
    
    k = int(sys.stdin.readline().strip())
    
    idx = 0
    while True:
        
        value = bin(idx)[2:]
        idx += 1
        
        if value.startswith('0'):
            continue
        
        if '11' in value:
            continue
        
        k -= 1
                
        if (k == 0):
            print(value)
            break
    
    
if __name__=="__main__":
    main()