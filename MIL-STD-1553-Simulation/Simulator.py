
from Bus_Controller.Data_Link_Layer_Encoder_BC import DataLinkLayerEncoderBC
from Remote_Terminal.Data_Link_Layer_Decoder_RT import DataLinkLayerDecoderRT

from Remote_Terminal.Data_Link_Layer_Encoder_RT import DataLinkLayerEncoderRT
from Bus_Controller.Data_Link_Layer_Decoder_BC import DataLinkLayerDecoderBC

if __name__ == "__main__":
    cmd_wd_frame = DataLinkLayerEncoderBC().build_cmd_word("01R041F")
    DataLinkLayerDecoderRT().decode_cmd_word(cmd_wd_frame)

    status_wd_frame = DataLinkLayerEncoderRT().build_status_word("1F")
    status_wd = DataLinkLayerDecoderBC().decode_status_word(status_wd_frame)

    data_wd_frame_BC = DataLinkLayerEncoderBC().build_data_word("ABCD")
    data_wd_frame_RT = DataLinkLayerEncoderRT().build_data_word("123F")
