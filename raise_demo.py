num = input('type a number between 0 and 100: ')

try:
    num = int(num)
except ValueError:
    raise ValueError('number must be between 0 and 100')
else:
    if not (num > 0 and num < 100):
        raise ValueError('number must be between 0 and 100')
    print('you entered', num)
