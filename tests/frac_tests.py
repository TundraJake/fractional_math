import unittest
from frac_math.parser import Parser

from frac_math.expression import Expression
from frac_math.operators import Operations
from frac_math.exp_evaluator import ExpEvaluator
import random
import string


class Test_Parser(unittest.TestCase):
    
    def test_single_char(self):
        exp = Expression('1')
        self.assertEqual(exp.get_expression(), '1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_number_count(),  1)
        self.assertEqual(parser.get_element_count(),  1)

    def test_starting_double_negative(self):
        exp = Expression('--1')
        self.assertEqual(exp.get_expression(), '--1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_number_count(),  1)
        self.assertEqual(parser.get_element_count(),  1)

    def test_double_char(self):
        exp = Expression('10')
        self.assertEqual(exp.get_expression(), '10')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_number_count(),  1)

    def test_signle_number_n_char(self):
        exp_str = ''.join(random.choice(string.digits) for i in range(9))
        exp = Expression(exp_str)
        self.assertEqual(exp.get_expression(), exp_str)
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_number_count(),  1)

    def test_simple_expression(self):
        exp = Expression('1 + 1')
        self.assertEqual(exp.get_expression(), '1+1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  1)
        self.assertEqual(parser.get_number_count(),  2)
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  3)

    def test_simple_subtraction_expression(self):
        exp = Expression('1 - 1')
        self.assertEqual(exp.get_expression(), '1-1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  1)
        self.assertEqual(parser.get_number_count(),  2)
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  3)

    def test_long_simple_expression_1(self):
        exp = Expression('1 + 5 + 10')
        self.assertEqual(exp.get_expression(), '1+5+10')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  2)
        self.assertEqual(parser.get_number_count(),  3)
        self.assertEqual(parser.get_number(0),  '1')
        self.assertEqual(parser.get_number(1),  '5')
        self.assertEqual(parser.get_number(2),  '10')
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.ADD, parser.print_operators())

    def test_long_simple_expression_2(self):
        exp = Expression('1 - 5 * 10')
        self.assertEqual(exp.get_expression(), '1-5*10')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  2)
        self.assertEqual(parser.get_number_count(),  3)
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.MUL, parser.print_operators())
                
    def test_long_simple_expression_3(self):
        exp = Expression('1 - 5 * 10 + 1/1')
        self.assertEqual(exp.get_expression(), '1-5*10+1/1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  4)
        self.assertEqual(parser.get_number_count(),  5)

    def test_fraction_1(self):
        exp = Expression('1/5')
        self.assertEqual(exp.get_expression(), '1/5')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  1)
        self.assertEqual(parser.get_number_count(),  2)
        self.assertEqual(parser.get_number(0), '1' , parser.print_numbers())
        self.assertEqual(parser.get_number(1), '5' , parser.print_numbers())

    def test_fraction_2(self):
        exp = Expression('1_1/5')
        self.assertEqual(exp.get_expression(), '1_1/5')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  0)
        self.assertEqual(parser.get_number_count(),  1)

    def test_fraction_3(self):
        exp = Expression('1_1/5 + 1_1/5')
        self.assertEqual(exp.get_expression(), '1_1/5+1_1/5')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  1)
        self.assertEqual(parser.get_number_count(),  2)
                                
    def test_fraction_4(self):
        exp = Expression('1_1/5 + 1_1/5 * 1_1/6')
        self.assertEqual(exp.get_expression(), '1_1/5+1_1/5*1_1/6')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(),  2)
        self.assertEqual(parser.get_number_count(),  3)

    def test_negative_number(self):
        exp = Expression('-1')
        self.assertEqual(exp.get_expression(), '-1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 0, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  1, parser.print_numbers())

    def test_double_negative_1(self):
        exp = Expression('1--1')
        self.assertEqual(exp.get_expression(), '1--1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())

    def test_double_negative_2(self):
        exp = Expression('1--1+1 + 5 +10')
        self.assertEqual(exp.get_expression(), '1--1+1+5+10')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 4, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  5, parser.print_numbers())

    def test_negative_fraction(self):
        exp = Expression('-1_1/5')
        self.assertEqual(exp.get_expression(), '-1_1/5')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 0, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  1, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())

    def test_multiple_negative_fractions(self):
        exp = Expression('-1_1/5 - 1_1/6')
        self.assertEqual(exp.get_expression(), '-1_1/5-1_1/6')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-1_1/6', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())        

    def test_multiple_negative_fractions_with_double_negative_1(self):
        exp = Expression('-1_1/5 -- 1_1/7')
        self.assertEqual(exp.get_expression(), '-1_1/5--1_1/7')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '1_1/7', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())

    def test_multiple_negative_fractions_with_double_negative_2(self):
        exp = Expression('-1_1/5 -- 1_1/7 + 4 * 7_1/2 - 3/4')
        self.assertEqual(exp.get_expression(), '-1_1/5--1_1/7+4*7_1/2-3/4')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 5, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  6, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '1_1/7', parser.print_numbers())
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
        self.assertEqual(exp.get_expression(), '1/5/1/2')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 3, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  4, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '5', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(3), '2', parser.print_numbers())

    def test_division_2(self):
        exp = Expression('1_1/5 / 3_1/2')
        self.assertEqual(exp.get_expression(), '1_1/5/3_1/2')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number(0), '1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '3_1/2', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())

    def test_division_3(self):
        exp = Expression('1_1/5 / 2_1/2 / -3_1/3')
        self.assertEqual(exp.get_expression(), '1_1/5/2_1/2/-3_1/3')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_number_count(),  3, parser.print_numbers())
        self.assertEqual(parser.get_operator_count(), 2, parser.print_operators())
        self.assertEqual(parser.get_number(0), '1_1/5', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '2_1/2', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '-3_1/3', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_operator(1), Operations.DIV, parser.print_operators())

    def test_division_4(self):
        exp = Expression('-1_1/5 / -2_1/2 / -3_1/3')
        self.assertEqual(exp.get_expression(), '-1_1/5/-2_1/2/-3_1/3')
        parser = Parser()
        parser.set_expression(exp)
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
        self.assertEqual(exp.get_expression(), '-1/5/-1/2')
        parser = Parser()
        parser.set_expression(exp)
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
        self.assertEqual(exp.get_expression(), '1/23/1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 2, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  3, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '23', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '1', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  5)

    def test_division_7(self):
        exp = Expression('-21 / -2')
        self.assertEqual(exp.get_expression(), '-21/-2')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 1, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  2, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '-21', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-2', parser.print_numbers())
        self.assertEqual(parser.get_element_count(),  3)

    def test_division_8(self):
        exp = Expression('1/ 2 / 1')
        self.assertEqual(exp.get_expression(), '1/2/1')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 2, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  3, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '2', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '1', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  5)

    def test_fraction_addition(self):
        exp = Expression('1/2 + 1/2')
        self.assertEqual(exp.get_expression(), '1/2+1/2')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 3, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  4, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '2', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '1', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '2', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.DIV, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  7)      

    def test_fraction_addition_and_subtraction(self):
        exp = Expression('1_1/2 - 1_1/2 + 1_1/2')
        self.assertEqual(exp.get_expression(), '1_1/2-1_1/2+1_1/2')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 2, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  3, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1_1/2', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '-1_1/2', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '1_1/2', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.ADD, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  5)      

    def test_several_double_negatives_with_multiplication(self):
        exp = Expression('--1_23/54 * --17/8 * -2/5 * --12/7')
        self.assertEqual(exp.get_expression(), '--1_23/54*--17/8*-2/5*--12/7')
        parser = Parser()
        parser.set_expression(exp)
        self.assertEqual(parser.get_operator_count(), 6, parser.print_operators())
        self.assertEqual(parser.get_number_count(),  7, parser.print_numbers())
        self.assertEqual(parser.get_number(0), '1_23/54', parser.print_numbers())
        self.assertEqual(parser.get_number(1), '17', parser.print_numbers())
        self.assertEqual(parser.get_number(2), '8', parser.print_numbers())
        self.assertEqual(parser.get_number(3), '-2', parser.print_numbers())
        self.assertEqual(parser.get_number(4), '5', parser.print_numbers())
        self.assertEqual(parser.get_number(5), '12', parser.print_numbers())
        self.assertEqual(parser.get_number(6), '7', parser.print_numbers())
        self.assertEqual(parser.get_operator(0), Operations.MUL, parser.print_operators())
        self.assertEqual(parser.get_element_count(),  13)     

class Test_Simple_Operations(unittest.TestCase):

    def test_single_number_evaluation_01(self):
        exp = '1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1')

    def test_single_number_evaluation_02(self):
        exp = '-1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1')

    def test_single_number_evaluation_03(self):
        exp = '1_1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1_1/2')

    def test_single_number_evaluation_04(self):
        exp = '-1_1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1_1/2')

    def test_single_number_evaluation_05(self):
        exp = '--1_1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1_1/2')

    def test_single_number_evaluation_06(self):
        exp = '--4/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2')

    def test_single_number_evaluation_07(self):
        exp = '0'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_single_number_evaluation_08(self):
        exp = '-0'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_single_number_evaluation_09(self):
        exp = '--0'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_single_number_evaluation_10(self):
        exp = '--0_4/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2')

    def test_single_number_evaluation_11(self):
        exp = '1_4/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '3')

    def test_single_number_evaluation_12(self):
        exp = '--1_4/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '3')

    def test_single_number_evaluation_13(self):
        exp = '-1_4/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-3')

    def test_multiple_negative_sign_01(self):
        exp = '----1 --- 1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_multiple_negative_sign_02(self):
        exp = '-----1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1')

    def test_zero_addition_01(self):
        exp = '0 + 0'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_zero_addition_02(self):
        exp = '0 + 0 + 1 + 5'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '6')

    def test_zero_subtraction_01(self):
        exp = '0 - 0'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_zero_subtraction_02(self):
        exp = '0 - 0 - 1 + 5'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '4')

    def test_zero_multiplication_01(self):
        exp = '0 * 0'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_zero_multiplication_02(self):
        exp = '0 * 0 * -1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_zero_multiplication_03(self):
        exp = '0 * 0 * -1 + 5 * 0'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_zero_multiplication_04(self):
        exp = '0 * 0 * -1 + 5 * 5'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '25')

    def test_zero_division_01(self):
        exp = '0 / 5'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_zero_division_02(self):
        exp = '0 / 5 / 25'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_whole_number_addition_01(self):
        exp = '1 + 1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2')

    def test_whole_number_addition_02(self):
        exp = '1 + 1 + 1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '3')

    def test_whole_number_addition_03(self):
        exp = '5 + 24 + 721 + 10 + 40'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '800')

    def test_whole_number_subtraction_01(self):
        exp = '1 - 1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_whole_number_subtraction_02(self):
        exp = '1 - 1 - 1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1')

    def test_whole_number_subtraction_03(self):
        exp = '1 - 1 - 999'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-999')

    def test_whole_number_multiplication_01(self):
        exp = '10 * 10'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '100')

    def test_whole_number_multiplication_02(self):
        exp = '10 * 10 * 10'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1000')

    def test_whole_number_multiplication_03(self):
        exp = '10 * -10 * 10'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1000')

    def test_whole_number_multiplication_04(self):
        exp = '-10 * 10 * -10'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1000')

    def test_whole_number_division_01(self):
        exp = '1 / 2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/2')

    def test_whole_number_division_02(self):
        exp = '1 / 23'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/23')

    def test_whole_number_division_03(self):
        exp = '1 / 23'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/23')

    def test_whole_number_division_04(self):
        exp = '1 / 1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1')
  
    def test_whole_number_division_05(self):
        exp = '25 / 1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '25')

    def test_whole_number_division_06(self):
        exp = '-25 / 1'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-25')

    def test_whole_number_division_07(self):
        exp = '20 / 2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '10')

    def test_whole_number_division_08(self):
        exp = '21 / 2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '10_1/2')

    def test_whole_number_division_09(self):
        exp = '-21 / 2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-10_1/2')

    def test_whole_number_division_10(self):
        exp = '-21 / -2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '10_1/2')

    def test_whole_number_division_11(self):
        exp = '1 / 2 / 2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/4')   

    def test_whole_number_division_12(self):
        exp = '1 / 2 / 2 / 2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/8')

    def test_whole_number_division_13(self):
        exp = '1 / 2 / 2 / 2 / 2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/16')

    def test_whole_number_division_14(self):
        exp = '4 / 2 / 2 '
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1')

    def test_whole_number_division_multiplication_01(self):
        exp = '2 * 2 / 2 '
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2')

    def test_whole_number_division_multiplication_02(self):
        exp = '2 * 2 * 2  / 3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2_2/3')

    def test_whole_number_division_multiplication_03(self):
        exp = '2 * 3 * 3  / 3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '6')

    def test_whole_number_division_multiplication_04(self):
        exp = '2 / 3 * 3  / 3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2/3')

class Test_Moderate_Operations(unittest.TestCase):

    def test_fraction_addition_01(self):
        exp = '1/2 + 1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1')

    def test_fraction_addition_02(self):
        exp = '1/2 + 1/2 + 1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1_1/2')

    def test_fraction_addition_03(self):
        exp = '1/2 + 1/2 + 1/2 + 1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2')

    def test_fraction_addition_04(self):
        exp = '3/2 + 1/2 + 1/2 + 1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '3')

    def test_fraction_addition_05(self):
        exp = '3/2 + 6/5 + 1/2 + 1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '3_7/10')

    def test_fraction_addition_06(self):
        exp = '1_1/2 + 1_1/2 + 1_1/2 + 6_35/67'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '11_3/134')

    def test_fraction_addition_and_subtraction_01(self):
        exp = '1_1/2 - 1_1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_fraction_addition_and_subtraction_02(self):
        exp = '-1_1/2 + 1_1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_fraction_addition_and_subtraction_03(self):
        exp = '-1_1/2 + 1_1/2 + 1_1/2 + 1_1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '3')

    def test_fraction_addition_and_subtraction_04(self):
        exp = '-1_1/2 + 1_1/2 + 1_1/2 + 1_1/2 - 1_24/423'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1_133/141')

    def test_fraction_addition_and_subtraction_05(self):
        exp = '-1_1/2 + 1_1/2 + 1_1/2 -- 1_1/2 - 1_24/423'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1_133/141')

    def test_fraction_addition_and_subtraction_06(self):
        exp = '--1_1/2 + 1_1/2 + 1_1/2 -- 1_1/2 - 1_24/423'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '4_133/141')
        
    def test_fraction_addition_and_subtraction_07(self):
        exp = '--1_1/2 + 1_1/2 + 1_1/2 -- 1_1/2 - 1_24/423 + 1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '5_125/282')

    def test_fraction_multiplication_01(self):
        exp = '1/2 * 1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/4')

    def test_fraction_multiplication_02(self):
        exp = '1/2 * 1/8'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/16')

    def test_fraction_multiplication_03(self):
        exp = '1/2 * 16/8'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1')

    def test_fraction_multiplication_04(self):
        exp = '1/2 * 17/8'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1_1/16')

    def test_fraction_multiplication_05(self):
        exp = '23/54 * 17/8'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '391/432')

    def test_fraction_multiplication_06(self):
        exp = '23/54 * 17/8 * 2/5 * 12/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '391/630')

    def test_fraction_multiplication_07(self):
        exp = '1_23/54 * 17/8 * 2/5 * 12/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2_7/90')

    def test_fraction_multiplication_08(self):
        exp = '--1_23/54 * --17/8 * -2/5 * --12/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-2_7/90')

    def test_fraction_multiplication_09(self):
        exp = '--1_23/54 * --17/8 * --2/5 * --12/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2_7/90')

    def test_fraction_multiplication_10(self):
        exp = '77/54 * (57/8) *  7/5 * 19/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '38_437/720')

    def test_fraction_multiplication_10(self):
        exp = '1_23/54 * 5_17/8 * 1_2/5 * 19/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '38_437/720')

    def test_fraction_multiplication_11(self):
        exp = '1_23/54 * -17/8 * 2/5 * 12/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-2_7/90')

    def test_fraction_multiplication_12(self):
        exp = '1_23/54 * -17/8 * -2/5 * 12/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2_7/90')

    def test_fraction_multiplication_13(self):
        exp = '-1_23/54 * -17/8 * -2/5 * 12/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-2_7/90')

    def test_fraction_multiplication_14(self):
        exp = '-1_23/54 * -17/8 * -2/5 * 5_12/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-8_149/1080')

    def test_fraction_multiplication_14(self):
        exp = '-77/54 * -17/8 * -2/5 * 47/7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-8_149/1080')

    def test_fraction_subtraction_01(self):
        exp = '1/2 - 1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_fraction_subtraction_02(self):
        exp = '1/2 - 1/3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '1/6')

    def test_fraction_subtraction_03(self):
        exp = '1/2 - 1/3 - 1/3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1/6')

    def test_fraction_subtraction_04(self):
        exp = '1/2 - 1/3 - 1/3 - 1/3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1/2')

    def test_fraction_subtraction_05(self):
        exp = '0_1/2 - 0_1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '0')

    def test_fraction_subtraction_06(self):
        exp = '-0_1/2 - 0_1/2'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1')

    def test_fraction_subtraction_07(self):
        exp = '-0_1/2 - 0'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1/2')

    def test_fraction_subtraction_07(self):
        exp = '-0_1/2 - 0 - 34/123 - 1232 / 3 -- 3_1/5'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-408_299/1230')

class Test_Extensive_Operations(unittest.TestCase):

    def test_01(self):
        exp = '1 + 3/4 - 1/2 * 7'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '-1_3/4')

    def test_02(self):
        exp = '1 + 3/4 * 1/2 * 7 / 6 * 3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '2_5/16')

    def test_03(self):
        exp = '--1 + 4_3/4 * 1/2 * 7 / 6 * 3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '9_5/16')

    def test_04(self):
        exp = '--1 + 4_3/4 * 1/2 * --7_1/8 / 6 * 3 --1 --1_2/3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '12_49/384')

    def test_05(self):
        exp = '--10_9/2 + 4_3/4 * 1/2 * --7_8/8 / 9 * 3 --1 --1_2/3'
        rvp = ExpEvaluator(exp)
        rvp.calculate()
        self.assertEqual(rvp.get_calculation(), '23_1/2')

class Test_Bad_Input(unittest.TestCase):

    def test_01(self):
        exp = '*0'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_02(self):
        exp = '-*0'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_03(self):
        exp = '-*+10'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_04(self):
        exp = '10 -* 10'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_05(self):
        exp = '1/0'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_06(self):
        exp = '1/5 + 1/0'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_07(self):
        exp = '1 + 3/4 - 1/2/0 * 7'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_08(self):
        exp = '1 -0_-3/4 * 1/2 * 7 / 6 * 3'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()
   
    def test_09(self):
        exp = '--1 + 4_3/-4 * 1/2 * 7 / 6 * 3'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_10(self):
        exp = '--1 + 4_3/4 * 1/2 * --7_1/8 / 6 * 3 --1 --1_-2/-3'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_11(self):
        exp = '--10_10_9/2 + 4_3/4 * 1/2 * --7_8/8 / 9 * 3 --1 --1_2/3'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_12(self):
        exp = '--10__9/2 + 4_3/4 * 1/2 * --7_8/8 / 9 * 3 --1 --1_2/3'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_13(self):
        exp = 'a'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_14(self):
        exp = '1 + 2a'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_15(self):
        exp = '1 + a'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()


    def test_16(self):
        exp = '1 + @'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_17(self):
        exp = '1 + !'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_18(self):
        exp = '1 + \''
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_19(self):
        exp = '1 + \"'
        with self.assertRaises(Exception) as e:
            rvp = ExpEvaluator(exp)
            rvp.calculate()

    def test_20(self):
        with self.assertRaises(Exception) as e:
            exp = ''
            rvp = ExpEvaluator(exp)
            rvp.calculate()

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)