# Напишіть функцію commonStr що задовільняє наступній умові:



# Дано дві строчки, поверніть нову строчку 
# яка буде складатись виключно зі спільних символів перерадних строк.
# Якщо немає спільних символів - поверніть пусту строчку. 
# Ви можете повернути відповідь у будь-якому порядку.
# Символи не повині дублюватись у відповіді.

# Приклад 1
# commonStr('loli', 'luck') -> 'l'

# Приклад 1
# commonStr('good day', 'good morning') -> 'god'



def commonStr(str1, str2):
    newStr = ''
    for x in str1:
        if x in str2 and x not in newStr and x != ' ':
            newStr += x
    return newStr

print(commonStr('loli', 'luck') == 'l') 
print(commonStr('good day', 'good morning') == 'god') 