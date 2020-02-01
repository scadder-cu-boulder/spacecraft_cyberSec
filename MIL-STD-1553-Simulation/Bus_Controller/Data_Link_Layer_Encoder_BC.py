
class DataLinkLayerEncoderBC:

    def __char_check(self, character):
        if not str.isdigit(character):
            print("Invalid address bits")
            return False
        elif int(character) != 0  and int(character) != 1:
            print("Invalid address bits 1")
            return False
        else:
            return True

    def build_cmd_word(self, cmd_word):
        try:
            # Following string represents 3 Sync bits. 
            # Command Word uses positive sync. Hence value is 100
            cmd_word_frame = '100'

            # Following 2 characters represent 5 bit RT Address.
            # Input is HEX. So, first HEX character represent a single bit
            # While the next HEX character represents 4 bits in the frame
            # So, char1 can either be 0 and 1 and char2 can be 0x0-0xF 
            char1 = cmd_word[0]
            if not self.__char_check(char1):
                exit()
            cmd_word_frame = cmd_word_frame + char1

            char2 = cmd_word[1]
            cmd_word_frame = cmd_word_frame + '{0:04b}'.format(int(char2, 16))

            # Next character shows Reception or Transmission command for RT
            # It is represented by 1 bit in data frame. 0 is R and 1 is T
            char3 = cmd_word[2]
            if char3 == 'R':
                cmd_word_frame = cmd_word_frame + '0'
            elif char3 == 'T':
                cmd_word_frame = cmd_word_frame + '1'
            else:
                print("Invalid T/R bit")

            # Next 2 characters from input represent 5 bit Subaddress 
            # or Mode code representators. 
            # Input value of 0x00 or 0x1f says that next 5 bits will be a Mode Code
            # Structure is same as RT address.        
            char4 = cmd_word[3]
            if not self.__char_check(char4):
                exit()
            cmd_word_frame = cmd_word_frame + char4

            char5 = cmd_word[4]
            cmd_word_frame = cmd_word_frame + '{0:04b}'.format(int(char5, 16))

            # Next 2 characters from input represent 5 bit Word Count or Mode Code
            # depending on the last 5 bits from the message.
            # Structure is again same as RT address.
            char6 = cmd_word[5]
            if not self.__char_check(char6):
                exit()
            cmd_word_frame = cmd_word_frame + char6

            char7 = cmd_word[6]
            cmd_word_frame = cmd_word_frame + '{0:04b}'.format(int(char7, 16))

            # We need to add one parity bit at the end of the message
            cmd_word_frame = cmd_word_frame + '1'

            print(cmd_word_frame)
            return cmd_word_frame
        except Exception as ex:
            print("Exception while creating Command Word Frame.\n Exception:{}".format(str(ex)))


    def build_data_word(self, data_word):
        print("jsdbcj")
