'''
그리디
[4796] 캠핑
'''

import sys

def main():
    
    i = 1
    while True:
        
        l, p, v = map(int, sys.stdin.readline().strip().split())

        if l==0 and p==0 and v==0:
            break
        
        q, r = divmod(v, p)
        
        print(f'Case {i}: {q * l + min(r, l)}')
        i += 1

    
if __name__ == "__main__":
    main()