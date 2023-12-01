#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    n_args = len(sys.argv)
    result = 0
    if n_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        for x in range(1, n_args):
            if sys.argv[2] == '+':
                result = add(int(sys.argv[1]), int(sys.argv[3]))
            elif sys.argv[2] == '-':
                result = sub(int(sys.argv[1]), int(sys.argv[3]))
            elif sys.argv[2] == '*':
                result = mul(int(sys.argv[1]), int(sys.argv[3]))
            elif sys.argv[2] == '/':
                result = div(int(sys.argv[1]), int(sys.argv[3]))
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], result))
