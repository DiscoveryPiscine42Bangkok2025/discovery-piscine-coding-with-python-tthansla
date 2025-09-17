import sys

args = sys.argv[1:]
if len(args) != 1:
    print("none")
    raise SystemExit

s = args[0]
cnt = s.count('z')          
print('z' * cnt if cnt else "none")
