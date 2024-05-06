'''
그리디
[13305] 주유소
'''

import sys

def main():
    
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    
    n = int(inputs[0])
    dist_list = [int(i) for i in inputs[1].strip().split()]
    station_list = [int(i) for i in inputs[2].strip().split()]
    
    cost = 0
    min_price = station_list[0]
    for i in range(n-1):   
        
        cost += min_price * dist_list[i]
        
        if station_list[i+1] < min_price:
            min_price = station_list[i+1]
        
    print(cost)
    
    
if __name__=="__main__":
    main()