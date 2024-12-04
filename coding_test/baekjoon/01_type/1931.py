"""
그리디
[1931] 회의실 배정
"""

import sys


def main():
    
    inputs = sys.stdin.read().strip().split('\n')
    
    n = int(inputs[0])
    meeting_room = [tuple(map(int, x.split())) for x in inputs[1:n+1]]
    meeting_room.sort(key=lambda x: (x[1], x[0]))
    
    cnt = 0
    end_time = 0
    for start, end in meeting_room:
        
        if end_time <= start:
            cnt += 1
            end_time = end
    
    print(cnt)
    
    
if __name__=="__main__":
    main()