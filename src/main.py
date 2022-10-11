import lexer

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

def e(t):
    summ = T(t) + e_prime(t)
    return summ

def e_prime(t):
    summ = 0
    cur = t.get_next_token()
    if (cur != None and cur[1] in "+-"):
        t._consume_next_token()
        if (cur[1] == "+"):
            summ+=T(t)
        else:
            summ -= T(t)
        summ+= e_prime(t)

    return summ

def T(t):
    return factor(t) * T_prime(t)


def T_prime(t):
    summ = 1
    cur = t.get_next_token()

    if (cur != None and cur[1] in "*/"):
        t._consume_next_token()
        if (cur[1] == "*"):
            summ*= factor(t)
        else:
            summ/= factor(t)

        summ*= T_prime(t)

    return summ


def factor(t):
    cur = t.get_next_token()
    if (cur != None and cur[0] == "num" ):
        return t._consume_next_token()[1]


print(e(t))










