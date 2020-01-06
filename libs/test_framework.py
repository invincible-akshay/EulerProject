class CustomTests:
    """
    A class to hold generic testing functionality for all future questions.
    """
    def __init__(self):
        """
        Initialize the test counter
        """
        self.test_count = 0
        print('** Initialized Tests Class **')

    def run_test(self, *args):
        """
        :param args: variable arguments to handle one or 2 input parameters
        [ func expected input1 input2 ]
        :return: Nothing, print the outcome here itself
        """
        self.test_count += 1
        func = args[0]
        expected = args[1]

        # TODO Is it possible to handle arbitrary number of arguments?
        if len(args) == 3:
            actual = func(args[2])
        elif len(args) == 4:
            actual = func(args[2], args[3])

        print('Test # {0}'.format(self.test_count))
        print('Expected: {0} while actual: {1}'.format(expected, actual))
        if expected == actual:
            print('SuCCESS!')
        else:
            print('FaILURE')
