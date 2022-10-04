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

    # assume current character is a number => return number token (num, '213')
    def _number_token(self):
        numbers = "0123456789"
        num = ""

        while (self._get_cur_character() != None and self._get_cur_character() in numbers):
            num+=self._consume_character()

        return ("num", float(num))

    # retrieves the next token
    def _get_next_token(self):
        numbers = "0123456789"

        self._consume_whitespace()
        if (self._get_cur_character() != None and self._get_cur_character() in numbers):
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































