import matplotlib.pyplot as plt
import time
import math

def millis():
    return time.time_ns() // 1_000_000

data = input().split()
# data = "0 1 1 0 2 0 3 0 4 5 5 62 6 687 7 7719".split()
n_elements = list(map(int, data[::2]))
cpp_time = list(map(int, data[1::2]))

py_time = list()
d = dict()

for i in range(8):
    d.clear()
    n = pow(10,i)
    start = millis()
    for j in range(n):
        d[j]=24
    py_time.append(millis()-start)
    

plt.figure()
plt.plot(n_elements, cpp_time, label = "C++")
plt.plot(n_elements, py_time, label = "Python")
plt.xlabel("2*10^i bite")
plt.ylabel("millis")
plt.legend()
plt.show()