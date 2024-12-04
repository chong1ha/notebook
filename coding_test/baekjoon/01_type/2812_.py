"""
그리디
[2812] 크게 만들기
(시간초과)
"""

import sys

def main():

    n, k = map(int, sys.stdin.readline().strip().split())
    num = int(sys.stdin.readline().strip())
    
    if len(str(num)) != n:
        return

    digits = []
    for digit in str(num):
        digits.append(digit)

    stack = []
    remove_cnt = k
    for digit in digits:
        
        while stack and remove_cnt > 0 and stack[-1] < digit:
            stack.pop()
            remove_cnt -= 1
            
        stack.append(digit)
    
    result = stack[:n-k]
    print(''.join(result))


if __name__=="__main__":
    main()