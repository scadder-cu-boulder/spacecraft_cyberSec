Shared Memory Module
======

Design
------
This module uses two instances of tcpdump to capture packets of both direction (in and out). These captured packets are stored to a temporary shared queue to be later pushed on to the Shared Memory Space. While capturing the packets, the command words received from the bus controller side are prepended with the bit '1'. This is done so that it's easier for the security monitor to distinguish between an legitimate command word when compared with a spoofed to replayed one. After writing the data into the temporary queue, the code then pushes each packet on to the Shared Memory Space. Everytime, that is done, the last read address, last written address are compared and then updated accordingly. Once the code wirtes to the last available address in the memory space (0x40001ffc), it cycles back to the start of the address space (0x40000010) and the next cycle bit is set to '1'.

Block Diagram
------
![Function Block Diagram of Shared Memory Module](https://github.com/prgu6170/spacecraft_cyberSec/blob/master/Shared_Mem_Module/shared_mem_module.jpeg)

Running the Shared Memory Module
------
To start the Shared Memory Module, you must have the Bus_Controller and Remote_Terminal simulators already running. The code can be then launched by entering the Shared_Mem_Module directory and executing the following command
```
python queue.py
```
