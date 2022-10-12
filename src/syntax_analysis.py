"""

    This file handles the syntacticall analysis part of the project

"""

"""

    production rules

    statement: print(exp);


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


    # Defines what a line of a code could look like and executes that line
    def statement(self):
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

    # executes the program line by line
    def execute_program(self):
        while (len(self.tokens) > 0):
            self.statement()




