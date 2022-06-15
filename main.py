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


                

class Test_Simple_Operations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual('1 + 1', 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)