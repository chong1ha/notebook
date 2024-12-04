"""
그리디
[11000] 강의실 배정
"""

import sys
import heapq


def main():
    
    inputs = sys.stdin.read().strip().split('\n')
    
    n = int(inputs[0])
    meeting_room = [tuple(map(int, x.split())) for x in inputs[1:n+1]]
    meeting_room.sort()
    
    heap = []
    for start, end in meeting_room:
        
        if heap and heap[0] <= start:
            heapq.heappop(heap)
    
        heapq.heappush(heap, end)
        

    print(len(heap))
    
    
if __name__=="__main__":
    main()