def divide_by_second():
    try:
        first = float(input('Enter first number: '))
        second = float(input('Enter second number: '))
        first / second
    except (ZeroDivisionError, ValueError) as e:
        print(f'Error. {e}')
    else:
        print(f'Result is: {first / second}.')
    finally:
        print('End of program')

# divide_by_second()
class NegativeNumberError(ValueError):
    pass

def ask_for_number():
    try:
        number = float(input('Enter a number: '))
    except ValueError as e:
        print(e)
    else:
        if number < 0:
            raise NegativeNumberError('Number must be positive!')
        print(f'You entered {number}')

# ask_for_number()

# def return_inverse_of_list(a_list):
#     try:
#         return [1/n for n in a_list]
#     except ZeroDivisionError as e:
#         print(e)
#     except TypeError as e:
#         print(e)
#     except:
#         print('invalid element')

def invert_numbers(numbers):
    result = []
    for num in numbers:
        try:
            result.append(1 / num)
        except ZeroDivisionError:
            result.append(float('inf'))  # or handle as desired

    return result

numbers = [1, 2, 0, 3, 4]
print(invert_numbers(numbers))
# [1.0, 0.5, inf, 0.3333333333333333, 0.25]