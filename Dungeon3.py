print("Welcome to Dungeon Crawler")
print("Who dares to enter the dungeon?")
name = input()
print("Foolish" , name , "you will soon meet your end!")
print("Tell me, are you a hunter, thief, magician, or warrior?")
class1 = input()
print("If you are a", class1 , "like you say you are, how much damage can you do?")
attack = int(input())
if attack>100:
    print("I know you are not that powerful, you can't have over 100 points! Try again!")
    attack = int(input())
magic = int(100 - attack)
print("Alright, so you left yourself with" , str(magic) , "magic points")
print("Well" , name , "you may enter the dungeon. Hopefully a" , class1 , "like yourself can survive with only" , attack , "attack points, and" , magic , "magic points.")
print("Good luck!")
