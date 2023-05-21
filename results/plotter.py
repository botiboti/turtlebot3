import matplotlib.pyplot as plt
import numpy as np

f = open("beta_neg3.txt", "r")
secs = []
phis = []

for line in (f.readlines()):
    floats = line.split(" ")
    secs.append(float(floats[0]))
    phis.append(float(floats[-1]))

plt.xlabel("t(s)", fontsize=18)
plt.ylabel("Phi(rad)", fontsize=18)
plt.scatter(secs, phis, color='purple')
# plt.legend()
plt.savefig("beta_neg3.png")