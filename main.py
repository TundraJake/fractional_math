import unittest
from parser import Parser
from expression import Expression
from operators import Operations
import random
import string
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

class Test_Parser(unittest.TestCase):
    
    def test_single_char(self):
        exp = Expression('1')
        self.assertEqual(exp.get_expression_string(), '1')
        parser = Parser(exp)
        self.assertEqual(parser.get_number_count(),  1)

    def test_double_char(self):
        exp = Expression('10')
        self.assertEqual(exp.get_expression_string(), '10')
        parser = Parser(exp)
        self.assertEqual(parser.get_number_count(),  1)

    def test_signle_number_n_char(self):
        exp_string = ''.join(random.choice(string.digits) for i in range(9))
        exp = Expression(exp_string)
        self.assertEqual(exp.get_expression_string(), exp_string)
        parser = Parser(exp)
        self.assertEqual(parser.get_number_count(),  1)

    def test_simple_expression(self):
        exp = Expression('1 + 1')
        self.assertEqual(exp.get_expression_string(), '1+1')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  1)
        self.assertEqual(parser.get_number_count(),  2)
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())

    def test_long_simple_expression_1(self):
        exp = Expression('1 + 5 + 10')
        self.assertEqual(exp.get_expression_string(), '1+5+10')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  2)
        self.assertEqual(parser.get_number_count(),  3)
        self.assertEqual(parser.get_number(0),  '1')
        self.assertEqual(parser.get_number(1),  '5')
        self.assertEqual(parser.get_number(2),  '10')
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.ADD, parser.print_operators())

    def test_long_simple_expression_2(self):
        exp = Expression('1 - 5 * 10')
        self.assertEqual(exp.get_expression_string(), '1-5*10')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  2)
        self.assertEqual(parser.get_number_count(),  3)
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.MUL, parser.print_operators())
                
    def test_long_simple_expression_3(self):
        exp = Expression('1 - 5 * 10 + 1/1')
        self.assertEqual(exp.get_expression_string(), '1-5*10+1/1')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  3)
        self.assertEqual(parser.get_number_count(),  4)

    def test_fraction_1(self):
        exp = Expression('1/5')
        self.assertEqual(exp.get_expression_string(), '1/5')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  0)
        self.assertEqual(parser.get_number_count(),  1)
        self.assertEqual(parser.get_number(0), '1/5' , parser.print_numbers())

    def test_fraction_2(self):
        exp = Expression('1_1/5')
        self.assertEqual(exp.get_expression_string(), '1_1/5')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  0)
        self.assertEqual(parser.get_number_count(),  1)

    def test_fraction_3(self):
        exp = Expression('1_1/5 + 1_1/5')
        self.assertEqual(exp.get_expression_string(), '1_1/5+1_1/5')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  1)
        self.assertEqual(parser.get_number_count(),  2)
                                
    def test_fraction_4(self):
        exp = Expression('1_1/5 + 1_1/5 * 1_1/6')
        self.assertEqual(exp.get_expression_string(), '1_1/5+1_1/5*1_1/6')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  2)
        self.assertEqual(parser.get_number_count(),  3)

    def test_negative_number(self):
        exp = Expression('-1')
        self.assertEqual(exp.get_expression_string(), '-1')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 0, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  1, parser.print_numbers())

    def test_double_negative_1(self):
        exp = Expression('1--1')
        self.assertEqual(exp.get_expression_string(), '1--1')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())

    def test_double_negative_2(self):
        exp = Expression('1--1+1 + 5 +10')
        self.assertEqual(exp.get_expression_string(), '1--1+1+5+10')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 4, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  5, parser.print_numbers())

    def test_negative_fraction(self):
        exp = Expression('-1_1/5')
        self.assertEqual(exp.get_expression_string(), '-1_1/5')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 0, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  1, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())

    def test_multiple_negative_fractions(self):
        exp = Expression('-1_1/5 - 1_1/6')
        self.assertEqual(exp.get_expression_string(), '-1_1/5-1_1/6')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-1_1/6', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())        

    def test_multiple_negative_fractions_with_double_negative_1(self):
        exp = Expression('-1_1/5 -- 1_1/7')
        self.assertEqual(exp.get_expression_string(), '-1_1/5--1_1/7')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-1_1/7', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())

    def test_multiple_negative_fractions_with_double_negative_2(self):
        exp = Expression('-1_1/5 -- 1_1/7 + 4 * 7_1/2 - 3/4')
        self.assertEqual(exp.get_expression_string(), '-1_1/5--1_1/7+4*7_1/2-3/4')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 4, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  5, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-1_1/7', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '4', parser.print_numbers())
        self.assertEqual(parser.get_number(3), '7_1/2', parser.print_numbers())
        self.assertEqual(parser.get_number(4), '-3/4', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_operator(2), Operations.MUL, parser.print_operators())
        self.assertEqual(parser.get_operator(3), Operations.ADD, parser.print_operators())
        
    def test_division_1(self):
        exp = Expression('1/5 / 1/2')
        self.assertEqual(exp.get_expression_string(), '1/5/1/2')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '1/2', parser.print_numbers())

    def test_division_2(self):
        exp = Expression('1_1/5 / 2_1/2')
        self.assertEqual(exp.get_expression_string(), '1_1/5/2_1/2')
        parser = Parser(exp)
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number(0), '1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '2_1/2', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())

    def test_division_3(self):
        exp = Expression('1_1/5 / 2_1/2 / -3_1/3')
        self.assertEqual(exp.get_expression_string(), '1_1/5/2_1/2/-3_1/3')
        parser = Parser(exp)
        self.assertEqual(parser.get_number_count(),  3, parser.print_numbers())
        self.assertEqual(parser.get_operator_count(), 2, parser.print_operators())
        self.assertEqual(parser.get_number(0), '1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '2_1/2', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '-3_1/3', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.DIV, parser.print_operators())

    def test_division_4(self):
        exp = Expression('-1_1/5 / -2_1/2 / -3_1/3')
        self.assertEqual(exp.get_expression_string(), '-1_1/5/-2_1/2/-3_1/3')
        parser = Parser(exp)
        self.assertEqual(parser.get_number_count(),  3, parser.print_numbers())
        self.assertEqual(parser.get_operator_count(), 2, parser.print_operators())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-2_1/2', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '-3_1/3', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.DIV, parser.print_operators())

    def test_division_5(self):
        exp = Expression('-1/5 / -1/2')
        self.assertEqual(exp.get_expression_string(), '-1/5/-1/2')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-1/2', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())

class Test_Simple_Operations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual('1 + 1', 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)