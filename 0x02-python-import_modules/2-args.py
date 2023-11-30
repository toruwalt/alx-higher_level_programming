#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n_args = len(sys.argv)
    print("{} arguments".format(n_args - 1))
    for x in range(1, n_args):
        print("{}: {}".format(x, sys.argv[x]))
