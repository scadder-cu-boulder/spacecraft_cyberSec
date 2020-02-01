class DataLinkLayerEncoderRT:

    message_error_bit = '0'
    instrumentation_bit = '0'
    service_request_bit = '0'
    reserved_bits = '000'
    brdcst_received_bit = '0'
    busy_bit = '0'
    subsystem_flag_bit = '0'
    dynamic_bus_control_accpt_bit = '0'
    terminal_flag_bit = '1'
    parity_bit = '1'

    def __char_check(self, character):
        if not str.isdigit(character):
            print("Invalid address bits")
            return False
        elif int(character) != 0  and int(character) != 1:
            print("Invalid address bits 1")
            return False
        else:
            return True

    def build_status_word(self, rt_address):
        try:
            if len(rt_address) != 2:
                raise Exception("Invalid RT address")
            # Check for foradcast from the command word
            # if Subaddress is 0x1f no need to send status word
            status_word_frame = '100'

            # Following 2 characters represent 5 bit RT Address.
            # Input is HEX. So, first HEX character represent a single bit
            # While the next HEX character represents 4 bits in the frame
            # So, char1 can either be 0 and 1 and char2 can be 0x0-0xF 
            char1 = rt_address[0]
            if not self.__char_check(char1):
                exit()
            status_word_frame = status_word_frame + char1

            char2 = rt_address[1]
            status_word_frame = status_word_frame + '{0:04b}'.format(int(char2, 16))

            # rest of the bits are static in this case and will be appended
            # in the final message.
            # The specific functionality can be implemented for each bit separately

            status_word_frame = status_word_frame + self.message_error_bit \
                                + self.instrumentation_bit \
                                + self.service_request_bit \
                                + self.reserved_bits \
                                + self.brdcst_received_bit \
                                + self.busy_bit \
                                + self.subsystem_flag_bit \
                                + self.dynamic_bus_control_accpt_bit \
                                + self.terminal_flag_bit \
                                + self.parity_bit 

            print(status_word_frame)

            return status_word_frame
        except Exception as ex:
            print("Exception while encoding a status word on RT.\n Exception: {}".format(str(ex)))

    def build_data_word(self, data_word):
        print("jhsjd")