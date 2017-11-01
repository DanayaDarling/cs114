name = input('Tell me your name, and I shall tell you your fortune?  ')
import random
def getfortune(fortunenumber):
    if fortunenumber == 1:
        return ', you shall be rich and loved all the days of your life.'
    elif fortunenumber == 2:
        return ', you were meant for great things.'
    elif fortunenumber == 3:
        return ', your future is too depressing to even describe.'
    elif fortunenumber == 4:
        return ', for some reason I cannot read your fortune.'
    elif fortunenumber == 5:
        return ', you have the grim! It is an omen of death.'
    elif fortunenumber == 6:
        return ', life has many paths, do not be afraid to travel more than one of them.'
    elif fortunenumber == 7:
        return ', I do not know what you want me to say, just live your life I guess.'
    elif fortunenumber == 8:
        return ', you will have a bright future, as long as you do nothing stupid.'
    elif fortunenumber == 9:
        return ', your future looks almost exactly like the rest of your life has been up to this point.'
r = random.randint(1,9)
fortune = getfortune(r)
print(name + fortune)
