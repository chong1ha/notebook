
# input() vs sys.stdin.readline()


## input()
- 내장함수, prompt message를 parameter로 받을 수 있음.
- 사용 예: `input("Enter a value: ")`
- 입력받은 값의 개행 문자를 자동으로 삭제하고 반환함.
    - 개행문자는 입력의 종료를 나타냄
    - 입력을 문자열로 변환하고, 개행문자를 제거한 뒤 값을 반환

## sys.stdin.readline()
- sys 모듈의 메서드이며, prompt message를 인수로 받지 X
- 표준 입력(stdin)에서 한 줄씩 데이터를 읽어옴
    - 이때, 표준 입력은 사용자로부터 받은 입력을 담고 있는 버퍼를 가르킴
- 사용하기 위해 sys 모듈을 임포트해야 함.
    - `import sys`
- 입력 받은 값을 그대로 반환하므로, 개행 문자를 포함함.
    - `hello를 입력하고 엔터 누르면, 실제론 hello\n`
- 주로 대량의 데이터를 처리할 때 효율적.
    - `input()`함수는 각 호출마다 입출력 오버헤드가 발생 (성능 저하)
    - `sys`는 한번에 읽어와 버퍼에 저장


## 정리 
- `input()` 간편하고 직관적, 임포트없이 사용가능해서 사용하기 편함
- `sys.stdin.readline()` 한 번 호출하면 한 줄씩 모두 읽어올 수 있어 대용량 데이터 처리에 효율적
- `sys.stdin.read()` 표준 입력(stdin)에서 지정된 바이트 수만큼 데이터를 읽어옴
- `input()` 과 `sys.stdin.readline()` 모두 사용자의 입력을 버퍼에 저장
- `sys.stdin.readline()` 더 빠른 이유는, 사용자의 입력이 한 줄로 끝날 때까지 버퍼를 모두 읽어온 뒤 값을 반환하기에
    - `input()`은 사용자의 입력이 종료될때까지(엔터 누를때까지) 버퍼를 계속 읽기에 (계속 대기하기에) 많은 입력이 발생하는 경우 대기 시간이 길어짐

## 정리2
- `sys.stdin.readline()`은 단 한번의 호출로 여러줄의 입력을 처리
- `input()`은 여러 줄을 입력할 경우, 여러번 호출 (오버헤드 발생)
    ```python
    1
    11 11
    11 11 11

    호출 시, input()은 3번 호출
    호출 시, sys.stdin.readline()은 1번 호출

    inputs = [input() for _ in range(3)]
    inputs = [sys.stdin.readline().strip() for _ in range(3)]
    ```

## 정리3
- 코테 입력 크기가 엄청 크진않으니, input() 쓰기가 편함

## 사용 예시
- 사용자로부터 한 줄을 입력받을 때: `input()`
    ```python
    user_input = input("Enter a value: ")
    print("Input:", user_input)
    ```
- 대량의 데이터를 한 번에 입력받을 때: `sys.stdin.readline()`
    ```python
    import sys
    # 입력 받은 데이터를 문자열로 반환
    data = sys.stdin.readline().strip() 
    print("Data:", data)
    ```


