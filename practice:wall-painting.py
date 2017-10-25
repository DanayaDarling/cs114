gallon = 400

width = int(input('How many feet wide is the wall?  '))
height = int(input('How many feet tall is the wall?  '))
square_foot = width * height
paint_needed = square_foot / gallon
print('You need to buy ' + str(paint_needed) + ' gallon(s) of paint')
cost_of_gallon = int(input('How much is the paint you wish to buy?  '))
total_cost = cost_of_gallon * paint_needed
print('It will cost $' + str(total_cost) + ' to paint your wall.')
