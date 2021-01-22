"""
Input example for math.
"""
import sys

def main():
    """
    Do math.
    """
    print('Hello to my awesome addition script.')

    try:
        input_1 = input('Enter the first number: ')
        input_2 = input('Enter the second number: ')
    except KeyboardInterrupt:
        print('\nI quit. Bye')
        sys.exit()

    try:
        number_1 = float(input_1)
        number_2 = float(input_2)
        print(number_1 / number_2)
    except ValueError:
        print('Both input values must be numbers.')
    except ZeroDivisionError:
        print("Can't divide by zero. Bro.")

if __name__ == '__main__':
    main()
