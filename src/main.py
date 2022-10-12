import lexer
import syntax_analysis as sa
chr = lexer.get_characters_from_file("code.txt")




t = lexer.lex(chr)

# list_tokens = t.get_list_token()
# print(list_tokens)

"""
    Grammar

    E -> E + T | T
    T -> T * F | F
    F -> [0123456789]* | (E)

    E  -> TE'
    E' -> +FE' | -FE' | e
    T -> FT'
    T' -> *FT' | /FT' | e
    F -> [0123456789]*


"""
list_tokens = t.get_list_token()
lol = sa.syn_analysis(list_tokens)

lol.execute_program()














