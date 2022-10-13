"""

    This file handles the syntacticall analysis part of the project

"""

"""

    production rules

    statement: print(string); | print(exp);


    exp: exp + term | exp - term | term
    term: factor * term | factor / term | factor
    factor: [0123456789]* | (exp)

    **Elimination of left recursion**
    exp: term exp'
    exp': +term exp' | -term exp' | e

    term: factor term'
    term': *factor term' | /factor term' | e

    factor: [0123456789]* | (exp)



"""

class syn_analysis:
    def __init__(self, tokens):
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

        else:
            raise Exception("expected token but got", self.tokens)



    """

        Printing methods handled below

    """


    # given a list of tokens will return true if it print an math expression
    def _is_print_math_expression(self):
        if (len(self.tokens) > 2 and self.tokens[0][0] == "Print"):
            if (self.tokens[1][1] == "(" and (self.tokens[2][0] == "num" or self.tokens[2][1] == "(")):
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




    # Defines what a line of a code could look like and executes that line
    def statement(self):
        if (self._is_print_math_expression()):
            self.print_math_expression()
        elif (self._is_print_string()):
            self.print_string()



    # executes the program line by line
    def execute_program(self):
        while (len(self.tokens) > 0):
            self.statement()




