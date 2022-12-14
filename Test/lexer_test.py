import sys

# Adding the src directory to the enviroment variable
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/compiler/new_compiler/src')

import unittest
import lexer


class lexer_test(unittest.TestCase):
    # file contains a bunch of whitespace
    def test_whitespace_file(self):
        # No whitespace
        l = lexer.lex("")
        self.assertEqual([], l.get_list_token())

        # any number of whitespace
        l = lexer.lex(" ")
        self.assertEqual([], l.get_list_token())
        l = lexer.lex("                                                      ")
        self.assertEqual([], l.get_list_token())

        # tab
        l = lexer.lex("                         ")
        self.assertEqual([], l.get_list_token())

        # new line
        l = lexer.lex("\n \n \n \n")
        self.assertEqual([], l.get_list_token())

    # file contains only numbers
    def test_numbers_file(self):
        # single numbers - pos
        l = lexer.lex("7439")
        self.assertEqual([("num", 7439.0)], l.get_list_token())

        l = lexer.lex("83102199120")
        self.assertEqual([("num", 83102199120.0)], l.get_list_token())

        l = lexer.lex("1")
        self.assertEqual([("num", 1.0)], l.get_list_token())

        # single number
        l = lexer.lex("21890")
        self.assertEqual([("num", 21890.0)], l.get_list_token())

        l = lexer.lex("8321")
        self.assertEqual([("num", 8321.0)], l.get_list_token())

        l = lexer.lex("1")
        self.assertEqual([("num", 1.0)], l.get_list_token())

        # different num zeros prefixing number
        l = lexer.lex("0")
        self.assertEqual([("num", 0)], l.get_list_token())

        l = lexer.lex("00")
        self.assertEqual([("num", 0)], l.get_list_token())

        l = lexer.lex("00000000000000000000000000000000000000000000")
        self.assertEqual([("num", 0)], l.get_list_token())

        l = lexer.lex("00000000000000000000000000000000000000000000 ")
        self.assertEqual([("num", 0)], l.get_list_token())

        # multiple numbers
        l = lexer.lex("13 82109 319020921090")
        self.assertEqual([("num", 13), ("num", 82109), ("num", 319020921090)], l.get_list_token())

        l = lexer.lex("120 99991 1890212012")
        self.assertEqual([("num", 120), ("num", 99991), ("num", 1890212012)], l.get_list_token())

        l = lexer.lex("210 2192 8108210 992199")
        self.assertEqual([("num", 210), ("num", 2192), ("num", 8108210), ("num", 992199)], l.get_list_token())

    # file contains only identifiers
    def test_identifier (self):
        # single identifier
        l = lexer.lex("count")
        self.assertEqual([("identifier", "count")], l.get_list_token())

        l = lexer.lex("x")
        self.assertEqual([("identifier", "x")], l.get_list_token())

        l = lexer.lex("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.assertEqual([("identifier", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")], l.get_list_token())

        # spaces before and after identifier
        l = lexer.lex("           bruh             ")
        self.assertEqual([("identifier", "bruh")], l.get_list_token())

        # multiple identifier
        l = lexer.lex("read the words in my mouth")
        self.assertEqual([("identifier", "read"), ("identifier", "the"),
            ("identifier", "words"), ("identifier", "in"), ("identifier", "my"),
            ("identifier", "mouth")], l.get_list_token())

        # multiple identifier with spaces
        l = lexer.lex("   abc    ANS     WHAT IT    fudge         black         ")
        self.assertEqual([("identifier", "abc"), ("identifier", "ANS"),
            ("identifier", "WHAT"), ("identifier", "IT"), ("identifier", "fudge"),
            ("identifier", "black")], l.get_list_token())

    # file contains only math operator
    def test_mathop (self):
        # single operators
        l = lexer.lex("+")
        self.assertEqual([("mathop", "+")], l.get_list_token())

        l = lexer.lex("-")
        self.assertEqual([("mathop", "-")], l.get_list_token())

        l = lexer.lex("*")
        self.assertEqual([("mathop", "*")], l.get_list_token())

        l = lexer.lex("/")
        self.assertEqual([("mathop", "/")], l.get_list_token())

        # multiple operators
        l = lexer.lex("+-/*")
        self.assertEqual([("mathop", "+"), ("mathop", "-"), ("mathop", "/"),
        ("mathop", "*")], l.get_list_token())

        l = lexer.lex("--- --- ")
        self.assertEqual([("mathop", "-"), ("mathop", "-"), ("mathop", "-"),
        ("mathop", "-"), ("mathop", "-"), ("mathop", "-")], l.get_list_token())

        l = lexer.lex("** //")
        self.assertEqual([("mathop", "*"), ("mathop", "*"), ("mathop", "/"), ("mathop", "/")], l.get_list_token())

        # multiple operator with spaces
        l = lexer.lex("    +++            -/   * ")
        self.assertEqual([("mathop", "+"), ("mathop", "+"), ("mathop", "+"),
        ("mathop", "-"), ("mathop", "/"),
        ("mathop", "*")], l.get_list_token())

    # file contains only paranthesis
    def test_paranthesis (self):
        l = lexer.lex("(")
        self.assertEqual([("paranthesis", "(")], l.get_list_token())

        l = lexer.lex(")")
        self.assertEqual([("paranthesis", ")")], l.get_list_token())

        # spaces for single
        l = lexer.lex("   (     ")
        self.assertEqual([("paranthesis", "(")], l.get_list_token())
        l = lexer.lex("  )         ")
        self.assertEqual([("paranthesis", ")")], l.get_list_token())

        # multiple paranthesis
        l = lexer.lex("() ")
        self.assertEqual([("paranthesis", "("), ("paranthesis", ")")], l.get_list_token())

        l = lexer.lex("((())) ")
        self.assertEqual([("paranthesis", "("), ("paranthesis", "("), ("paranthesis", "("),
         ("paranthesis", ")"), ("paranthesis", ")"), ("paranthesis", ")")], l.get_list_token())

        # multiple spaces and multiple paranthesis
        l = lexer.lex("   ()(  )((  ((   )))     )")
        self.assertEqual([("paranthesis", "("), ("paranthesis", ")"), ("paranthesis", "("),
        ("paranthesis", ")"), ("paranthesis", "("), ("paranthesis", "("), ("paranthesis", "("),
        ("paranthesis", "("), ("paranthesis", ")"), ("paranthesis", ")"), ("paranthesis", ")"),
        ("paranthesis", ")")], l.get_list_token())

    # file contains only equaliy token
    def test_equal (self):
        l = lexer.lex("=")
        self.assertEqual([("equality", "=")], l.get_list_token())

        l = lexer.lex(" =")
        self.assertEqual([("equality", "=")], l.get_list_token())

        l = lexer.lex("= ")
        self.assertEqual([("equality", "=")], l.get_list_token())

        l = lexer.lex(" = ")
        self.assertEqual([("equality", "=")], l.get_list_token())

        l = lexer.lex(" = = = == = === ")
        self.assertEqual([("equality", "="), ("equality", "="), ("equality", "=")
        , ("equality", "="), ("equality", "="), ("equality", "="), ("equality", "=")
        ,("equality", "="), ("equality", "=")], l.get_list_token())

    # file contains only semicolon
    def test_semicolon(self):
        l = lexer.lex(";")
        self.assertEqual([("semicolon", ";")], l.get_list_token())

        l = lexer.lex(" ;")
        self.assertEqual([("semicolon", ";")], l.get_list_token())

        l = lexer.lex("; ")
        self.assertEqual([("semicolon", ";")], l.get_list_token())

        l = lexer.lex(" ; ")
        self.assertEqual([("semicolon", ";")], l.get_list_token())

        l = lexer.lex(" ;; ; ;;  ;;;;")
        self.assertEqual([("semicolon", ";"), ("semicolon", ";"), ("semicolon", ";")
        , ("semicolon", ";"), ("semicolon", ";"), ("semicolon", ";"), ("semicolon", ";")
        ,("semicolon", ";"), ("semicolon", ";")], l.get_list_token())

    # file contains only print statement
    def test_print(self):
        l = lexer.lex("print")
        self.assertEqual([("Print", "print")], l.get_list_token())

        l = lexer.lex(" print")
        self.assertEqual([("Print", "print")], l.get_list_token())

        l = lexer.lex("print ")
        self.assertEqual([("Print", "print")], l.get_list_token())

        l = lexer.lex(" print ")
        self.assertEqual([("Print", "print")], l.get_list_token())

        l = lexer.lex(" print print print printprint")
        self.assertEqual([("Print", "print"), ("Print", "print"), ("Print", "print")
        , ("identifier", "printprint")], l.get_list_token())

        l = lexer.lex("print()")
        self.assertEqual([("Print", "print"), ("paranthesis", "("), ("paranthesis", ")")], l.get_list_token())

    # file contains only string statement
    def test_string(self):
        l = lexer.lex("\"\"")
        self.assertEqual([("string", "")], l.get_list_token())

        l = lexer.lex("\"I am a string!\"")
        self.assertEqual([("string", "I am a string!")], l.get_list_token())

        l = lexer.lex("\"Hello world \"")
        self.assertEqual([("string", "Hello world ")], l.get_list_token())

        l = lexer.lex("\" print (gg);\"")
        self.assertEqual([("string", " print (gg);")], l.get_list_token())

        l = lexer.lex("\" 5 + 3 - 18 / 89 * 69 \"")
        self.assertEqual([("string", " 5 + 3 - 18 / 89 * 69 ")], l.get_list_token())

        l = lexer.lex("\" whatcolorisyourbugati1829122 ; a z jka  aojstyuioqwsmxnbcvbansmxnvbcnxm,.<./?!-+qa 210912n 3189\"")
        self.assertEqual([("string", " whatcolorisyourbugati1829122 ; a z jka  aojstyuioqwsmxnbcvbansmxnvbcnxm,.<./?!-+qa 210912n 3189")], l.get_list_token())

    # file contains only boolean operators and values
    def test_boolean_all (self):
        l = lexer.lex("True ")
        self.assertEqual([("boolean", "True")], l.get_list_token())

        l = lexer.lex("False ")
        self.assertEqual([("boolean", "False")], l.get_list_token())

        l = lexer.lex(" True      False")
        self.assertEqual([("boolean", "True"),  ("boolean", "False")], l.get_list_token())

        l = lexer.lex("False      True       ")
        self.assertEqual([("boolean", "False"),  ("boolean", "True")], l.get_list_token())

        l = lexer.lex("   False True True False    True False   True False True True False False False   ")
        self.assertEqual([("boolean", "False"),  ("boolean", "True"), ("boolean", "True"),
        ("boolean", "False"), ("boolean", "True"), ("boolean", "False"), ("boolean", "True"),
        ("boolean", "False"), ("boolean", "True"), ("boolean", "True"), ("boolean", "False"),
        ("boolean", "False"), ("boolean", "False")], l.get_list_token())

        l = lexer.lex(" and")
        self.assertEqual([("logical_operators", "and")], l.get_list_token())

        l = lexer.lex("or ")
        self.assertEqual([("logical_operators", "or")], l.get_list_token())

        l = lexer.lex(" and or ")
        self.assertEqual([("logical_operators", "and"), ("logical_operators", "or")], l.get_list_token())

        l = lexer.lex(" or and ")
        self.assertEqual([("logical_operators", "or"), ("logical_operators", "and")], l.get_list_token())

        l = lexer.lex(" or and and and or      or or    and or and or ")
        self.assertEqual([("logical_operators", "or"), ("logical_operators", "and"), ("logical_operators", "and"),
        ("logical_operators", "and"), ("logical_operators", "or"), ("logical_operators", "or"),
        ("logical_operators", "or"), ("logical_operators", "and"), ("logical_operators", "or"),
        ("logical_operators", "and"), ("logical_operators", "or")], l.get_list_token())

        l = lexer.lex("   True and False")
        self.assertEqual([("boolean", "True"), ("logical_operators", "and"), ("boolean", "False")], l.get_list_token())

        l = lexer.lex("True and True    ")
        self.assertEqual([("boolean", "True"), ("logical_operators", "and"), ("boolean", "True")], l.get_list_token())

        l = lexer.lex("False or    False")
        self.assertEqual([("boolean", "False"), ("logical_operators", "or"), ("boolean", "False")], l.get_list_token())

        l = lexer.lex("False    or True")
        self.assertEqual([("boolean", "False"), ("logical_operators", "or"), ("boolean", "True")], l.get_list_token())

        l = lexer.lex("   False and True      and False or True and    True or False  ")
        self.assertEqual([("boolean", "False"), ("logical_operators", "and"), ("boolean", "True"),
        ("logical_operators", "and"), ("boolean", "False"), ("logical_operators", "or"), ("boolean", "True"),
        ("logical_operators", "and"), ("boolean", "True"), ("logical_operators", "or"), ("boolean", "False")], l.get_list_token())

    # file contains only datatypes
    def test_datatypes (self):
        l = lexer.lex(" float")
        self.assertEqual([("datatype", "float")], l.get_list_token())

        l = lexer.lex("string ")
        self.assertEqual([("datatype", "string")], l.get_list_token())

        l = lexer.lex(" bool ")
        self.assertEqual([("datatype", "bool")], l.get_list_token())

        l = lexer.lex("bool float string")
        self.assertEqual([("datatype", "bool"), ("datatype", "float"), ("datatype", "string")], l.get_list_token())

        l = lexer.lex(" string bool bool float      string float float string string ")
        self.assertEqual([("datatype", "string"), ("datatype", "bool"), ("datatype", "bool"),
        ("datatype", "float"), ("datatype", "string"), ("datatype", "float"),
        ("datatype", "float"), ("datatype", "string"), ("datatype", "string")], l.get_list_token())

    # file contains only keyword
    def test_keywords (self):
        l = lexer.lex(" if")
        self.assertEqual([("keyword", "if")], l.get_list_token())

        l = lexer.lex("if if ")
        self.assertEqual([("keyword", "if"), ("keyword", "if")], l.get_list_token())

        l = lexer.lex("if if if if if if ")
        self.assertEqual([("keyword", "if"), ("keyword", "if"), ("keyword", "if"), 
        ("keyword", "if"), ("keyword", "if"), ("keyword", "if")], l.get_list_token())


if __name__ == '__main__':

    unittest.main()