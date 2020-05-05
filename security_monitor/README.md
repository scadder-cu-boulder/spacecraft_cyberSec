# Security Monitor

Security monitor runs continuously to check if there is a new value written in the shared memory. It uses LAST_READ_MEM, LAST_WRITTEN_MEM, and NEXT_CYCLE memory addresses to keep track of what it has read previously, which memory to read and when to cycle back to the first address. Each time it reads a memory address, security_monitor calls a function and passes this information to it. This function is responsible for identifying attacks using the logic shown below. 

Below is the block diagram for security monitor implementation.

![alt text](https://github.com/prgu6170/spacecraft_cyberSec/blob/master/security_monitor/security_monitor.jpeg)

DoS attacks are detected of the received packet count is much greater than expected. So the security monitor for detects it as Replay attacks and then escalates the warning to DoS.
