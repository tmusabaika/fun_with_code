import random

def check_guess(response, challenge):
    if int(response) == challenge:
        return 0
    else:
        return 1

random_num = random.randint(0, 10)
attempts = 1

print(random_num)

while (attempts < 4):
    
    print('\n'+'*'*10)
    print('Attempt ' +str(attempts) + '\n')
    guess = input('Guess a number between 0 and 10: \n')
    result = check_guess(guess, random_num)
    if result == 0:
        print('You guessed it!')
        exit(0)
    elif result == 1:
        variance = abs((float(guess - random_num)/10)*100)
        if variance <= 20:
            print('Very close!')
        elif variance >= 50:
            print('You drifted...')
        else:
            print('Quite close')
        if attempts == 2:
            print('One more try')
        elif attempts < 3:
            print('Nope... Give it another go!')
        else:
            print('Nope... No more tries. Reload Game')
    attempts += 1
