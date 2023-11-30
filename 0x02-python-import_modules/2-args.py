#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n_args = len(sys.argv) - 1
    if n_args == 0:
        print("{} arguments.".format(n_args))
    elif n_args == 1:
        print("{} argument:".format(n_args))
    else:
        print("{} arguments:".format(n_args))

    for x in range(1, n_args + 1):
        print("{}: {}".format(x, sys.argv[x]))
