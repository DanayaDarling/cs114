print('input total without a decimal')
twentyT = 10
tenT = 15
fiveT = 21
oneT = 27
quaterT = 40
dimeT = 50
nickelT = 40
pennyT = 100
change = int(input())
twenty = change // 2000
if twenty > twentyT:
    print('insufficient funds')
else:
    print(twenty , 'twenty(ies)')
changet = change - twenty * 2000
tens = changet // 1000
if tens > tenT:
    print('insufficient funds')
else:
    print(tens , 'ten(s)')
changef = change - (twenty * 2000) - (tens * 1000)
fives = changef // 500
if fives > fiveT:
    print('insufficient funds')
else:
    print(fives , 'five(s)')
changeo = change - (twenty * 2000) - (tens * 1000) - (fives * 500)
ones = changeo //100
if ones > oneT:
    print('insufficient funds')
else:
    print(ones , 'one(s)')
changeq = change - (twenty * 2000) - (tens * 1000) - (fives * 500) - (ones * 100)
quaters = changeq // 25
if quaters > quaterT:
    print('insufficient funds')
else:
    print(quaters , 'quater(s)')
changed = change - (twenty * 2000) - (tens * 1000) - (fives * 500) - (ones * 100) - (quaters * 25)
dimes = changed // 10
if dimes > dimeT:
    print('insufficient funds')
else:
    print(dimes , 'dime(s)')
changen = change - (twenty * 2000) - (tens * 1000) - (fives * 500) - (ones * 100) - (quaters * 25) - (dimes * 10)
nickels = changen // 5
if nickels > nickelT:
    print('insufficient funds')
else:
    print(nickels , 'nickel(s)')
changep = change - (twenty * 2000) - (tens * 1000) - (fives * 500) - (ones * 100) - (quaters * 25) - (dimes * 10) - (nickels * 5)
penny = changep // 1
if penny > pennyT:
    print('insufficient funds')
else:
    print(penny , 'penny(ies)')
