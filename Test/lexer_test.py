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

        # single number - neg
        l = lexer.lex("-21890")
        self.assertEqual([("num", -21890.0)], l.get_list_token())

        l = lexer.lex("-8321")
        self.assertEqual([("num", -8321.0)], l.get_list_token())

        l = lexer.lex("-1")
        self.assertEqual([("num", -1.0)], l.get_list_token())

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

        l = lexer.lex("-120 -99991 -1890212012")
        self.assertEqual([("num", -120), ("num", -99991), ("num", -1890212012)], l.get_list_token())

        # mixed numbers
        l = lexer.lex("210 -2192 8108210 -992199")
        self.assertEqual([("num", 210), ("num", -2192), ("num", 8108210), ("num", -992199)], l.get_list_token())










if __name__ == '__main__':

    unittest.main()