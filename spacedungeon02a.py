magic_points = 50
attack_points = 50
print('          ~~~~~~~~~******  Welcome Traveler  ******~~~~~~~~~')
print('')
print('      You have been given 50 magic points, and 50 attack points.')
print('    An enemy approches!! Do you wish to *attack* or *cast a spell*?   ')
offense = input()
if offense == 'cast a spell':
    while magic_points >= 10:
        print('Your spell has hit the enemy!')
        magic_points -= 10
        print('You have ' + str(magic_points) + ' magic points left.')
elif offense == 'attack':
    while attack_points >= 10:
        print('You hit the enemy!')
        attack_points -= 10
        print('You have ' + str(attack_points) + ' attack points left.')
