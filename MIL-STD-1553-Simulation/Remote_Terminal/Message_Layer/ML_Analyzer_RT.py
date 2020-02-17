from Data_Link_Layer.Data_Link_Layer_Decoder_RT import DataLinkLayerDecoderRT
from Data_Link_Layer.Data_Link_Layer_Encoder_RT import DataLinkLayerEncoderRT


class MessageLayerAnalyzerRT:

    lookup_memory = {"01": "HA", "02": "NA"}

    def construct_data_word(self, data_wd_part):
        data_part_frame = \
            DataLinkLayerEncoderRT().build_data_word(data_wd_part)
        # future implementation of checksum here
        return data_part_frame

    def deconstruct_command_word(self, recd_command_frame):
        recd_command_word = \
            DataLinkLayerDecoderRT().decode_cmd_word(recd_command_frame)
        return recd_command_word

    def deconstruct_data_word(self, recd_data_frame):
        recd_data_word = \
            DataLinkLayerDecoderRT().decode_data_word(recd_data_frame)
        return recd_data_word

    def construct_status_word(self, rt_address):
        status_word_frame = \
            DataLinkLayerEncoderRT().build_status_word(rt_address)
        return status_word_frame

    def analyze_command_word(self, cmd_word):
        rt_address = cmd_word[0:2]
        if not rt_address == "01":
            return 0
        else:
            tr_bit = cmd_word[2]
            if tr_bit == "R":
                return [self.construct_status_word(rt_address)]
            elif tr_bit == "T":
                communication_frames = list()
                communication_frames.append(
                    self.construct_status_word(rt_address))
                data_count = int(cmd_word[-2:], 16)
                for i in range(data_count):
                    communication_frames.append(
                        self.construct_data_word(
                            self.lookup_memory["{0:02x}".format(
                                int(cmd_word[3:5], 16)+i)].encode("hex")))
                return communication_frames

    def interprete_incoming_frame(self, incoming_frame):
        if incoming_frame[0:3] == "100":
            command_word = self.deconstruct_command_word(incoming_frame)
            return self.analyze_command_word(command_word)

        elif incoming_frame[0:3] == "001":
            data_word = self.deconstruct_data_word(incoming_frame)
            print(data_word)
            return data_word.decode("hex")
