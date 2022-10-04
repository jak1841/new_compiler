import lexer

chr = lexer.get_characters_from_file("code.txt")



"""

    Exp: Term + Term | Term - Term | Term
    Term: Factor * Factor | Factor / Factor | Factor
    Factor: Num | (exp)

"""


t = lexer.lex(chr)

print(t.get_list_token())








