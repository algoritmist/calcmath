import warnings

warnings.filterwarnings("ignore")

import equation_test
import system_test

print("Test equations:")
equation_test.test()
print("Test systems:")
system_test.test()
