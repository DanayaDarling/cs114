change = int(input())
quaters = change // 25
print(quaters , 'quater(s)')
changed = change - quaters * 25
dimes = changed // 10
print(dimes , 'dime(s)')
changen = change - (quaters * 25) - (dimes * 10)
nickels = changen // 5
print(nickels , 'nickel(s)')
changep = change - (quaters * 25) - (dimes * 10) - (nickels * 5)
penny = changep // 1
print(penny , 'penny(ies)')
