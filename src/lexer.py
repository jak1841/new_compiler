"""
    Author: Jaskarn Dhillon
    Purpose: converts a stream of characters into tokens with a specefic type
"""

"""
    Tokens Seperated by whitespace

    List of Token
        (Integer, [0123456789]*)
        (MathOperator, [+, -, *, /])
        (Equality, [=])
        (Variable, [A-Z|a-z])
        (Paranthesis, [(, )])
        (Print, print)
        (semicolon, ;)
"""

# returns a string of characters from a specefic filename
def get_characters_from_file(filename):
    characters = ""
    with open(filename) as f:
        while True:
            c = f.read(1)
            characters+= c
            if not c:
                return characters
                break


class lex:
    def __init__(self, characters_from_file):
        self.string = characters_from_file
        self.index = 0

    # end of file reached => true else false
    def _is_EOF(self):
        return len(self.string) <= self.index

    # current character is whitespace => increments index
    def _consume_whitespace(self):
        while (self._is_EOF() == False and self.string[self.index].isspace()):
            self.index += 1

    # current character return
    def _get_cur_character(self):
        if (self._is_EOF()):
            return None
        return self.string[self.index]

    # not EOF => increment index and return current character
    def _consume_character(self):
        if (self._is_EOF()):
            return None
        chr = self._get_cur_character()
        self.index+= 1
        return chr

    # peeks and returns the next character
    def _peek(self):
        if (self._is_EOF()):
            return None
        return self.string[self.index + 1]

    # assuming current character leads to a number will return a number token
    def _number_token(self):
        numbers = "0123456789."
        num = ""

        num_decimal_points = 0


        # negative numbers
        if (self._get_cur_character() == "-"):
            num += self._consume_character()

        while (self._get_cur_character() != None and self._get_cur_character() in numbers):
            num+=self._consume_character()

        return ("num", float(num))


    # checks if the current character will lead to a num token
    def _is_num_token(self, cur):
        numbers = "0123456789"

        if (cur in numbers):
            return True
        elif (cur == "-" and self._peek() in numbers):
            return True



        return False



    # retrieves the next token
    def _get_next_token(self):

        self._consume_whitespace()
        cur = self._get_cur_character()

        if (cur == None):
            return None


        elif (self._is_num_token(cur)):
            return self._number_token()






        else:
            return None

    # returns a list of tokens of the form (token_id, token_val)
    def get_list_token(self):
        lst_token = []
        cur_token = self._get_next_token()

        while (cur_token != None):
            lst_token.append(cur_token)
            cur_token = self._get_next_token()



        return lst_token































