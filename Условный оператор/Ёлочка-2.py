lst = [input() + ' ' for _ in range(3)]
lst = ''.join(lst)


if (lst == 'раз два три ') or (lst == '1 2 3 '):
    print('ГОРИ')
else:
    print('НЕ ГОРИ')