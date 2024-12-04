"""
그리디
[13164] 행복유치원
"""

import sys

def main():
    
    n, k = map(int, sys.stdin.readline().strip().split())
    height_list = [int(x) for x in sys.stdin.readline().strip().split()]
    
    diff = [height_list[i + 1] - height_list[i] for i in range(n - 1)]
    diff.sort()

    cost = sum(diff[:n - k])
    print(cost)
    
    
if __name__=="__main__":
    main()