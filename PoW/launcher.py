#!/usr/bin/env python3

import time
import os

start = time.time()
os.system("./full_execution.py 10000")
end = time.time()
print ("Total Execution time: ", end - start)
