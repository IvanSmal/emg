import serial
from serial.tools import list_ports
import matplotlib.pyplot as plt
import numpy as np
import time

# Below is code to auto find arduino port
ports = list(list_ports.comports())

if len(ports) < 1:
    raise IOError("No Arduino Found")

ard_ports=[]

for p in ports:
    if "Arduino" in p.description:
        ard_ports=p.device
        print('Arduino in port: '+ ard_ports)
    else:
        raise IOError("No Arduino Found")

# open correct serial port and read the data
try:
    ser = serial.Serial(ard_ports,9600)
except:
    print("Unable to access port: " + ard_ports + '\n' + "Try restarting the system.")
    exit()

fig, ax= plt.subplots()

toPlot=[]
toPlot[1:100]=np.zeros(100, dtype=int)
i=0
try:
    while i<100:
        data = ser.readline()
        toPlot.append(float(data.decode()))
        plt.cla()
        ax.plot(list(range(1,101)), toPlot[-101:-1])  # pyplot will add this data
        ax.set_ylim(1,1000)
        plt.draw()  # update plot
#        plt.pause(0.0000001)  # pause
        time.sleep(0.001)
        i=i+1
        print('looping')

except:
    ser.close()
    print("serial connection closed")
    plt.close()

ax.plot(toPlot)