
# from Bus_Controller.Data_Link_Layer_Encoder_BC import DataLinkLayerEncoderBC
# from Remote_Terminal.Data_Link_Layer_Decoder_RT import DataLinkLayerDecoderRT

# from Remote_Terminal.Data_Link_Layer_Encoder_RT import DataLinkLayerEncoderRT
# from Bus_Controller.Data_Link_Layer_Decoder_BC import DataLinkLayerDecoderBC

# from Remote_Terminal.Mode_Code_Analyzer import ModeCodeAnalyzer

from Bus_Controller.Message_Layer.ML_Encoder_BC import MessageLayerEncoderBC


if __name__ == "__main__":
    # cmd_wd_frame = DataLinkLayerEncoderBC().build_cmd_word("01R041F")
    # DataLinkLayerDecoderRT().decode_cmd_word(cmd_wd_frame)

    # status_wd_frame = DataLinkLayerEncoderRT().build_status_word("1F")
    # status_wd = DataLinkLayerDecoderBC().decode_status_word(status_wd_frame)

    # data_wd_frame_BC = DataLinkLayerEncoderBC().build_data_word("ABCD")
    # data_wd_frame_RT = DataLinkLayerEncoderRT().build_data_word("123F")

    # data_word_BC = \
    # DataLinkLayerDecoderBC().decode_data_word(data_wd_frame_BC)

    # ModeCodeAnalyzer().analyze_mode_code("01T1F02")

    print(MessageLayerEncoderBC().send_message_to_RT("11", "11", "HELLOjhb"))
    print(MessageLayerEncoderBC().receive_message_from_RT("11", "10", "05"))
