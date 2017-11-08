print("            What are you trying to convert?            ")
base_conversion = input('     miles to kilometers, kilometers to miles, etc.  : ')
if base_conversion == 'miles to kilometers':
    miles = int(input('How many miles do you wish to convert?  '))
    converted_number = miles * 1.60934
    print('That would be ' + str(converted_number) + ' kilometers')
elif base_conversion == 'kilometers to miles':
    kilometers = int(input('How many kilometers do you wish to convert?  '))
    converted_number = kilometers / 1.60934
    print('That would be ' + str(converted_number) + ' miles')
elif base_conversion == 'miles to feet':
    miles = int(input('How many miles do you wish to convert?  '))
    converted_number = miles * 5280
    print('That would be ' + str(converted_number) + ' feet')
elif base_conversion == 'miles to meters':
    miles = int(input('How many miles do you wish to convert?  '))
    converted_number = miles * 1609.34
    print('That would be ' + str(converted_number) + ' meters')
elif base_conversion == 'kilometers to feet':
    kilometers = int(input('How many kilometers do you wish to convert?  '))
    converted_number = kilometers * 3280.84
    print('That would be ' + str(converted_number) + ' feet')
elif base_conversion == 'kilometers to meters':
    kilometers = int(input('How many kilometers do you wish to convert?  '))
    converted_number = kilometers * 1000
    print('That would be ' + str(converted_number) + ' meters')
elif base_conversion == 'kilometers to inches':
    kilometers = int(input('How many kilometers do you wish to convert?  '))
    converted_number = kilometers * 39370.1
    print('That would be ' + str(converted_number) + ' inches')
elif base_conversion == 'miles to inches':
    miles = int(input('How many miles do you wish to convert?  '))
    converted_number = miles * 63360
    print('That would be ' + str(converted_number) + ' inches')
