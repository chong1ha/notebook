"""
그리디
[2141] 우체국
(틀림)
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
    
    total_distance = sum(x * a for x, a in locations)
    
    avg_distance = total_distance / total_people
    
    min_distance = float('inf')
    post_office_location = None
    for location, people in locations:
        distance_to_post_office = abs(location - avg_distance) * people
        if distance_to_post_office < min_distance:
            min_distance = distance_to_post_office
            post_office_location = location
    
    print(post_office_location)


if __name__ == "__main__":
    main()
