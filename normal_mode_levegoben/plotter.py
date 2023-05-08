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
    for line in (f.readlines() [-200:]):
        floats = line.split(", ")
        if (left == []):
            k = float(floats[-3:][2])
        left.append(float(floats[-3:][0]))
        right.append(float(floats[-3:][1]))
        # plt.plot(float(floats[-3:][2]), float(floats[-3:][0]), 'o', color='blue')
        # plt.plot(float(floats[-3:][2]), float(floats[-3:][1]), 'o', color='blue')
    if (k>10):
        break

    left_avg = sum(left)/len(left)    
    right_avg = sum(right)/len(right)

    if (k>2.4):
        if (left_avg > 0 and right_avg < 0):
            left_torque.append(left_avg)
            right_torque.append(right_avg)
        elif (left_avg < 5.0 and right_avg != 0):
            left_torque.append(right_avg)
            right_torque.append(-right_avg)
        elif (right_avg < 5.0 and left_avg != 0):
            left_torque.append(left_avg)
            right_torque.append(-left_avg)
        elif (left_avg > 0 and right_avg > 0):
            left_torque.append(left_avg)
            right_torque.append(-right_avg)
        elif (left_avg < 0 and right_avg > 0):
            left_torque.append(left_avg)
            right_torque.append(right_avg)
        elif (left_avg < 0 and right_avg < 0):
            left_torque.append(left_avg)
            right_torque.append(-right_avg)
        elif (right_avg == 0 and left_avg == 0):
            left_torque.append(left_avg)
            right_torque.append(right_avg)
    else:
        left_torque.append(left_avg)
        right_torque.append(right_avg)
    
    ks.append(k)

# plt.grid()
plt.xlabel("k")
plt.ylabel("M[%]")
plt.scatter(ks, left_torque, color='blue')
plt.scatter(ks, right_torque, color='blue')

plt.savefig("plot_levegoben_.png")