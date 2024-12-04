'''
그리디
[13904] 과제
'''

import sys

def main():
    
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    
    n = int(inputs[0])
    task_list = [list(map(int, input.split())) for input in inputs[1:]]
    
    if len(task_list) != n:
        return
    
    task_list.sort(key=lambda x: x[1], reverse=True)
    
    visit_list = [False] * 1001
    cnt = 0
    for d, w in task_list:
        
        for day in range(d, 0, -1):
            
            if not visit_list[day]:
                visit_list[day] = True
                cnt += w
                break
            
    print(cnt)      
    
    
if __name__=="__main__":
    main()