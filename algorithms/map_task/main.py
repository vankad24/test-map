import matplotlib.pyplot as plt
import time
import math
import sys

def millis():
    return time.time_ns() // 1_000_000

data = input().split()
# data = "0 1 1 0 2 0 3 0 4 5 5 62 6 687 7 7719".split()
n_elements = list(map(int, data[::2]))
cpp_time = list(map(int, data[1::2]))
cpp_mem= list(map( lambda x: round( pow(10,x)*2*4/1024,2 ), n_elements )) #sizeof(int)*2*кол-во элементов в Кб

py_time = list()
py_mem = list()
d = dict()

for i in range(8):
    d.clear()
    n = pow(10,i)
    start = millis()
    for j in range(n):
        d[j]=24
    py_time.append(millis()-start)
    py_mem.append(round( sys.getsizeof(d)/1024 ,2 ))


plt.figure()
plt.subplot(121)# сколько всего строк графиков, сколько всего колонок, индекс в этих строках и колонках
plt.plot(n_elements, cpp_time, label = "C++")
plt.plot(n_elements, py_time, label = "Python")
plt.xlabel("10^i elements")
plt.ylabel("millis")
plt.legend()
plt.subplot(122)
plt.plot(n_elements, cpp_mem, label = "C++")
plt.plot(n_elements, py_mem, label = "Python")
plt.xlabel("10^i elements")
plt.ylabel("Kilobytes")
plt.show()