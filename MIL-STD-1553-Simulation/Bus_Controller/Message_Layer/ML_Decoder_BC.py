from Data_Link_Layer.Data_Link_Layer_Decoder_BC import DataLinkLayerDecoderBC


class MessageLayerDecoderBC:

    def receive_status_word(self, recd_status_frame):
        recd_status_word = \
          DataLinkLayerDecoderBC().decode_status_word(recd_status_frame)

        return recd_status_word

    def receive_data_word(self, receive_data_word):
        recd_data_word = \
          DataLinkLayerDecoderBC().decode_data_word(receive_data_word)
        return recd_data_word
