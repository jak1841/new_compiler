import lexer

chr = lexer.get_characters_from_file("code.txt")



"""

    Exp: Term + term | term - term | term
    Term: factor * factor | factor / factor | factor
    factor: num


"""


t = lexer.lex(chr)

list_tokens = t.get_list_token()
print(list_tokens)


def exp(t):
    summ = term(t)
    while (t != [] and t[0][1] in "+-"):
        cur = t.pop(0)
        if (cur[1] == "+"):
            summ+= term(t)
        elif (cur[1] == "-"):
            summ-= term(t)

    return summ

def term(t):
    summ = factor(t)
    while (t != [] and t[0][1] in "*/"):
        cur = t.pop(0)
        if (cur[1] == "*"):
            summ = summ * factor(t)
        elif(cur[1] == "/"):
            summ = summ/factor(t)

    return summ

def factor(t):
    if (t != [] and t[0][0] == "num"):
        return t.pop(0)[1]


    raise Exception("Expected a number or paranthesis but got ", t)



print(eval ("1 + 3 + 4 / 5 / 6 *2 /6 -9 +8 - 1 -2 /1 /5 /3 * 6 *3"))
print(exp(list_tokens))











