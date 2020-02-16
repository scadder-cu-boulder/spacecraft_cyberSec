import binascii
from Data_Link_Layer.Data_Link_Layer_Encoder_BC import DataLinkLayerEncoderBC
from Data_Link_Layer.Data_Link_Layer_Decoder_BC import DataLinkLayerDecoderBC


class CommunicationLayerBC:
    def send_command_word(
            self, rt_address, tr_bit, sub_address, data_word_count):
        command_word = ''
        if not len(rt_address) > 2:
            command_word = command_word + rt_address

        if (not len(tr_bit) > 1) and tr_bit.isalpha():
            command_word = command_word + tr_bit

        if not len(sub_address) > 2:
            command_word = command_word + sub_address

        if not len(data_word_count) > 2:
            command_word = command_word + data_word_count

        if len(command_word) < 7 or len(command_word) > 7:
            raise Exception(
                "Invalid data input. Command word format does not match.")
        command_frame = DataLinkLayerEncoderBC().build_cmd_word(command_word)
        return command_frame

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

    def send_data_word(self, data_wd_part):
        data_part_frame = \
            DataLinkLayerEncoderBC().build_data_word(data_wd_part)
        # future implementation of checksum here

        return data_part_frame

    def receive_status_word(self, recd_status_frame):
        recd_status_word = \
          DataLinkLayerDecoderBC().decode_status_word(recd_status_frame)

        return recd_status_word

    def receive_data_word(self, receive_data_word):
        recd_data_word = \
          DataLinkLayerDecoderBC().decode_data_word(receive_data_word)
        return recd_data_word
