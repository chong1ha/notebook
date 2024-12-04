'''
그리디
[2170] 선긋기
'''

import sys

def main():
    
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    
    n = int(inputs[0])
    pairs = [tuple(map(int, input.strip().split())) for input in inputs[1: n+1]]
    pairs.sort()
    
    tmp_list = []
    x_p, y_p = pairs[0]
    
    for x, y in pairs[1:]:
        
        if x <= y_p:
            y_p = max(y, y_p)
        else:
            tmp_list.append((x_p, y_p))
            x_p, y_p = x, y
    
    tmp_list.append((x_p, y_p)) 
    
    print(sum(y-x for x, y in tmp_list))
    
    
if __name__=="__main__":
    main()