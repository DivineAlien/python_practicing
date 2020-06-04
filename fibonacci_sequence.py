"""
In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence,
 called the Fibonacci sequence, such that each number is the
 sum of the two preceding ones, starting from 0 and 1.
"""


def fibonacci_sequence(limit: int):
    """
    generate fibonacci sequence of numbers from 0 to n
    using yield to make a generator for efficiency
    :param limit: where the sequence stops
    :return: fibonacci number
    """
    first_number = 0
    second_number = 1

    while first_number <= limit:
        yield first_number
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number


def run():
    """
    asking the user from input to enter a number for sequence limit
    then printing the fibonacci sequence from 0 to limit
    """
    while True:
        try:
            limit = int(input('please enter your limit for fibonacci sequence: \n'))
        except ValueError:
            print('please enter a number!!!')
        else:
            break

    for number in fibonacci_sequence(limit):
        print(number, end=", ")


if __name__ == '__main__':
    run()
