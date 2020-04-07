# amount (in cents)
amount = 1156

# values coins used USD (in cents)
cents_in_dollar = 100
cents_in_quarter = 25
cents_in_dime = 10
cents_in_nickel = 5

# determine minimum number of coins needed
dollars = amount // cents_in_dollar
cents = amount % cents_in_dollar

quarters = cents // cents_in_quarter
cents = cents % cents_in_quarter

dimes = cents // cents_in_dime
cents = cents % cents_in_dime

nickels = cents // cents_in_nickel
cents = cents % cents_in_nickel

# print minimum number of coins
print(f'Dollars: {dollars}')
print(f'Quarters: {quarters}')
print(f'Dimes: {dimes}')
print(f'Nickels: {nickels}')
print(f'Cents: {cents}')
