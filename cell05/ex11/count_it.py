import sys

a = sys.argv[1:]         
if not a:
    print("none")
else:
    print(f"parameters: {len(a)}")
    for s in a:
        print(f"{s}: {len(s)}")