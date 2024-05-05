'''
그리디
[19598] 최소 회의실 개수

시간초과로 인해
'''

import sys

def main():
    
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    
    n = int(inputs[0])
    meeting_room = [tuple(map(int, input.split())) for input in inputs[1:n+1]]
    
    if len(meeting_room) != n:
        return
    
    meeting_room.sort()
    
    tmp_list = []
    for start, end in meeting_room:
        
        exists = False
        for i in range(len(tmp_list)):
        
            if tmp_list[i] <= start:
                tmp_list[i] = end
                exists = True
                break
            
        if not exists:
            tmp_list.append(end)
    
    print(len(tmp_list))
    
if __name__=="__main__":
    main()