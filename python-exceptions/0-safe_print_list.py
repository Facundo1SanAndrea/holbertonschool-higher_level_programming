#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    restart = 0
    for large in range(x):
        try:
            print(f"{my_list[large]}", end='')
            restart += 1
        except IndexError:
            print()
            return(restart)
    print()
    return (restart)
