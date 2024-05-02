'''
그리디
[1026] 보물
'''

import sys

def main():
    
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    
    n = int(inputs[0])
    a_list = [int(i) for i in inputs[1].strip().split()]
    b_list = [int(i) for i in inputs[2].strip().split()]
    
    if len(a_list) != n:
        return
    if len(b_list) != n:
        return
    
    a_list.sort()
    b_list.sort(reverse=True)
    
    cnt = 0
    for i in range(n):
        cnt += a_list[i] * b_list[i]
    
    print(cnt)
    
    
if __name__=="__main__":
    main()