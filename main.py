from parser import Parser
import unittest
from unittest.case import TestCase
from parser import Parser
from expression import Expression
import random
import string

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

    def test_long_simple_expression_1(self):
        exp = Expression('1 + 5 + 10')
        self.assertEqual(exp.get_expression_string(), '1+5+10')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  2)
        self.assertEqual(parser.get_number_count(),  3)

    def test_long_simple_expression_2(self):
        exp = Expression('1 - 5 * 10')
        self.assertEqual(exp.get_expression_string(), '1-5*10')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  2)
        self.assertEqual(parser.get_number_count(),  3)
                
    def test_long_simple_expression_3(self):
        exp = Expression('1 - 5 * 10 + 1/1')
        self.assertEqual(exp.get_expression_string(), '1-5*10+1/1')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  4)
        self.assertEqual(parser.get_number_count(),  5)
                
                

class Test_Simple_Operations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual('1 + 1', 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)