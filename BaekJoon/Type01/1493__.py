"""
그리디
[1493] 박스 채우기
(런타임 에러, TypeError)
"""

class Cube:
    def __init__(self):
        self.length = 0
        self.cnt = 0


def fill_boxes(l, w, h, cube_list):
    
    cnt = 0
    
    if l == 0 or w == 0 or h == 0:
        return
    
    for cube in cube_list:
        
        if cube.cnt <= 0:
            continue
        
        if l < cube.length or w < cube.length or h < cube.length:
            continue
    
        cube.cnt -= 1
        cnt += 1
        
        # 큐브(a, a, a), 3 분할 (a, w-a, a) (l-a, w, a) (l, w, h-a)
        cnt += fill_boxes(cube.length, w - cube.length, cube.length, cube_list)
        cnt += fill_boxes(l - cube.length, w, cube.length, cube_list)
        cnt += fill_boxes(l, w, h - cube.length, cube_list)

        return cnt


if __name__ == "__main__":
    
    l, w, h = map(int, input().split())
    n = int(input())

    cube_list = []
    for _ in range(n):
        cube_idx, cube_cnt = map(int, input().split())

        cube_info = Cube()
        cube_info.length = 2 ** cube_idx
        cube_info.cnt = cube_cnt

        cube_list.append(cube_info)


    cube_list.sort(key=lambda x: x.length, reverse=True)
    cnt = fill_boxes(l, w, h, cube_list)

    if cnt == -1:
        print("-1")
    else:
        print(cnt)
