import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    for s in args:
        if not s.endswith("ism"):
            print(s + "ism")
