def add_everything_up(a, b):
    try:
        return "{:.3f}".format(a + b)
    except TypeError as axe:
        return f'{a}{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
