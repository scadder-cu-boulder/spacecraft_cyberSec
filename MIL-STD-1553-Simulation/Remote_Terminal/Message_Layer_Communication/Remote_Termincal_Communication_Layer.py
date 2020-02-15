from Data_Link_Layer.Data_Link_Layer_Decoder_RT import DataLinkLayerDecoderRT
from Data_Link_Layer.Data_Link_Layer_Encoder_RT import DataLinkLayerEncoderRT
from Data_Link_Layer.Mode_Code_Analyzer import ModeCodeAnalyzer


class CommunicationLayerRT:

    def generate_data_parts(self, data_wd):
        data_wd_parts = []
        for char in data_wd:
            data_part_bits = format(ord(char), 'b')
            bits_diff = 8 - len(data_part_bits)
            if bits_diff > 0:
                appnd_bits = '0'*bits_diff
                data_part_bits = appnd_bits + data_part_bits
            data_wd_parts.append(data_part_bits)

        return data_wd_parts

    # def send_data_word(self, data_wd_part):
    #     data_part_frame = \
    #         DataLinkLayerEncoderBC().build_data_word(data_wd_part)
    #     #future implementation of checksum here

    #     return data_part_frame

    # def receive_command_word(self, recd_command_frame):
    #     recd_command_word = \
    #         DataLinkLayerDecoderRT().decode_command_word(recd_command_frame)

    #     return recd_command_word

    # def receive_status_word(self, recd_status_frame):
    #     recd_status_word = \
    #         DataLinkLayerDecoderRT().decode_status_word(recd_status_frame)

    #     return recd_status_word

    # def receive_data_word(self, receive_data_word):
    #     recd_data_word = \
    #         DataLinkLayerDecoderRT().decode_data_word(recd_data_frame)

    #     return recd_data_word
