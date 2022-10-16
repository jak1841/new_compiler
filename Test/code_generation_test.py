import sys

# Adding the src directory to the enviroment variable
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/compiler/new_compiler/src')

import unittest
import lexer
import syntax_analysis

class code_generation(unittest.TestCase):
    # given a string which is assumed to be the code will run it
    def run_string(self, str):
        # No whitespace
        lex = lexer.lex(str)
        code = syntax_analysis.syn_analysis(lex.get_list_token())

        code.execute_program()

    # testing the mathexpression function
    def test_math_expression(self):
        code = """print(\"hello test\");"""

        self.run_string(code)


if __name__ == '__main__':
    print("\n CODE_GENERATION TEST \n")
    unittest.main()
