"""

    This file handles the syntacticall analysis part of the project

"""

"""

    production rules

    statement: identifier = exp;

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
    def __init__(self):
        pass