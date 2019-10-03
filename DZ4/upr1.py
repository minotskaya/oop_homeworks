import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('number', nargs='?')

    return parser

def fibonachi(n):
    a = [0]*(n)
    a[1] = 1
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2]
    return a[n-1]


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    n = int(namespace.number)

    print(fibonachi(n))
