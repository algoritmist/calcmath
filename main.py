from iterations import solve
import numpy as np
import sys
from interaction import *

# A = np.matrix('4 0.24 -0.08; 0.09 3 -0.15; 0.04 -0.08 4.0')
# b = np.array([8, 9, 20])

args = sys.argv
if len(args) == 1:
    print(get_info())
    exit(0)

mode = args[1]
if mode == '-i':
    run_interactive()
