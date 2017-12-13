import random
import os

os.system("say 'Welcome traveler to the fallen dungeon'")
print('         ~~~~~~~~~******   Welcome Traveler   ******~~~~~~~~~')
print('        ~~~~~~~~~~******          to          ******~~~~~~~~~~')
print('       ~~~~~~~~~~~******  The Fallen Dungeon  ******~~~~~~~~~~~')
print('')
os.system("say 'Who dares to enter the dungeon?'")
print('                   Who dares to enter the dungeon?   ')
name = input()
print('            Foolish ' + str(name) + ' you will soon meet your end!')
print(' Tell me, are you a *warrior* *magician* *thief* or *hunter*? (*see stats*)   ')
class1 = input()
while class1 == 'warrior' or 'magician' or 'thief' or 'hunter' or 'see stats':
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
    elif class1 == 'thief':
        attack_points = 60
        magic_points = 40
        print('As a thief you have 60 attack points, and 40 magic points.')
        break
    elif class1 == 'hunter':
        attack_points = 40
        magic_points = 60
        print('As a hunter you have 60 magic points, and 40 attack points.')
        break
    elif class1 == 'see stats':
        print('*warrior* - 80 attack points, 20 magic points')
        print('*magician* - 20 attack points, 80 magic points')
        print('*thief* - 60 attack points, 40 magic points')
        print('*hunter* - 40 attack points, 60 magic points')
        class1 = input()
    else:
        print('I guess the stars did not explain the game play well enough. You must type something between the stars as your choice.')
        class1 = input()
print('')
print('            Well ' + str(name) + ' you may enter the dungeon.')
print('Hopefully a ' + str(class1) + ' like yourself can survive with only ' + str(attack_points) + ' attack points, and ' + str(magic_points) + ' magic points.')
print('')
pack = [' food ', ' a magic potion ', ' an attack potion ', ' space for future items. ']
ring_pickup = input('You begin your journey and notice a glowing ring on the ground. Do you want to pick it up?   ')
while ring_pickup == 'yes' or 'no':
    if ring_pickup == 'yes':
        print('')
        pack[3] = ('a ring')
        print('You have added the ring to your pack')
        break
    elif ring_pickup == 'no':
        print('')
        print('You do not risk picking up an unknown object.')
        break
    else:
        ring_pickup = input('Simply answer yes or no.  ')

print('')
print('You look in your pack and see that you have' + str(pack[0]) + str(pack[1]) + str(pack[2]) + ', and ' + str(pack[3]))
print('')
print('********************************************************************************************************************************************************')
print('')
print('    There is an enemy!! He seems to have 100 health! Do you wish to *attack* or *cast a spell*?')
enemy_health = 100
your_health = 200

def roll_for_damage(health):
    damage = random.randint(10,50)
    health -= damage
    print('The hit has cost ' + str(damage) + ' health. The victum has ' +str(health) + ' health left.')
    return health
    if health <= 0:
        print('The victim has died')
        exit()

def cast_spell(magic_points, health):
    print('You choose to cast a spell, which costs 10 MP...')
    print('')
    if magic_points >= 10:
        print('Your spell has hit your enemy!')
        magic_points -= 10
        print('You have ' + str(magic_points) + ' MP left.')
        health = roll_for_damage(health)
        return magic_points
        return health
    else:
        print('You do not have enough MP')
        print('You have given your enemy a chance to kill you. You have died')
        exit()

def attack(attack_points, health):
    print('You choose to attack, which costs 10 AP...')
    print('')
    if attack_points >= 10:
        print('You have hit your enemy!')
        attack_points -= 10
        print('You have ' + str(attack_points) + ' AP left.')
        health = roll_for_damage(health)
        return attack_points
        return health
    else:
        print('You do not have enough AP')
        print('You have given your enemy a chance to kill you. You have died')
        exit()

def use_item(your_health, attack_points, magic_points):
    print('Which item would you like to use?')
    if pack[3] != ' space for future items. ':
        active_item = input('*' + str(pack[0]) + '* *' + str(pack[1]) + '* *' + str(pack[2]) + '* *' + str(pack[3]) + '*')
    else:
        active_item = input('*' + str(pack[0]) + '* *' + str(pack[1]) + '* *' + str(pack[2]) + '*')
    while active_item == 'food' or 'an attack potion' or 'a magic potion' or 'a ring' or 'a necklace':
        if active_item == 'food':
            print('Eating food has helped you heal!')
            your_health += 20
            print('You now have ' + str(your_health) + ' health!')
            break
        elif active_item == 'an attack potion':
            print('Drinking this potion gave you more strength!')
            attack_points += 20
            print('You now have ' + str(attack_points) + ' AP!')
            break
        elif active_item == 'a magic potion':
            print('Drinking this potion gave you more magic!')
            magic_points += 20
            print('You now have ' + str(magic_points) + ' MP!')
            break
        elif active_item == 'a ring':
            print('You put the ring on and feel yourself glowing!')
            pack[3] = ' space for future items. '
            attack_points += 10
            magic_points += 10
            your_health += 10
            print('Your health, magic points, and attack points have all increased! You now have ' + str(your_health) + ' health, ' + str(attack_points) + ' AP, and ' + str(magic_points) + ' MP! ')
            break
        elif active_item == 'a necklace':
            print('You put the necklace on and feel yourself glowing!')
            pack[3] = ' space for future items. '
            attack_points += 10
            magic_points += 10
            your_health += 10
            print('Your health, magic points, and attack points have all increased! You now have ' + str(your_health) + ' health, ' + str(attack_points) + ' AP, and ' + str(magic_points) + ' MP! ')
            break
    else:
        print('You do not have that item!')
        active_item = input()

print('')
offense = input()
print('')
while offense == 'cast a spell' or 'attack':
    if offense == 'cast a spell':
        magic_points = cast_spell(magic_points, enemy_health)
        break
    elif offense == 'attack':
        attack_points = attack(attack_points, enemy_health)
        break
    else:
        print('It seems you do not understand how monsters, or possibly this game, work, therefore, you have died.')
        exit()
print('')
print('         He was angered by your attack! He uses hes large claws to attack you!')
print('')
your_health = roll_for_damage(your_health)
print('    Thinking you are dead he begins to fall asleep. What is your next move?')
print('')
print('     *cast a spell*   *attack*  *use item*   *run away*')
second_choice = input()
while second_choice == 'cast a spell' or 'attack' or 'use item' or 'run away':
    if second_choice == 'cast a spell':
        magic_points = cast_spell(magic_points, enemy_health)
        break
    elif second_choice == 'attack':
        attack_points = attack(attack_points, enemy_health)
        break
    elif second_choice == 'use item':
        use_item(your_health, attack_points, magic_points)
        print('He still has not noticed you, would you like to *attack* *cast a spell* or *run away*')
        second_choice = input()
    elif second_choice == 'run away':
        print('You are a coward! Farewell ' + str(name) + ' the Coward. That is what everyone will call you from now on! '+ str(name) + ' the Coward...')
        exit()
    else:
        print('Choose!')
        second_choice = input()
print('')
print('He has noticed that, and it looks like his sleep has returned his strength! He attacks you again!')
your_health = roll_for_damage(your_health)
print('')
print('This is your last chance, You can either, *attack*, or *cast a spell*')
print('It will use all of your AP or MP, which do you choose?')
third_choice = input()
while third_choice == 'cast a spell' or 'attack':
    if third_choice == 'cast a spell':
        while magic_points > 10:
            while enemy_health >= 0:
                enemy_health = roll_for_damage(enemy_health)
            else:
                print('You have defeated the beast!')
                exit()
        else:
            print('You did not defeat the enemy with your points')
            exit('You died')

    elif third_choice == 'attack':
        while attack_points > 10:
            while enemy_health >= 0:
                enemy_health = roll_for_damage(enemy_health)
            else:
                print('You have defeated the beast!')
                print('Congragulations ' + str(class1) + '! From this day forth you shall be know as the defender of this dungeon!' )
                print('You have recieved riches beyond imagining! Good Job!')
                print('')
                exit()

        else:
            print('You did not defeat the enemy with your points')
            exit('You died')
    else:
        print('You cannot run, or use an item, or anything else at this time')
        print('*attack* or *cast a spell*')
        third_choice = input()
