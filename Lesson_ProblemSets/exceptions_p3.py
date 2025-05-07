'''
problem sets: exceptions
'''

def divide_by_second():
    try:
        first = float(input('Enter the first number: '))
        second = float(input('Enter the second number: '))
        result = first / second
    except (ZeroDivisionError, ValueError) as e:
        print(e)
    else:
        print(result)
    finally:
        print('End of the program')

# divide_by_second()

class NegativeNumberError(ValueError):
    pass

def ask_for_number():
    number = input('Enter a number: ')
    numerical = float(number)
    if numerical < 0:
        raise NegativeNumberError('Number must be positive!')
    print(f'The number is {numerical}.')

# ask_for_number()

def return_inverse_of_elements(a_list):
    new_list = []

    for element in a_list:
        try:
            new_list.append(1/element)
        except ZeroDivisionError:
            new_list.append(float('inf'))
        except TypeError:
            new_list.append(float(element))
    return new_list

# print(return_inverse_of_elements([1, 2, 3, 4, 5, 0, 'inf']))

students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return('Student not found.')

# for student in students:
    # print(get_age(student))
# print(get_age('Daquan'))

numbers = [1, 2, 3, 4, 5, 6]

def lbyl(numbers):
    if len(numbers) > 5:
        return numbers[5]

def afnp(numbers):
    try:
        return numbers[5]
    except IndexError:
        return None

# print(lbyl(numbers))
# print(afnp(numbers))