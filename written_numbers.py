number = input('Input a number between 1 and 99 :  ')
if int(number) >= 20:
    tens = int(number) // 10
    ones = int(number) % 10
    if tens == 2:
        tens_print = 'twenty'
    elif tens == 3:
        tens_print = 'thirty'
    elif tens == 4:
        tens_print = 'fourty'
    elif tens == 5:
        tens_print = 'fifty'
    elif tens == 6:
        tens_print = 'sixty'
    elif tens == 7:
        tens_print = 'seventy'
    elif tens == 8:
        tens_print = 'eighty'
    elif tens == 9:
        tens_print = 'ninety'

    if ones == 1:
        ones_print = 'one'
    elif ones == 2:
        ones_print = 'two'
    elif ones == 3:
        ones_print = 'three'
    elif ones == 4:
        ones_print = 'four'
    elif ones == 5:
        ones_print = 'five'
    elif ones == 6:
        ones_print = 'six'
    elif ones == 7:
        ones_print = 'seven'
    elif ones == 8:
        ones_print = 'eight'
    elif ones == 9:
        ones_print = 'nine'

print(tens_print + ' ' + ones_print)
