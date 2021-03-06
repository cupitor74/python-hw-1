# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перевірить певне число на те чи воно парне або непарне.

# Функція приймає на вхід будь яке число і виводить в консоль строку типу 'Число Х є парним'.
# Наприклад:
#   oddOrEven(1) - > 'Число Х є непарним'
#   oddOrEven(20) - > 'Число Х є парним'
# Можна додавати свої тести за прикладом. Потрібно врахувати обробку можливих помилок.


def oddOrEven(num):
    c = 'парним' if num % 2 == 0 else 'непарним'
    print('Число {} є {}:'.format(num, c))

oddOrEven(1) # 'Число Х є непарним'
oddOrEven(20) # 'Число Х є парним'
