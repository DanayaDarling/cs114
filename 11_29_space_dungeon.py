import random

print('         ~~~~~~~~~******   Welcome Traveler   ******~~~~~~~~~')
print('        ~~~~~~~~~~******          to          ******~~~~~~~~~~')
print('       ~~~~~~~~~~~******  The Fallen Dungeon  ******~~~~~~~~~~~')
print('')
print('                   Who dares to enter the dungeon?   ')
name = input()
print("          Foolish " + str(name) + " you will soon meet your end!")
print("       Tell me, are you a *warrior* *magician* *theif* or *hunter*?    ")
class1 = input()
while class1 == 'warrior' or 'magician' or 'theif' or 'hunter':
    if class1 == 'warrior':
        attack_points = 80
        magic_points = 20
        print('As a warrior you have 80 attack points, and 20 magic points.')
        break
    elif class1 == 'magician':
        attack_points = 20
        magic_points = 80
        print('As a magician you have 80 magic points, and 20 attack points.')
        break
    elif class1 == 'theif':
        attack_points = 60
        magic_points = 40
        print('As a theif you have 60 attack points, and 40 magic points.')
        break
    elif class1 == 'hunter':
        attack_points = 40
        magic_points = 60
        print('As a hunter you have 60 magic points, and 40 attack points.')
        break
    else:
        print('I guess the stars did not explain the game play well enough. You must type something between the stars as your choice.')
        class1 = input()
print('')
print("                    Well " + str(name) + " you may enter the dungeon.")
print('')
print('    Hopefully a ' + str(class1) + ' like yourself can survive with only ' + str(attack_points) + ' attack points, and ' + str(magic_points) + ' magic points.')
print('')
pack = ['food', 'magic potion', 'attack potion', 'an empty slot for future items.']
ring_pickup = input('You being your journey and notice a glowing ring on the ground. Do you want to pick it up?   ')
while ring_pickup == 'yes' or 'no':
    if ring_pickup == 'yes':
        pack[3] = ('a ring')
        print('You have added the ring to your pack')
        break
    elif ring_pickup == 'no':
        print('You do not risk picking up an unknown object.')
        break
    else:
        ring_pickup = input('Simply answer yes or no.  ')
print('You look in your pack and see that you have some ' + str(pack[0]) + ', a ' + str(pack[1]) + ', an ' + str(pack[2]) + ', and ' + str(pack[3]))
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
        print('You have given your enemy a chance to kill you. You have died')
        exit()

def attack(attack_points):
    print('You choose to attack, which costs 10 AP...')
    print('')
    if attack_points >= 10:
        print('You have hit your enemy!')
        attack_points -= 10
        print('You have ' + str(attack_points) + ' AP left.')
        roll_for_damage(enemy_health)
    else:
        print('You do not have enough AP')
        print('You have given your enemy a chance to kill you. You have died')
        exit()

print('')
offense = input()
print('')
while offense == 'cast a spell' or 'attack':
    if offense == 'cast a spell':
        cast_spell(magic_points)
        break
    elif offense == 'attack':
        attack(attack_points)
        break
    else:
        print('It seems you do not understand how monsters, or possibly this game, work, therefore, you have died.')
        break

print('He was angered by your attack! He uses hes large claws to attack you!')
roll_for_damage(your_health)
print('Thinking you are dead he begins to fall asleep. What is your next move?')
# second_choice = input('                    *cast a spell*   *attack*  *use item*   *run away*')
# while second_choice == 'cast a spell' or 'attack' or 'use item' or 'run away':
#     if second_choice == 'cast a spell':
#         cast_spell(magic_points)
#         break
#     elif second_choice == 'attack':
#         attack(attack_points)
#         break
#     elif second_choice == 'use item':
#         print('You check your pack and see that you have food for health, a potion for for magic or attack, and an unknown ring you do not remmebr picking up.')

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
