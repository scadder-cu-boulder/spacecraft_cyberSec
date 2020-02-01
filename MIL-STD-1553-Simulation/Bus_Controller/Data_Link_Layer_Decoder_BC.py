class DataLinkLayerDecoderBC:

    message_error_bit = ''
    instrumentation_bit = ''
    service_request_bit = ''
    reserved_bits = ''
    brdcst_received_bit = ''
    busy_bit = ''
    subsystem_flag_bit = ''
    dynamic_bus_control_accpt_bit = ''
    terminal_flag_bit = ''
    rt_address = ''

    def decode_status_word(self, status_word_frame):
        try:
            # 3 bits Sync and 1 bit parity bit are ignored for decoding 
            # as it does not affect any data that is necessary
            status_word = {}

            rt_address = rt_address + status_word_frame[3]

            addr_char = cmd_word_frame[4:8]
            rt_address = rt_address + str(hex(int(addr_char,2)))[2:]
            status_word.update('rt_address':rt_address)

            # Next bit represents message error bit
            message_error_bit = cmd_word_frame[8]
            status_word.update('message_error_bit':message_error_bit)

            # Next bit represents instrumentation bit
            instrumentation_bit = cmd_word_frame[9]
            status_word.update('instrumentation_bit':instrumentation_bit)

            # Next bit represents service request bit
            service_request_bit = cmd_word_frame[10]
            status_word.update('service_request_bit':service_request_bit)

            # Next 3 bits represent reserved bits
            reserved_bits = cmd_word_frame[11:14]
            status_word.update('reserved_bits':reserved_bits)

            # Next bit represents BRDCST received bit
            brdcst_received_bit = cmd_word_frame[14]
            status_word.update('brdcst_received_bit':brdcst_received_bit)

            # Next bit represents busy bit
            busy_bit = cmd_word_frame[15]
            status_word.update('busy_bit':busy_bit)

            # Next bit represents subsystem flag bit
            subsystem_flag_bit = cmd_word_frame[16]
            status_word.update('subsystem_flag_bit':subsystem_flag_bit)

            # Next bit represents dynamic bus control accept bit
            dynamic_bus_control_accpt_bit = cmd_word_frame[17]
            status_word.update('dynamic_bus_control_accpt_bit':dynamic_bus_control_accpt_bit)

            # Next bit represents terminal flag bit
            terminal_flag_bit = cmd_word_frame[18]
            status_word.update('terminal_flag_bit':terminal_flag_bit)

            return status_word
        except Exception as ex:
            print("Exception while decoding a status word from on RT\n Exception:{}".format(str(ex)))
