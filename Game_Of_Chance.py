import random as r


guess = int(input("Guess a number between 0-30:\n>>"))
bet = int(input("How much money do you want to bet:\n>>"))
multiplier = 1
primes = [2,3,5,7,11,13,17,19,23,29]
num = r.randint(0,30)

if guess == num:
    if guess % 2 == 0: multiplier *= 2
    if guess % 10 == 0: multiplier *= 3
    if guess in primes: multiplier *= 5
    if guess < 5: multiplier *= 2
else: multiplier = 0

print(f"Payout: £{bet*multiplier}")

