import sys
import re

a = sys.argv[1:]
if len(a) != 2:
    print("none")
    sys.exit(0)

keyword, text = a
if not keyword:  
    print("none")
    sys.exit(0)

count = len(re.findall(re.escape(keyword), text))

print(count if count > 0 else "none")