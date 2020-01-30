
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
        msg = '100'
        char1 = cmd_word[0]
        if not self.__char_check(char1):
            exit()
        msg = msg + char1

        char2 = cmd_word[1]
        msg = msg + '{0:04b}'.format(int(char2))

        char3 = cmd_word[2]
        if char3 == 'R':
            msg = msg + '0'
        elif char3 == 'T':
            msg = msg + '1'
        else:
            print("Invalid T/R bit")

        char4 = cmd_word[3]
        if not self.__char_check(char4):
            exit()
        msg = msg + char4

        char5 = cmd_word[4]
        msg = msg + '{0:04b}'.format(int(char5))

        char6 = cmd_word[5]
        if not self.__char_check(char6):
            exit()
        msg = msg + char6

        char7 = cmd_word[6]
        msg = msg + '{0:04b}'.format(int(char7))

        print(msg)


    def build_data_word(self, data_word):
        print("jsdbcj")
