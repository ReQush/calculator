roman_to_arabic_symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
all_roman = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]


def roman_to_arabic(roman):
    value = 0
    g = 0
    while g < len(roman):
        if g+1 < len(roman) and roman_to_arabic_symbols[roman[g]] < roman_to_arabic_symbols[roman[g+1]]:
            value += roman_to_arabic_symbols[roman[g+1]] - roman_to_arabic_symbols[roman[g]]
            g += 2
        else:
            value += roman_to_arabic_symbols[roman[g]]
            g += 1
    return value

def arabic_to_roman(value):
    roman = ''
    for arabic, letter in all_roman:
        while value >= arabic:
            roman += letter
            value -= arabic
    return roman

def doings(x,y):
    x,y = int(x),int(y)
    if op == '+':
        result = x + y
    if op == '-':
        result = x - y
    if op == '*':
        result = x * y
    if op == '/':
        if y != 0:
            result = round(x / y)
        else:
            print('Деление на ноль')
    return result

while True:
    inlet = input('Введите пример(поддерживаются римские цифры):\n').split()
    if len(inlet) < 3:
        print('Неверный формат ввода')
        continue
    nums = ['1','2','3','4','5','6','7','8','9','0']
    roman_symbols = ['I','V','X','L','C','D','M']
    check = True


    x = inlet[0]
    y = inlet[2]
    op = inlet[1]

    if x[0] in nums and y[0] in nums:
        check = True
    elif x[0]  in roman_symbols and y[0]  in roman_symbols:
        check = False
    else:
        print('Некорректный ввод')
        continue



    if check == True:
        result = doings(x,y)
        print('Мой ответ: ',result)
        print()

    if check == False:
        roman = x
        num1 = roman_to_arabic(roman)
        roman = y
        num2 = roman_to_arabic(roman)
        x = num1
        y = num2
        value = doings(x,y)
        if value == 0:
            print('nulla')
            print()
        if value < 0:
            print('Римские числа не могут быть отрицательными')
            print()
        if value > 0:
            result = arabic_to_roman(value), value
            print('Мой ответ: ',result)
            print()
    