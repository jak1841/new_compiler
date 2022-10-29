"""
    Author: Jaskarn Dhillon
    Purpose: converts a stream of characters into tokens with a specefic type
"""

"""
    Tokens Seperated by whitespace

    List of Token
        (Integer, [0123456789]*) X
        (MathOperator, [+, -, *, /]) X
        (Equality, [=]) X
        (identifier, [A-Z|a-z]*) X
        (Paranthesis, [(, )]) X
        (Print, print)
        (semicolon, ;) X
        (string, "[characters]*")
        (boolean, true | false)
        (logical_operators or | and)
        (datatype, float | string | bool)

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
        if (len(self.string) <= self.index + 1):
            return None
        return self.string[self.index + 1]



    '''

        Detecting tokens functions

    '''

    # assuming current character leads to a number will return a number token
    def _number_token(self):
        numbers = "0123456789"
        num = ""

        while (self._get_cur_character() != None and self._get_cur_character() in numbers):
            num+=self._consume_character()

        return ("num", float(num))

    # checks if the current character will lead to a num token
    def _is_num_token(self, cur):
        numbers = "0123456789"

        if (cur in numbers):
            return True

        return False

    # assuming current character leads to a identifier will return a identifier token
    def _identfier_token(self):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        alpha_range = lower + upper

        ident = ""

        while (self._get_cur_character() != None and self._get_cur_character() in alpha_range):
            ident += self._consume_character()

        # keywords
        if (ident == "print"):
            return ("Print", ident)
        elif (ident in ["True", "False"]):
            return ("boolean", ident)
        elif (ident in ["or", "and"]):
            return ("logical_operators", ident)
        elif (ident in ["string", "float", "bool"]):
            return ("datatype", ident)
        elif (ident == "if"):
            return ("keyword", ident)


        return ("identifier", ident)

    # checks if the current character will lead to identifier token
    def _is_identifier_token(self, cur):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if (cur in lower or cur in upper):
            return True
        return False

    # assuming current character leads to a math operator will return a mathop token
    def _math_operator_token(self):
        return ("mathop", self._consume_character())

    # checks if the current character will lead to a mathoperator token
    def _is_math_operator_token(self, cur):
        math_operators = "+*-/"
        return cur in math_operators

    # assumign current character leads to a paranthesis will return paranthesis token
    def _paranthesis_token (self):
        return ("paranthesis", self._consume_character())

    # checks if the current character will lead to a paranthesis token
    def _is_paranthesis_token(self, cur):
        paranthesis = "()"
        return cur in paranthesis


    # assuming current character leads to a equality token will return equality token
    def _equality_token(self):
        return ("equality", self._consume_character())

    # checks if the current characeter will lead to a equality token
    def _is_equality_token(self, cur):
        return cur == "="


    # assuming current character leads to a semicolon token will return it
    def _semicolon_token(self):
        return ("semicolon", self._consume_character())

    # checks if the current character will lead to semicolon token
    def _is_semicolon_token(self,cur):
        return cur == ";"

    # assuming current character leads to a string token will return it
    def _string_token(self):
        str = ""
        self._consume_character()   # removes first double quote
        while (self._get_cur_character() != None and self._get_cur_character() != "\""):
            str +=self._consume_character()

        if (self._get_cur_character() == None):
            raise Exception("Expected end double quote but got None")
        self._consume_character() # removes second double quote

        return ("string", str)


    # checks if the current character will lead to a string token
    def _is_string_token(self, cur):
        if (cur == "\""):
            return True







    # returns the next token
    def get_next_token(self):
        temp = self.index



        self._consume_whitespace()  # gets rid of whitespace
        cur = self._get_cur_character()

        try:
            if (cur == None):
                return None
            elif (self._is_num_token(cur)):
                return self._number_token()
            elif (self._is_identifier_token(cur)):
                return self._identfier_token()
            elif (self._is_math_operator_token(cur)):
                return self._math_operator_token()
            elif (self._is_paranthesis_token(cur)):
                return self._paranthesis_token()
            elif (self._is_equality_token(cur)):
                return self._equality_token()
            elif (self._is_semicolon_token(cur)):
                return self._semicolon_token()
        except:
            pass
        finally:
            self.index = temp


    # retrieves and consumes the next token
    def _consume_next_token(self):

        self._consume_whitespace()  # gets rid of whitespace
        cur = self._get_cur_character()

        if (cur == None):
            return None

        elif (self._is_num_token(cur)):
            return self._number_token()
        elif (self._is_identifier_token(cur)):
            return self._identfier_token()
        elif (self._is_math_operator_token(cur)):
            return self._math_operator_token()
        elif (self._is_paranthesis_token(cur)):
            return self._paranthesis_token()
        elif (self._is_equality_token(cur)):
            return self._equality_token()
        elif (self._is_semicolon_token(cur)):
            return self._semicolon_token()
        elif (self._is_string_token(cur)):
            return self._string_token()








        else:
            return None

    # returns a list of tokens of the form (token_id, token_val)
    def get_list_token(self):
        lst_token = []
        cur_token = self._consume_next_token()

        while (cur_token != None):
            lst_token.append(cur_token)
            cur_token = self._consume_next_token()



        return lst_token

































