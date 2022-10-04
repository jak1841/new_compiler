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
    def is_EOF(self):
        return len(self.string) <= self.index

    # current character is whitespace => increments index
    def consume_whitespace(self):
        while (self.is_EOF() == False and self.string[self.index].isspace()):
            self.index += 1

    # current character return
    def get_cur_character(self):
        if (self.is_EOF()):
            return None
        return self.string[self.index]

    # not EOF => increment index and return current character
    def consume_character(self):
        if (self.is_EOF()):
            return None
        chr = self.get_cur_character()
        self.index+= 1
        return chr

    # assume current character is a number => return number token (num, '213')
    def number_token(self):
        numbers = "0123456789"
        num = ""

        while (self.get_cur_character() != None and self.get_cur_character() in numbers):
            num+=self.consume_character()

        return ("num", float(num))

    # retrieves the next token 
    def get_next_token(self):
        numbers = "0123456789"

        self.consume_whitespace()
        if (self.get_cur_character() != None and self.get_cur_character() in numbers):
            return self.number_token()
        else:
            return None

    # returns a list of tokens of the form (token_id, token_val)
    def get_list_token(self):
        lst_token = []
        cur_token = ""
        while (self.is_EOF() == False and cur_token != None):
            cur_token = self.get_next_token()
            lst_token.append(cur_token)

        return lst_token































