
convert_equations = input('What are you converting? (miles to kilometers, etc.)  ')
miles = int(input('How many?')

def convert_number(convert_equations):
    if convert_equations == 'miles to kilometers':
        converted_number = miles * 1.60934
    elif convert_equations == 'miles to feet':
        converted_number = miles * 5280
    elif convert_equations == 'miles to meters':
        converted_number = miles * 1609.34
    elif convert_equations == 'miles to inches':
        converted_number = miles * 63360

 final_number == convert_number(convert_equations)
print(final_number)
