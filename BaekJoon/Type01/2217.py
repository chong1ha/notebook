'''
그리디
[2217] 로프
'''

import sys

def main():
    
    n = int(sys.stdin.readline().strip())
    roop_weight_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
    roop_weight_list.sort(reverse=True)
    
    max_weight = 0
    for i, w in enumerate(roop_weight_list):
        
        cur_weight = w * (i+1)
        if max_weight < cur_weight:
            max_weight = cur_weight
        
    print(max_weight)   

    
if __name__=="__main__":
    main()