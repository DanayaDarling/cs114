print('input total without a decimal')
change = int(input())
twenty = change // 2000
print(twenty , 'twenty(ies)')
changet = change - twenty * 2000
tens = changet // 1000
print(tens , 'ten(s)')
changef = change - (twenty * 2000) - (tens * 1000)
fives = changef // 500
print(fives , 'five(s)')
changeo = change - (twenty * 2000) - (tens * 1000) - (fives * 500)
ones = changeo //100
print(ones , 'one(s)')
changeq = change - (twenty * 2000) - (tens * 1000) - (fives * 500) - (ones * 100)
quaters = changeq // 25
print(quaters , 'quater(s)')
changed = change - (twenty * 2000) - (tens * 1000) - (fives * 500) - (ones * 100) - (quaters * 25)
dimes = changed // 10
print(dimes , 'dime(s)')
changen = change - (twenty * 2000) - (tens * 1000) - (fives * 500) - (ones * 100) - (quaters * 25) - (dimes * 10)
nickels = changen // 5
print(nickels , 'nickel(s)')
changep = change - (twenty * 2000) - (tens * 1000) - (fives * 500) - (ones * 100) - (quaters * 25) - (dimes * 10) - (nickels * 5)
penny = changep // 1
print(penny , 'penny(ies)')
