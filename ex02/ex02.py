import sys

def multiply_all(*args: int) -> int:
    res = 1
    for arg in args:
        res *= arg
    return res

if __name__ == '__main__':
    print(multiply_all(1, 2, 3, 4, 5))