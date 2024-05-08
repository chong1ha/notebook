"""
그리디
[2212] 센서
"""

import sys

def main():
    
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    
    n = int(inputs[0])
    k = int(inputs[1])
    coord_list = list(map(int, inputs[2].split()))
    
    if len(coord_list) != n:
        return
    
    coord_list.sort()
    
    diff = [coord_list[i+1] - coord_list[i] for i in range(n-1)]
    diff.sort(reverse=True)
    cost = sum(diff[k-1:])
    print(cost)
    
    
if __name__=="__main__":
    main()