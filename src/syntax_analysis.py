"""

    This file handles the syntacticall analysis part of the project

"""

"""

    production rules

    code: print_statement | identifier = [String | exp];
    print_statement: print(string); | print(exp);


    exp: exp + term | exp - term | term
    term: factor * term | factor / term | factor
    factor: [0123456789]* | (exp) | identifier

    **Elimination of left recursion**
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
                raise Exception("expected ) but got", self.tokens)
        elif (len(self.tokens) > 0 and self.tokens[0][0] == "identifier"):
            # consumes the token
            cur = self.tokens.pop(0)

            if (cur not in self.sym_table):
                raise Exception("unexpected symbol", cur)

            return self.sym_table[cur]


        else:
            raise Exception("expected token but got", self.tokens)



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
        self.tokens.pop(0) # consume print
        self.tokens.pop(0) # consumes (

        cur = self.tokens.pop(0) # consumes identfier

        if (cur not in self.sym_table):
            raise Exception("unexpected symbol:", cur)

        value = self.sym_table[cur] # retrives the value at the symbol table
        print(value)

        if (len(self.tokens) > 1):
            if (self.tokens[0][1] == ")" and self.tokens[1][1] == ";"):
                self.tokens.pop(0) # consume right paranthesis
                self.tokens.pop(0) # consume the end semicolon
                return
        raise Exception("expected ), or ; but got", self.tokens)





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
        if (len(self.tokens) > 0 and self.tokens[0][0] == "Print"):
            self.tokens.pop(0)
            if (len(self.tokens) > 0 and self.tokens[0][1] == "("):
                self.tokens.pop(0)
                x = self.exp()
                if (len(self.tokens) > 0 and self.tokens[0][1] == ")"):
                    self.tokens.pop(0)
                    if (len(self.tokens) > 0 and self.tokens[0][1] == ";"):
                        self.tokens.pop(0)
                        print(x)
                        return
        raise Exception("Syntax error", self.tokens)

    # assuming that the list of tokens leads to a print strign exceutes that line
    def print_string(self):
        self.tokens.pop(0) # consumes print statement
        self.tokens.pop(0) # consume left paranthesis
        print(self.tokens.pop(0)[1]) # print the string

        if (len(self.tokens) > 0 and self.tokens[0][1] == ")"):
            self.tokens.pop(0) # consumes right paranthesis
            if (len(self.tokens) > 0 and self.tokens[0][1] == ";"):
                self.tokens.pop(0)
            else:
                raise Exception("Expected a ; but got ", self.tokens)

        else:
            raise Exception("Expected a ) but got ", self.tokens)

    # given a list of tokens will return true if it prints an string
    def _is_print_string(self):
        if (len(self.tokens) > 2 and self.tokens[0][0] == "Print"):
            if (self.tokens[1][1] == "(" and self.tokens[2][0] == "string" ):
                return True

        return False


    # assuming that the list of tokens leads to identfier assignment executes that line
    def identfier_assignment(self):
        ident = self.tokens.pop(0) # consumes identifier
        self.tokens.pop(0) # consume equality

        if (len(self.tokens) > 0 and self.tokens[0][0] == "string"):
            self.sym_table[ident] = self.tokens.pop(0)[1] # add new value to symbol table
        elif (len(self.tokens) > 0 and self.tokens[0][0] == "num"):
            self.sym_table[ident] = self.exp()
        elif (len(self.tokens) > 0 and self.tokens[0][1] == "("):
            self.sym_table[ident] = self.exp()
        else:
            raise Exception("expected a num or string but got", self.tokens)

        # ensures ; at the end
        if (len(self.tokens) > 0 and self.tokens[0][1] == ";"):
            self.tokens.pop(0)
            return
        raise Exception("expected ; but got", self.tokens)

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




