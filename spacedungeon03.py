import random

print('         ~~~~~~~~~******  Welcome Traveler  ******~~~~~~~~~')
print('       ~~~~~~~~~~~******  to Space Dungeon  ******~~~~~~~~~~~')
print('')
print("                  Who dares to enter the dungeon?")
name = input()
print("               Foolish " + str(name) + " you will soon meet your end!")
print("       Tell me, are you a *hunter*, *thief*, *magician*, or *warrior*?")
class1 = input()
print("    If you are a " + str(class1) + " like you say you are, how much damage can you do?")
attack_points = int(input())
if attack_points >= 100:
    print("    I know you are not that powerful, you can't have over 100 points! Try again!")
    attack_points = int(input())
magic_points = int(100 - attack_points)
print("    Alright, since you can only have 100 points at this level, you have left yourself with" , str(magic_points) , "magic points")
print('')
print("                    Well " + str(name) + " you may enter the dungeon.")
print('')
print('    Hopefully a ' + str(class1) + ' like yourself can survive with only ' + str(attack_points) + ' attack points, and ' + str(magic_points) + ' magic points.')
print('')
print('    There is an enemy!! He seems to have 100 health! Do you wish to *attack* or *cast a spell*?')
enemy_health = 100
your_health = 100

def roll_for_damage(health):
    damage = random.randint(5,20)
    health -= damage
    print('The victum now has ' + str(health) + ' health left.')

def cast_spell(magic_points):
    print('You choose to cast a spell, which costs 10 MP...')
    print('')
    if magic_points >= 10:
        print('Your spell has hit your enemy!')
        magic_points -= 10
        print('You have ' + str(magic_points) + ' MP left.')
        roll_for_damage(enemy_health)
    else:
        print('You do not have enough MP')
        print('You have died')

def attack(attack_points):
    print('You choose to attack, which costs 10 AP...')
    print('')
    if attack_points >= 10:
        print('You have hit your enemy!')
        attack_points -= 10
        print('You have ' + str(attack_points) + ' AP left.')
        roll_for_damage(enemy_health)
    else:
        print('You do not have enough MP')
        print('You have died')

print('')
offense = input()
print('')
if offense == 'cast a spell':
    cast_spell(magic_points)
elif offense == 'attack':
    attack(attack_points)
else:
    print('It seems you do not understand how monsters, or possibly this game, work, therefore, you have died.')

print('He was angered by your attack! He uses hes large claws to attack you!')
roll_for_damage(your_health)
print('Thinking you are dead he begins to fall asleep. Will you use all of your MP or AP to try to defeat the beast?')
second_offense = input('         *cast a spell* or *attack*')
if second_offense == 'cast a spell':
    for attack in range():
        random_damage = random.randint(10,20)
        print('Your spell hit the monster and he lost ' + str(random_damage) + ' health'
        enemy_health -= random_damage


#     while magic_points >= 10:
#         print('Your spell has hit the enemy!')
#         magic_points -= random.randint(1, 10)
#         print('You have ' + str(magic_points) + ' magic points left.')
#     print('')
#     print('~~You magic does not seem to faze the beast. To survive you must attack!~~')
#     print('')
#     while attack_points >= 10:
#         print('You hit the enemy!')
#         attack_points -= random.randint(1, 10)
#         print('You have ' + str(attack_points) + ' attack points left.')
#     print('The monster has still shown no sign of weakness...')
# elif offense == 'attack':
#     while attack_points >= 10:
#         print('You hit the enemy!')
#         attack_points -= random.randint(1, 10)
#         print('You have ' + str(attack_points) + ' attack points left.')
#     print('')
#     print('~~You attack does not seem to faze the beast. To survive you must use your magic!~~')
#     print('')
#     while magic_points >= 10:
#         print('Your spell has hit the enemy!')
#         magic_points -= random.randint(1, 10)
#         print('You have ' + str(magic_points) + ' magic points left.')
#     print('The monster has still shown no sign of weakness...')
# print('')
# print('    Despite all your efforts, the beast looks unfazed. Your future does not look bright.')
# print('')
