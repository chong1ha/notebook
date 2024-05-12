"""
그리디
[2141] 우체국
"""

def main():
    
    n = int(input())
    locations = []
    total_people = 0
    for _ in range(n):
        x, a = map(int, input().split())
        locations.append((x, a))
        total_people += a
        
    locations.sort()
    
    answer = 0
    min_diff = float('inf')
    left = 0
    right = total_people
    for i in range(n):
        right -= locations[i][1]
        if min_diff > abs(right - left):
            answer = locations[i][0]
            min_diff = abs(right - left)
        left += locations[i][1]
    
    print(answer)
    

if __name__ == "__main__":
    main()
