'''
Developer: Krishna Kumar
Language: Python (3.10.12)
Description: Help me to see CPU Temperature for different cores.
Date: 3-07-2024
'''

import psutil
import matplotlib.pyplot as plt
import time

t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
x = []
for i in range(100):
    a = psutil.sensors_temperatures()
    t1.append(a['coretemp'][0][1])
    t2.append(a['coretemp'][1][1])
    t3.append(a['coretemp'][2][1])
    t4.append(a['coretemp'][3][1])
    t5.append(a['coretemp'][4][1])
    x.append(i)
    time.sleep(0.01)


flag=0
while(flag<20):
    flag = flag + 1
    a = psutil.sensors_temperatures()
    t1.append(a['coretemp'][0][1])
    t2.append(a['coretemp'][1][1])
    t3.append(a['coretemp'][2][1])
    t4.append(a['coretemp'][3][1])
    t5.append(a['coretemp'][4][1])
    if(len(t1)>100):
        t1.pop(0)
        t2.pop(0)
        t3.pop(0)
        t4.pop(0)
        t5.pop(0)
    plt.figure("CPU Temperature Vs Time Graph")
    plt.ylabel("Temperature (in *C)")
    plt.xlabel("Time (in s)")
    plt.ylim(0, 90)
    plt.plot(x, t1, 'r')
    plt.plot(x, t2, 'y')
    plt.plot(x, t3, 'g')
    plt.plot(x, t4, 'b')
    plt.plot(x, t5, 'c')
    plt.legend(["core 1", "core 2", "core 3", "core 4", "core 5"])  #, loc="lower right")
    plt.draw()
    plt.pause(0.5)
    plt.clf()

print("Thank You for using this application.")
