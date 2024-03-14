#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)
    sum = 0
    for i in range(1, nargs):
        sum += int(sys.argv[i])
    print(sum)
