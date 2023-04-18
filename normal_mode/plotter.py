import matplotlib.pyplot as plt
import numpy as np
from os import walk
import re

# sorting key
def takeFloat(str):
    return float(str[2:])

# filtering and ordering files 
filenames = list(filter(lambda str: re.match('k_', str), next(walk("./"), (None, None, []))[2]))

filenames.sort(key=takeFloat)

# 
left_torque = []
right_torque = []
ks = []

# reading
for file in filenames:
    left = []
    right = []
    k = 0
    f = open(file, "r")
    for line in (f.readlines() [-1:]):
        floats = line.split(", ")
        if (left == []):
            k = float(floats[-3:][2])
        left.append(float(floats[-3:][0]))
        right.append(float(floats[-3:][1]))
    
    left_torque.append(sum(left)/len(left))
    right_torque.append(sum(right)/len(right))
    ks.append(k)

plt.xlabel("k")
plt.ylabel("M[%]")
plt.scatter(ks, left_torque, label='Left wheel')
plt.scatter(ks, right_torque, label='Right wheel')
plt.legend()
plt.savefig("plot.png")