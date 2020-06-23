import warnings
import serial
from serial.tools import list_ports

## Below is code to auto find arduino port
ports = list(list_ports.comports())

if len(ports) < 1:
    raise IOError("No Arduino Found")

ard_ports=[]

for p in ports:
    if "Arduino" in p.description:
        ard_ports=p.device
        print(ard_ports)
    else:
        raise IOError("No Arduino Found")
