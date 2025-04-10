'''
1
'''
# input1 = input('Enter a number to be divided: ')
# input2 = input('Enter a number that the previous input will be divided by: ')

# try:
#     float(input1) / float(input2)
# except ZeroDivisionError:
#     print('Second input must be nonzero!')
# except ValueError:
#     print('Input must be numeric!')


'''
2. previous answer, but prints result only when no exceptions are raised
'''
# input1 = input('Enter a number to be divided: ')
# input2 = input('Enter a number that the previous input will be divided by: ')

# try:
#     result = float(input1) / float(input2)
# except ZeroDivisionError:
#     print('Second input must be nonzero!')
# except ValueError:
#     print('Input must be numeric!')
# else:
#     print(result)
# finally:
#     print('End of the program.')

'''
3.
'''
# input1 = input('Enter a number to be divided: ')
# input2 = input('Enter a number that the previous input will be divided by: ')

# try:
#     result = float(input1) / float(input2)
# except (ZeroDivisionError, ValueError) as e:
#     print(f'Error: {e}')
# else:
#     print(result)
# finally:
#     print('End of the program.')

'''
4. 
'''

# try:
#     in1 = float(input('Enter a number: '))
# except (ValueError):
#     print('Input must be numeric.')
# if in1 < 0:
#     raise ValueError('Input must be nonegative.')

# print(f'Input was: {in1}')

'''
5
'''
# class NegativeNumberError(ValueError):
#     def __init__(self, message):
#         super().__init__(message)

# try:
#     in1 = float(input('Enter a number: '))
# except (ValueError):
#     print('Input must be numeric.')
# if in1 < 0:
#     raise NegativeNumberError('Input must be nonegative.')

# print(f'Input was: {in1}')

'''
6
'''
# def inverse_numbers(numbers):
#     output_list = []
#     for num in numbers:
#         try:
#             output_list.append(1/num)
#         except ZeroDivisionError as e:
#             print('0 division encountered! Replacing with \'inf')
#             output_list.append(float('inf'))
#     return output_list

# print(inverse_numbers([1, 3, 5, 7, 9, 0, 6, 4]))

'''
7

b and c would raise a ZDE (divide by zero). floor division and modulo operations require division
'''

'''
8
'''
# students = {'John': 25, 'Jane': 22, 'Doe': 30}

# def get_age(name):
#     try:
#         return students[name]
#     except KeyError:
#         return 'Student not found'
    
# print(get_age('Naomi'))

'''
9
'''
numbers = [1, 2, 3, 4, 5]

def look_before_you_leap(numbers):
    if len(numbers) >= 6:
        return numbers[5]
    else:
        return 'index not within bounds'

def ask_forgiveness_never_permission(numbers):
    try:
        return numbers[5]
    except IndexError as e:
        return(f'Index not within bounds: {e}')

print(look_before_you_leap(numbers))
print(ask_forgiveness_never_permission(numbers))

'''
10
'''