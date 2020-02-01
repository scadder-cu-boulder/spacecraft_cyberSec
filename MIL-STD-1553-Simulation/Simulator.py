
from Bus_Controller.Data_Link_Layer_Encoder_BC import DataLinkLayerEncoderBC
from Remote_Terminal.Data_Link_Layer_Decoder_RT import DataLinkLayerDecoderRT


if __name__ == "__main__":
    cmd_wd_frame = DataLinkLayerEncoderBC().build_cmd_word("01R041F")
    DataLinkLayerDecoderRT().decode_cmd_word(cmd_wd_frame)
