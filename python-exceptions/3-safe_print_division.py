#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        restart = a / b
    except Exception:
        restart = None
    finally:
            print("Inside result: {}".format(restart))
            return (restart)
