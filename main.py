import unittest
from parser import Parser
from expression import Expression
from operators import Operations
from exp_evaluator import ExpEvaluator
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
        self.assertEqual(parser.get_element_count(),  1)

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
        self.assertEqual(parser.get_element_count(),  3)

    def test_simple_subtraction_expression(self):
        exp = Expression('1 - 1')
        self.assertEqual(exp.get_expression_string(), '1-1')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  1)
        self.assertEqual(parser.get_number_count(),  2)
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  3)


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
        self.assertEqual(parser.get_operator_count(),  4)
        self.assertEqual(parser.get_number_count(),  5)

    def test_fraction_1(self):
        exp = Expression('1/5')
        self.assertEqual(exp.get_expression_string(), '1/5')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(),  1)
        self.assertEqual(parser.get_number_count(),  2)
        self.assertEqual(parser.get_number(0), '1' , parser.print_numbers())
        self.assertEqual(parser.get_number(1), '5' , parser.print_numbers())

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
        self.assertEqual(parser.get_operator_count(), 5, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  6, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-1_1/7', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '4', parser.print_numbers())
        self.assertEqual(parser.get_number(3), '7_1/2', parser.print_numbers())
        self.assertEqual(parser.get_number(4), '-3', parser.print_numbers())
        self.assertEqual(parser.get_number(5), '4', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_operator(2), Operations.MUL, parser.print_operators())
        self.assertEqual(parser.get_operator(3), Operations.ADD, parser.print_operators())
        
    def test_division_1(self):
        exp = Expression('1/5 / 1/2')
        self.assertEqual(exp.get_expression_string(), '1/5/1/2')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 3, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  4, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '5', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(3), '2', parser.print_numbers())

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
        self.assertEqual(parser.get_element_count(),  5)

    def test_division_5(self):
        exp = Expression('-1/5 / -1/2')
        self.assertEqual(exp.get_expression_string(), '-1/5/-1/2')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 3, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  4, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '5', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '-1', parser.print_numbers())
        self.assertEqual(parser.get_number(3), '2', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  7)

    def test_division_6(self):
        exp = Expression('1/ 23 / 1')
        self.assertEqual(exp.get_expression_string(), '1/23/1')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 2, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  3, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '23', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '1', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  5)

    def test_division_7(self):
        exp = Expression('-21 / -2')
        self.assertEqual(exp.get_expression_string(), '-21/-2')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-21', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-2', parser.print_numbers())
        self.assertEqual(parser.get_element_count(),  3)

    def test_division_8(self):
        exp = Expression('1/ 2 / 1')
        self.assertEqual(exp.get_expression_string(), '1/2/1')
        parser = Parser(exp)
        self.assertEqual(parser.get_operator_count(), 2, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  3, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '2', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '1', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  5)        

class Test_Simple_Operations(unittest.TestCase):

    def test_whole_number_addition_1(self):
        exp = Expression('1 + 1')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2')

    def test_whole_number_addition_2(self):
        exp = Expression('1 + 1 + 1')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '3')

    def test_whole_number_addition_3(self):
        exp = Expression('5 + 24 + 721 + 10 + 40')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '800')

    def test_whole_number_subtraction_1(self):
        exp = Expression('1 - 1')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_whole_number_subtraction_2(self):
        exp = Expression('1 - 1 - 1')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1')

    def test_whole_number_subtraction_3(self):
        exp = Expression('1 - 1 - 999')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-999')

    def test_whole_number_multiplication_1(self):
        exp = Expression('10 * 10')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '100')

    def test_whole_number_multiplication_2(self):
        exp = Expression('10 * 10 * 10')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1000')

    def test_whole_number_multiplication_3(self):
        exp = Expression('10 * -10 * 10')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1000')

    def test_whole_number_multiplication_4(self):
        exp = Expression('-10 * 10 * -10')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1000')

    def test_whole_number_division_01(self):
        exp = Expression('1 / 2')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/2')

    def test_whole_number_division_02(self):
        exp = Expression('1 / 23')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/23')

    def test_whole_number_division_03(self):
        exp = Expression('1 / 23')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/23')

    def test_whole_number_division_04(self):
        exp = Expression('1 / 1')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1')

    
    def test_whole_number_division_05(self):
        exp = Expression('25 / 1')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '25')

    def test_whole_number_division_06(self):
        exp = Expression('-25 / 1')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-25')

    def test_whole_number_division_07(self):
        exp = Expression('20 / 2')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '10')


    def test_whole_number_division_08(self):
        exp = Expression('21 / 2')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '10_1/2')


    def test_whole_number_division_09(self):
        exp = Expression('-21 / 2')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-10_1/2')

    def test_whole_number_division_10(self):
        exp = Expression('-21 / -2')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '10_1/2')

    def test_whole_number_division_11(self):
        exp = Expression('1 / 2 / 2')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/4')   

    def test_whole_number_division_12(self):
        exp = Expression('1 / 2 / 2 / 2')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/8')

    def test_whole_number_division_13(self):
        exp = Expression('1 / 2 / 2 / 2 / 2')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/16')

    def test_whole_number_division_14(self):
        exp = Expression('4 / 2 / 2 ')
        parser = Parser(exp)
        rvp = ExpEvaluator(parser)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1')    

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=True)