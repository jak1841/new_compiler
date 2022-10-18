import sys

# Adding the src directory to the enviroment variable
sys.path.append('/mnt/c/Users/Jaskarn Dhillon/projects/compiler/new_compiler/src')

import unittest
import lexer
import syntax_analysis

class code_generation(unittest.TestCase):
    output_file = "Test/output_from_program.txt"

    # given a name of a file returns a list of lines of that file
    def get_content_file(self, name):
        with open(name, 'r') as f:
            return f.readlines()



    # given a string which is assumed to be the code will run it and redirect output to output file
    def run_string(self, str):
        # No whitespace
        lex = lexer.lex(str)
        code = syntax_analysis.syn_analysis(lex.get_list_token())

        with open(self.output_file,'w') as f:
            temp = sys.stdout
            sys.stdout = f
            code.execute_program()
            sys.stdout = temp



    # tests the print statements
    def test_print_statement(self):
        # printing strings
        code = """print(\"hello world\");
                  print (\"china\");
                  print (\"abcdefghijklmnopqrstuvwxyz\") ;
                  print(\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\") ;
                  print(\"1234567890 + 91032 / 81012 * 3829\");
                  print(\"///,sa.,.,as.,12w, dkmdkqewd c{{}[][]}}}])\--==++**/<>^$%#&*@#!$,.\");
                  print(\"()())))((()))\");
                  print(";;;;;");
                                            """
        self.run_string(code)
        self.assertEqual(["hello world\n", "china\n", "abcdefghijklmnopqrstuvwxyz\n",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ\n", "1234567890 + 91032 / 81012 * 3829\n",
        "///,sa.,.,as.,12w, dkmdkqewd c{{}[][]}}}])\--==++**/<>^$%#&*@#!$,.\n",
        "()())))((()))\n", ";;;;;\n" ], self.get_content_file(self.output_file))

        # printing math expressions
        code = """print(1234567890);
                  print ( 1+1);
                  print (819 -210) ;
                  print(9013 * 7218) ;
                  print(911/420/69);
                  print(66 * (89 - 89*2/89)* (9120-9119));
                  print(8219/8120*(2910+2019) -9120);
                                            """
        self.run_string(code)
        self.assertEqual(["1234567890.0\n", "2.0\n", "609.0\n",
        "65055834.0\n", "0.031435472739820565\n","5742.0\n","-4130.905049261084\n" ],
        self.get_content_file(self.output_file))

        # printing identfiers
        # printing math expressions
        code = """
                    x = 920;
                    y = "heehjiedwnodnjdskdsnndksjnflnsdkf";
                    z = "1 + 3203 /283 &28b 302-";
                    w = (0 - 1)*((123 + 8329) *2/ (911-910));
                    print(x);
                    print(y);
                    print(z);
                    print(w);
                                            """
        self.run_string(code)
        self.assertEqual(["920.0\n", "heehjiedwnodnjdskdsnndksjnflnsdkf\n", "1 + 3203 /283 &28b 302-\n",
        "-16904.0\n",],self.get_content_file(self.output_file))






    # testing the mathexpression function
    def test_math_expression(self):
        # basic math operations (+-*/, (), )
        code = """print(129 + 313);
                  print (1921 -21920);
                  print (931000 * 219) ;
                  print(821919295/ 5) ;
                  print(17 - 2910 - 8192 + 238923 -23 + 320-32);
                  print(82198311 - 82392 * 2389/ 2389 + (0 - 9120));
                  print((((((892)* 7)-910)+9210)/8)*999);
                  print((93290) -9203 /(424*324*234) *(234 *324*424));
                                            """
        self.run_string(code)
        self.assertEqual(["442.0\n", "-19999.0\n", "203889000.0\n",
        "164383859.0\n", "228103.0\n", "82106799.0\n","1816182.0\n",
         "84087.0\n"], self.get_content_file(self.output_file))

        # identifiers in math expressions
        code = """
                    x = (319201 + 021- 92012);
                    y = 8128 -2910 *21891 + 2021;
                    z = (10202/202) + 9210*2;
                    print(x);
                    print(y);
                    print(z);
                    w = x + y + z;
                    print((w));
                    print(x + y - (w - z));
                    print((x * x + y) + 321);
                    print(328192 - 1 * z);


                                            """
        self.run_string(code)
        self.assertEqual(["227210.0\n", "-63692661.0\n", "18470.50495049505\n",
        "-63446980.49504951\n", "0.0\n", "51560691760.0\n","309721.49504950497\n",
         ], self.get_content_file(self.output_file))



if __name__ == '__main__':
    print("\n CODE_GENERATION TEST \n")
    unittest.main()
