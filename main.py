import unittest
from frac_math.exp_evaluator import ExpEvaluator
from frac_math.cli_commands import print_commands, print_greeting, print_invalid_message, print_quiting_message
from tests import frac_tests

if __name__ == '__main__':
    print_greeting()
    print_commands()
    while True:
        user_input = input('\nEnter a command: ')
        if user_input == 'tests':
            suite = unittest.TestLoader().loadTestsFromModule(frac_tests)
            unittest.TextTestRunner(verbosity=2).run(suite)
        elif user_input == 'calc':
            print('Enter \'quit\' to exit...')
            exp = ''
            while exp != 'exit':
                exp = input('? ')

                if exp == 'quit':
                    print('Exiting calculator')
                    print_commands()
                    break
                else:
                    try:
                       evaluator = ExpEvaluator(exp)
                       evaluator.calculate()
                       print(f'> {evaluator.get_calculation()}')
                    except Exception as e:
                        print(e)
                
        elif user_input == 'quit':
            print_quiting_message()
        elif user_input == 'help':
            print_commands()
        else:
            print_invalid_message()
