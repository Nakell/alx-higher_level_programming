#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv) - 1
    if nargs == 0:
        print("0 arguments.")
    elif nargs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nargs))
    for i in range(1, len(sys.argv)):
        print("{:d}:".format(i), str(sys.argv[i]))
