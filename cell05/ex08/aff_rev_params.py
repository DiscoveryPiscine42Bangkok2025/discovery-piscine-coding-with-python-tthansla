import sys

a = sys.argv[1:]          
if len(a) < 2:
    print("none")
else:
    for b in reversed(a):
        print(b)
