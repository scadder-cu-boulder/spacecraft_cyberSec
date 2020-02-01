
from Bus_Controller.Data_Link_Layer_Encoder_BC import DataLinkLayerEncoderBC
from Remote_Terminal.Data_Link_Layer_Decoder_RT import DataLinkLayerDecoderRT

from Remote_Terminal.Data_Link_Layer_Encoder_RT import DataLinkLayerEncoderRT

if __name__ == "__main__":
    cmd_wd_frame = DataLinkLayerEncoderBC().build_cmd_word("01R041F")
    DataLinkLayerDecoderRT().decode_cmd_word(cmd_wd_frame)

    status_wd_frame = DataLinkLayerEncoderRT().build_status_word("1F")
