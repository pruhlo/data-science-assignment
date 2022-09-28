#!/usr/bin/env python
# coding: utf-8

# Напишіть програму, яка виконує такі кроки:
# * запросити користувача ввести чотирицифрове число (наприклад, 8473) (вважаємо, що користувач завжди вводить чотирицифрові числа)
# * змінній number присвоїти введене значення (саме як ціле число, тобто об'єкт відповідного типу)
# * змінній digit1 присвоїти значення 1-ої цифри числа 8473, тобто 8 (це треба порахувати зі змінної number)
# * змінній digit2 присвоїти значення 2-ої цифри числа 8473, тобто 4 (це треба порахувати зі змінної number)
# * змінній digit3 присвоїти значення 3-ої цифри числа 8473, тобто 7 (це треба порахувати зі змінної number)
# * змінній digit4 присвоїти значення 4-ої цифри числа 8473, тобто 3 (це треба порахувати зі змінної number)
# * вивести кожну цифру окремо на новому рядку  
# 
# Використовуйте розглянуті арифметичні оператори.
# 
# Ви не знаєте з яким саме числом працюєте. Ви знаєте тільки те, що в ньому є 4 цифри.
# 
# Завантажте файл з розширенням .py.

def check_input():
    """
    Return four-digit number
    
    Argument:
    number - input four-digit number
    """
    number = input('Enter four-digit number :')
    if len(number) != 4:
        print("Entered isn't four-digit number, try again ")
        check_input()
    else:
        try:
            number = int(number)
            return str(number)
        except ValueError:
            print('Invalid four-digit number, try again ')
            check_input()
        
def get_arguments():
    """Return each digit of the four-digit number"""
    string_number = check_input()
    if string_number == None:
        print('Something went wrong, try again')
        string_number = check_input()
    digit1 = int(string_number[0])
    digit2 = int(string_number[1])
    digit3 = int(string_number[2])
    digit4 = int(string_number[3])
    return digit1, digit2, digit3, digit4

if __name__ == '__main__':
    for count, val in enumerate(get_arguments()):
        print(f'digit{count+1}= {val}')

