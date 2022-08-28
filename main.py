'''
stroka = 'hi - \"'

chislo = 5

test = stroka + str(chislo) + '\" символ обратного слэша \\ это экранирование'

print(test)

print('Если поставить \\n то \n начнётся новая строка')

print('Если поставить \\t то \t будет отступ (табуляция)')

# f-строки
print(f'{stroka}{chislo}" можно и так без преобразования в str')
'''


number = int(input('Я загадал число. Введите число от 1 до 5: '))
print(f'Вы ввели число - {number}')

#Подключение модуля random

import random
numberAI = random.randint(1,5)

print(f'а число загаданное компьютером: {numberAI}')

if number == numberAI:
    print('Победа Вы угадали')
else:
    print('Вы не угадали')

