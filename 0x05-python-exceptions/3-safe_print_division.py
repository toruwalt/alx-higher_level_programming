#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, OverflowError, ValueError, FloatingPointError):
        result = None
    finally:
        print(f'Inside result: {result}')
    return result
