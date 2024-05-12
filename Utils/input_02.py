"""
활용
"""

import sys


def test_01():
    """ (여러 줄)
    3 4 5
    2
    1 2
    3 4 
    """
    
    # input
    l, w, h = map(int, input().split())
    n = int(input())
    tmp_list_input = [list(map(int, input().split())) for _ in range(n)]
    print("input 함수 사용 결과:", tmp_list_input)
    
    # sys
    l, w, h = map(int, sys.stdin.readline().strip().split())
    n = int(sys.stdin.readline().strip())
    tmp_list_sys = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    print("sys 함수 사용 결과:", tmp_list_sys)


def test_02():
    """ (한번에)
    3 4 5
    2
    1 2
    3 4 
    """
    
    # input 함수 사용
    l, w, h = map(int, input().split())
    n = int(input())
    tmp_list_input = [list(map(int, input().split())) for _ in range(n)]
    print("input 함수 사용 결과:", tmp_list_input)
    
    # sys 함수 사용
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    l, w, h = map(int, inputs[0].split())
    n = int(inputs[1])
    tmp_list_sys = [list(map(int, x.split())) for x in inputs[2:]]
    print("sys 함수 사용 결과:", tmp_list_sys)


if __name__ == "__main__":
    #test_01()
    test_02()
