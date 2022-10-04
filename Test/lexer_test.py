import sys

# Adding the src directory to the enviroment variable
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/compiler/new_compiler/src')

import unittest
import lexer


class lexer_test(unittest.TestCase):
    def test_empty_file(self):
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






    def test_only_numbers(self):
        self.assertEqual(5, 5)


if __name__ == '__main__':

    unittest.main()