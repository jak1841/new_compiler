"""

    This file handles the syntacticall analysis part of the project

"""

"""

    production rules

    code: print_statement | assignment

    print_statement: print(string); | print(exp) | print(identifier);

    assignment -> datatype identifier = [String | exp | identifier | boolean];



    bool_exp -> bool_exp or bool_term | bool_term
    bool_term -> bool_term and bool_factor | boolean
    bool_factor -> boolean | (bool_exp)
    boolean -> true | false

    ** Eliminating left recursion**
    bool_exp -> bool_term bool_exp'
    bool_exp' -> and bool_term bool_exp' | e
    bool_term -> bool_

    exp: term exp'
    exp': +term exp' | -term exp' | e
    term: factor term'
    term': *factor term' | /factor term' | e
    factor: [0123456789]* | (exp)



"""

class syn_analysis:
    def __init__(self, tokens):
        self.sym_table = {}
        self.tokens = tokens

    # Given a token_type will return true if top of token list has same token_type
    # if not return false
    def is_next_token_type_same(self, token_type):
        if (len(self.tokens) > 0 and self.tokens[0][0] == token_type):
            return True
        return False

    # Given a token_type will check that the top of the token list has that specefic
    # tokentype and if it does pop return the token, if not => error
    def match_token_type(self, token_type):
        if (len(self.tokens) > 0 and self.tokens[0][0] == token_type):
            return self.tokens.pop(0)

        # error if not same or tokens list is empty
        if (len(self.tokens) > 0):
            raise Exception("Expected", token_type, "but got", self.tokens[0])
        raise Exception("Expected", token_type, "but got", None)

    # Given a token value will check that the top of the token list has that specefic
    # token val and if it does pop return the token, if not => erro
    def match_token_val(self, token_val):
        if (len(self.tokens) > 0 and self.tokens[0][1] == token_val):
            return self.tokens.pop(0)

        # error if not same or tokens list is empty
        if (len(self.tokens) > 0):
            raise Exception("Expected", token_val, "but got", self.tokens[0])
        raise Exception("Expected", token_val, "but got", None)

    # Given a symbol_token checks if it is in the symbol table, if is => return symbol_token
    # if not => erro
    def match_symbol(self, symbol_token):
        if (symbol_token in self.sym_table):
            return symbol_token
        raise Exception("Unexpected symbol", symbol_token)




    # where the error is in the code
    def expected_token(self, expected_type):
        if (len(self.tokens) > 0):
            raise Exception("Expected", expected_type, "but got", self.tokens[0])
        raise Exception("Expected", expected_type, "but got", None)

    # error when encountering unexpected symbol
    def unexpected_symbol(self):
        raise Exception("unexpected symbol", cur)


    """
        This is for evaluating math expressions
    """

    def exp(self):
        return self.term() + self.exp_prime()

    def exp_prime(self):
        summ =  0
        if (len(self.tokens) > 0 and self.tokens[0][1] in "+-"):
            cur = self.tokens[0][1]
            self.tokens.pop(0)
            if (cur == "+"):
                summ+=self.term()
            else:
                summ-=self.term()

            summ+= self.exp_prime()

        return summ

    def term(self):
        return self.factor()* self.term_prime()

    def term_prime(self):
        summ =  1
        if (len(self.tokens) > 0 and self.tokens[0][1] in "*/"):
            cur = self.tokens[0][1]
            self.tokens.pop(0)
            if (cur == "*"):
                summ*=self.factor()
            else:
                summ/=self.factor()

            summ*= self.term_prime()

        return summ

    def factor(self):
        if (len(self.tokens) > 0 and self.tokens[0][0] == "num"):
            return self.tokens.pop(0)[1]
        elif (len(self.tokens) > 0 and self.tokens[0][1] == "("):
            self.tokens.pop(0)
            res = self.exp()
            if (len(self.tokens) > 0 and self.tokens[0][1]):
                self.tokens.pop(0)
                return res
            else:
                self.expected_token(")")
        elif (len(self.tokens) > 0 and self.tokens[0][0] == "identifier"):
            # consumes the token
            cur = self.tokens.pop(0)

            if (cur not in self.sym_table):
                self.unexpected_symbol()

            return self.sym_table[cur]


        else:
            self.expected_token("token")



    """

        Printing methods handled below

    """
    # given a list of tokens will return true if it prints an identfier
    def _is_print_identfier(self):
        if (len(self.tokens) > 3 and self.tokens[0][0] == "Print"):
            if (self.tokens[1][1] == "(" and self.tokens[2][0] == "identifier" and self.tokens[3][1] == ")"):
                return True

        return False


    # assuming that list of tokens lead to a print identifier, executes that line
    def print_identifier(self):
        self.match_token_type("Print")
        self.match_token_val("(")
        identifier_token = self.match_token_type("identifier")

        symbol = self.match_symbol(identifier_token)
        value = self.sym_table[symbol] # retrives the value at the symbol table
        print(value)

        self.match_token_val(")")
        self.match_token_val(";")






    # given a list of tokens will return true if it print an math expression
    def _is_print_math_expression(self):
        # number or (
        if (len(self.tokens) > 2 and self.tokens[0][0] == "Print"):
            if (self.tokens[1][1] == "("):
                if (self.tokens[2][0] == "num"):
                    return True
                elif (self.tokens[2][1] == "("):
                    return True

        # identfier
        if (len(self.tokens) > 3 and self.tokens[0][0] == "Print" and self.tokens[1][1] == "("):
            if (self.tokens[2][0] == "identifier"):
                if (self.tokens[3][0] == "mathop"):
                    return True




        return False

    # assuming that the list of tokens lead to a print an math expression executes that line
    def print_math_expression(self):
        self.match_token_type("Print")
        self.match_token_val("(")
        print(self.exp())
        self.match_token_val(")")
        self.match_token_val(";")


    # assuming that the list of tokens leads to a print strign exceutes that line
    def print_string(self):
        self.match_token_type("Print") # consumes print statement
        self.match_token_val("(") # consume left paranthesis
        string_token = self.match_token_type("string")
        print(string_token[1]) # print the string
        self.match_token_val(")")
        self.match_token_val(";")

    # given a list of tokens will return true if it prints an string
    def _is_print_string(self):
        if (len(self.tokens) > 2 and self.tokens[0][0] == "Print"):
            if (self.tokens[1][1] == "(" and self.tokens[2][0] == "string" ):
                return True

        return False


    # assuming that the list of tokens leads to identfier assignment executes that line
    def identfier_assignment(self):
        ident = self.match_token_type("identifier")
        self.match_token_val("=")

        if (self.is_next_token_type_same("string")):
            self.sym_table[ident] = self.match_token_type("string")[1]
        elif (self.is_next_token_type_same("num")):
            self.sym_table[ident] = self.exp()
        elif (self.is_next_token_type_same("paranthesis")):
            self.sym_table[ident] = self.exp()
        elif (self.is_next_token_type_same("identifier")):
            self.sym_table[ident] = self.exp()
        else:
            raise Exception("expected a num or string but got", self.tokens)

        self.match_token_val(";")

    # given a list of tokens will reture true if it is an identfier assigment statement
    def _is_identifier_assigment(self):
        if (len(self.tokens) > 1 and self.tokens[0][0] == "identifier"):
            if (self.tokens[1][1] == "="):
                return True

        return False




    # Defines what a line of a code could look like and executes that line
    def statement(self):
        if (self._is_print_math_expression()):
            self.print_math_expression()
        elif (self._is_print_identfier()):
            self.print_identifier()
        elif (self._is_print_string()):
            self.print_string()
        elif (self._is_identifier_assigment()):
            self.identfier_assignment()



    # executes the program line by line
    def execute_program(self):
        while (len(self.tokens) > 0):
            self.statement()




