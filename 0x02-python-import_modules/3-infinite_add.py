#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    n_args = len(sys.argv)
    for x in range(1, n_args):
        sum = sum + int(sys.argv[x])

    print(sum)
