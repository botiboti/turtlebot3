import matplotlib.pyplot as plt
import numpy as np

f = open("omega2.txt", "r")
b = open("omega4.txt", "r")
c = open("omega6.txt", "r")
secs = []
phis = []
secs1 = []
phis1 = []
secs2 = []
phis2 = []

for line in (f.readlines()):
    floats = line.split(" ")
    secs.append(float(floats[0]))
    phis.append(float(floats[-1]))
for line in (b.readlines()):
    floats = line.split(" ")
    secs1.append(float(floats[0]))
    phis1.append(float(floats[-1]))
for line in (c.readlines()):
    floats = line.split(" ")
    secs2.append(float(floats[0]))
    phis2.append(float(floats[-1]))

plt.xlabel("t(s)", fontsize=18)
plt.ylabel("Phi(rad)", fontsize=18)
plt.scatter(secs, phis, color='red')
plt.scatter(secs1, phis1, color='blue')
plt.scatter(secs2, phis2, color='purple')

# plt.legend()
plt.savefig("const_omega.png")