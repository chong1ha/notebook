'''
그리디
[19598] 최소 회의실 개수
'''

import sys
import heapq

def main():
    
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    
    n = int(inputs[0])
    meeting_room = [tuple(map(int, input.split())) for input in inputs[1:n+1]]
    
    if len(meeting_room) != n:
        return
    
    meeting_room.sort()
    
    heap = []
    for start, end in meeting_room:
        
        if heap and heap[0] <= start:
            heapq.heappop(heap)
            
        heapq.heappush(heap, end)
        
    print(len(heap))
    
    
if __name__=="__main__":
    main()