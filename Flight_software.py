from MIL_STD_1553_Simulation.Bus_Controller.BC_Simulator import Bus_Controller
from MIL_STD_1553_Simulation.Remote_Terminal.RT_Simulator import Remote_Terminal
from JSONdata import JSONinfo
import threading
import time
import csv
import os

RT_recieve_config = "RT_recieve_config.json"
RT_send_config = "RT_send_config.json"
RTs = ["RT_1"]
recieve_attributes = ["RT_address", "sub_address_or_mode_code", "word_count"]
send_attributes = ["RT_address", "sub_address_or_mode_code", "message"]
time_to_wait = 120

if __name__ == "__main__":
    try:
        JSONinfo()
        recieve_json = JSONinfo().recieve_info

        send_json = JSONinfo().send_info
        for RT in RTs:
            send_values = send_json[RT]
            recieve_values = recieve_json[RT]
            # print(send_values[send_attributes[0]],
            #      send_values[send_attributes[1]], 
            #      send_values[send_attributes[2]])
            # print(recieve_values[recieve_attributes[0]],
            #      recieve_values[recieve_attributes[1]], 
            #      recieve_values[recieve_attributes[2]])
            # bc_listener_thread = threading.Thread(
            #     target=Bus_Controller().start_listener)
            # bc_listener_thread.start()
            # rt_listener_thread = threading.Thread(
            #     target=Remote_Terminal().start_listener)
            # rt_listener_thread.start()
            bc_object = Bus_Controller()
            time.sleep(5)
            bc_object.send_data_to_rt(
                str(send_values[send_attributes[0]]), 
                str(send_values[send_attributes[1]]), 
                str(send_values[send_attributes[2]]))
            command_word_frame_sent_1 = bc_object.command_word_frame
            bc_object.command_word_frame = ""

            time.sleep(time_to_wait)

            bc_object.receive_data_from_rt(
                str(recieve_values[recieve_attributes[0]]), 
                str(recieve_values[recieve_attributes[1]]), 
                str(recieve_values[recieve_attributes[2]]))
            command_word_frame_sent_2 = bc_object.command_word_frame
            bc_object.command_word_frame = ""

    except KeyboardInterrupt:
        exit()
