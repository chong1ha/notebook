'''
그리디
[11399] ATM
'''

import sys

def main():
    
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    
    n = int(inputs[0])
    tmp_list = [int(x) for x in inputs[1].split()]
    
    if len(tmp_list) != n:
        return
    
    tmp_list.sort()
    
    cnt = 0
    total = 0
    for time in tmp_list:
        cnt += time
        total += cnt
    
    print(total)
        

if __name__=="__main__":
    main()