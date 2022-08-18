# coding:utf-8
def check_input(data):
    correct_type = [float, int]
    for _type_ in correct_type:
        if isinstance(data, _type_):
            return True
        if isinstance(data, str) and not data.isalpha():
            if data.count('.') <= 1:
                return True
        return False


def plus(a, b):
    if check_input(a) and check_input(b):
        return float(a) + float(b)
    else:
        print('please re-enter')


def minus(a, b):
    if check_input(a) and check_input(b):
        return float(a) - float(b)
    else:
        print('please re-enter')


def multiply(a, b):
    if check_input(a) and check_input(b):
        return float(a) + float(b)
    else:
        print('please re-enter')


def division(a, b):
    if check_input(a) and check_input(b):
        return float(a) + float(b)
    else:
        print('please re-enter')


print(plus('3.3', '12.5'))
