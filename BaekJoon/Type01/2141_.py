"""
그리디
[2141] 우체국
(런타임 에러, TypeError)
"""

import statistics

def main():
    
    n = int(input())
    tmp_list = [list(map(int, input().split())) for _ in range(n)]
    tmp_list.sort()    
    print(statistics.median(tmp_list)[0])
    

if __name__ == "__main__":
    main()
