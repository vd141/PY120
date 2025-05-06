'''
exception exercises
'''

def first_divided_by_second():
    try:
        first = float(input('Enter the first number: '))
        second = float(input('Enter the second number: '))
        result = first / second
    except (ZeroDivisionError, ValueError) as e:
        print(e)
    else:
        print(result)
    finally:
        print('End of the program.')

# first_divided_by_second()

class NegativeNumberError(Exception):
    pass

def ask_for_number():
    answer = input('Enter a number: ')
    number = float(answer)
    if number < 0:
        raise NegativeNumberError('Number must be positive!')
    print(f'You entered {number}!')

# ask_for_number()

def return_inverse_of_list_elements(a_list):
    new_list = []

    for element in a_list:
        try:
            new_list.append(1/element)
        except ZeroDivisionError:
            print('Zero detected. Inverse coerced to infinity.')
            new_list.append(float('inf'))
        except TypeError:
            print(f'Element {element} must be a float or int.')
    print(new_list)

# return_inverse_of_list_elements([1, 'e', 3, 0])

students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return('Student not found')

# for student in students:
#     print(get_age(student))

# print(get_age('Jerome'))

numbers = [1, 2, 3, 4, 5]

def lbyl_6(numbers):
    if len(numbers) >= 6:
        return numbers[5]
    print('Index 6 does not exist.')
    
def afnp_6(numbers):
    try:
        return numbers[5]
    except IndexError:
        print('Index 6 does not exist.')

print(lbyl_6(numbers))
print(afnp_6(numbers))