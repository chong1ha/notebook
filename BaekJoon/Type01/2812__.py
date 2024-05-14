"""
그리디
[2812] 크게 만들기
(시간초과)
"""

import sys

def main():
    
    n, k = map(int, sys.stdin.readline().strip().split())
    num = sys.stdin.readline().strip()
    
    if len(str(num)) != n:
        return

    max_num = []
    start_index = 0
    for _ in range(n - k):
        max_index = start_index
        for i in range(start_index, n - k + 1):
            if num[i] > num[max_index]:
                max_index = i
        max_num.append(num[max_index])
        start_index = max_index + 1

    print(''.join(map(str, max_num)))


if __name__=="__main__":
    main()


if __name__=="__main__":
    main()