class DataLinkLayerDecoderRT:

    def decode_command_word(self, cmd_message):
        cmd_wd = ''
        cmd_wd = cmd_wd + cmd_message[3]

        addr_char = cmd_message[4:8]
        cmd_wd = cmd_wd + str(hex(int(addr_char,2)))[2:]

        tr_char = cmd_message[8]
        if tr_char == '0':
            tr_char = 'R'
        if tr_char == '1':
            tr_char = 'T'
        cmd_wd = cmd_wd + tr_char
        
        cmd_wd = cmd_wd + cmd_message[9]

        subaddr_char = cmd_message[10:14]
        cmd_wd = cmd_wd + str(hex(int(subaddr_char,2)))[2:]
        
        # chars = cmd_message[9] + str(hex(int(subaddr_char,2)))[2:]       
        
        cmd_wd = cmd_wd + cmd_message[14]
        
        word_char = cmd_message[15:19]
        cmd_wd = cmd_wd + str(hex(int(word_char,2)))[2:]

        print(cmd_wd)
        
        return cmd_wd