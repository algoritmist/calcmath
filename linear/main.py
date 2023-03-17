import sys
from interaction import *

args = sys.argv
if len(args) == 1:
    print(get_info())
    exit(0)

k = args[1]
for key in keys:
    if k == key[0]:
        key[2](args[2:])
        exit(0)
print(f"key {k} not in list of available keys:")
print(keys_to_str())
