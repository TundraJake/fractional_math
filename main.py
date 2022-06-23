import unittest
from src import *
from tests import frac_tests
from parser import Parser

if __name__ == '__main__':
    while True:
        print('Welcome to the fracion calculator! \n\t Built with Python 3.8.4!')
        print('')
        print('Commands:')
        print('')
        print('\t tests: run all tests \n\t calc: enter calculator \n\t quit: quit the program')
        print('')
        user_input = input('\nEnter a command: ')
        if user_input == 'tests':
            suite = unittest.TestLoader().loadTestsFromModule(frac_tests)
            unittest.TextTestRunner(verbosity=2).run(suite)
        elif user_input == 'calc':
            
            exp = ''
            parser = Parser()
            while exp != 'exit':
                exp = input('? ')

                if not exp:
                    print('exiting calculator')
                    break
                else:
                    try:
                        print()
                    except Exception as e:
                        print(e)
                
        elif user_input == 'quit':
            print('Good bye!')
            exit()
        else:
            print('Invalid command')
