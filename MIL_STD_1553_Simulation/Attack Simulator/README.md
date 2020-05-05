#Attack Suite

> This code is meant to be run as a malicious remote terminal
> in order to help simulate an attacker on a spacecraft.


>Each attack is run separately and to run it you need to uncomment it one by one

1. Replay Attack

For this attack to run you need to have an already established
communication between the Remote Terminal and Bus Controller
<br>
There is a thread running that captures the packets and appends them to a buffer. This buffer has packets from the communication taking place since the script was active.
For the replay attack, the buffer is read and the packet is checked if it starts with the value '100' since that indicates either a command word or status word which is the initialization of communication. 
If the packet contains a '100' then the buffer is read and sent (replayed on the channel) until another packet with '100' is encountered after which the packets that have already been replayed are deleted.
The replay thread runs continuously until the thread is terminated by sleeping for 10 seconds in every cycle that it has run.

2. DoS Attack

This attack makes use of a fixed packet and floods the communication channel with it while disrupting communication and making most datawords and command words unreadable

3. Spoofing Attack

This function generates a command word by choosing a random value of data words between 01-1F. It then broadcasts the command word and a remote terminal to which the packet corresponds with responds with the respective number of data words to the Bus Controller that never initiated the communication.


### List of functions
1. record_packets(self, data) - Appends the packet provided to it by the capture_packets function to a buffer called cycle_list.
2. capture_packets(self) - This function reads the communicattion packets from the channel and provides it as an argument by calling the record_packets function.
3. replay_attack(self) - This function utilizes the packets in the captured_packets buffer to perform a replay attack.
4. dos_attack(self) - This function utilizes the a fixed frame and uses the send_packet function to perform a dos_attack.
5. spoofing_attack(self) - This function generates a new command word every 20 seconds and performs a spoofing attack.
6. show_packets(self) - This function is used to append the packets from cycle_list to captured_list.
7. send_packet(self, message) - This function is used to broadcast a packet/messaage provided to it via its argument to the communication channel.

