import os
import json


class JSONinfo:
    send_info = ""
    recieve_info = ""

    def __init__(self, send_file="RT_send_config.json", recieve_file="RT_recieve_config.json"):
        if os.path.isfile(send_file):
            with open(send_file, 'r') as file1:
                info1 = file1.read()
                info1 = json.loads(info1)
            self.send_info = info1
        else:
            raise Exception("{} Check File or File Location".format(send_file))

        if os.path.isfile(recieve_file):
            with open(recieve_file, 'r') as file2:
                info2 = file2.read()
                info2 = json.loads(info2)
            self.recieve_info = info2
        else:
            raise Exception(
                "{} Check File or File Location".format(recieve_file))
