"""
리스트 받기
"""

import sys


def test_01():
    """ 리스트 컴프리렌션 사용 (입력을 여러 줄에 걸처 한번에 받아 처리, 사실상 리스트인것 빼면 각 줄 받아 처리)
    3
    1 3
    2 3
    3 3
    """
    
    # input
    n = int(input())
    tmp_list_input = [list(map(int, input().split())) for _ in range(n)]
    print("input 함수 사용 결과:", tmp_list_input)
    
    # sys
    n = int(sys.stdin.readline().strip())
    tmp_list_sys = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print("sys 함수 사용 결과:", tmp_list_sys)

def test_02():
    """ 리스트 컴프리렌션 사용없이 (입력을 여러 줄에 걸처 한번에 받아 처리, 사실상 리스트인것 빼면 각 줄 받아 처리)
    3
    1 3
    2 3
    3 3
    """
    
    # input
    n = int(input())
    tmp_list_input = []
    for _ in range(n):
        values = list(map(int, input().split()))
        tmp_list_input.append(values)
    print("input 함수 사용 결과:", tmp_list_input)
    
    # sys
    n = int(sys.stdin.readline().strip())
    tmp_list_sys = []
    for _ in range(n):
        values = list(map(int, sys.stdin.readline().split()))
        tmp_list_sys.append(values)
    print("sys 함수 사용 결과:", tmp_list_sys)


def test_03():
    """ (입력을 한 번에 받아 처리)
    3 
    1 3
    2 3
    3 3
    """
    # input 함수 사용
    n = int(input())
    task_list_input = [list(map(int, input().split())) for _ in range(n)]
    print("input 함수 사용 결과:", n, task_list_input)
    
    # sys  함수 사용 (read() EOF 종료시, ctrl+z 엔터 혹은 ctrl+d 엔터)
    input_data = sys.stdin.read().strip()
    inputs = input_data.split('\n')
    n = int(inputs[0])
    task_list_sys = [list(map(int, task.split())) for task in inputs[1:n+1]]
    print("sys 함수 사용 결과:", n, task_list_sys)


if __name__ == "__main__":
    #test_01()
    #test_02()
    test_03()
