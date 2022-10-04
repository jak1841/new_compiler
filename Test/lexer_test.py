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
        # single numbers
        l = lexer.lex("7439")
        self.assertEqual([("num", 7439.0)], l.get_list_token())

        l = lexer.lex("-21890")
        self.assertEqual([("num", -21890.0)], l.get_list_token())

        l = lexer.lex("0")
        self.assertEqual([("num", 0)], l.get_list_token())








if __name__ == '__main__':

    unittest.main()