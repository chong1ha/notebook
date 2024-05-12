"""
그리디
[1493] 박스 채우기
(런타임 에러, RecursionError)
"""

class CubeInfo:
    
    def __init__(self):
        self.length = 0
        self.cnt = 0


cubes = []

cnt = 0
is_fail = False

def solve(l, w, h, idx):
    
    global cnt, is_fail

    if l == 0 or w == 0 or h == 0:
        return

    for i in range(idx, -1, -1):
    
        if cubes[i].cnt <= 0:
            continue

        if l < cubes[i].length or w < cubes[i].length or h < cubes[i].length:
            continue


        cubes[i].cnt -= 1
        cnt += 1

        # cube_size (a, a, a), 3개로 분할 가능
        # (a, w-a, a)
        solve(cubes[i].length, w - cubes[i].length, cubes[i].length, i)
        # (l-a, w, a)
        solve(l - cubes[i].length, w, cubes[i].length, i)
        # (l, w, h-a)
        solve(l, w, h - cubes[i].length, i)

        return

    is_fail = True


if __name__ == "__main__":
    
    l, w, h = map(int, input().split())
    n = int(input())

    for _ in range(n):
        cude_idx, cude_cnt = map(int, input().split())

        cube_info = CubeInfo()
        cube_info.length = 1 << cude_idx
        cube_info.cnt = cude_cnt

        cubes.append(cube_info)


    solve(l, w, h, n-1)

    if is_fail:
        print("-1")
    else:
        print(cnt)
