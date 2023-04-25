import sys
from interaction import *

print("Choose mode from list below:")
print(keys_to_str())
args = input().split()
k = args[0]
for key in keys:
    if k == key[0]:
        key[2](args[2:])
        exit(0)
print(f"key {k} not in list of available keys:")
print(keys_to_str())
