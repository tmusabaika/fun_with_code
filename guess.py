import random
import sys

def check_guess(response, challenge):
    if int(response) == challenge:
        return 0
    else:
        return 1

def check_variance(response, challenge):
    variance = abs((float(response - challenge)/10)*100)
    if variance <= 10:
        return 'Very close!'
    elif variance >= 60:
        return 'You drifted...'
    else:
        return ''

print(len(sys.argv))

if len(sys.argv) == 2:
    lower = 0
    upper = sys.argv[1]
elif len(sys.argv) == 3:
    if int(sys.argv[1]) > int(sys.argv[2]):
        print('Undefined range (range start value is bigger than range end value). Using default range')
        lower = 0
        upper = 10
    else:
        lower = sys.argv[1]
        upper = sys.argv[2]
elif len(sys.argv) == 1:
    print('No range defined. Using default range')
    lower = 0
    upper = 10
else:
    print('Invalid arguments. Enter at most 2 number (lower and upper values). Using default range')
    lower = 0
    upper = 10

print('Lower: ' + str(lower))
print('Upper: ' + str(upper))

random_num = random.randint(int(lower), int(upper))
attempts = 1

#print(random_num)

while (attempts <= 3):
    
    print('\n'+'*'*10)
    print('Attempt ' + str(attempts) + '\n')
    guess = input('Guess a number between ' + str(lower) + ' and ' + str(upper) + ': \n')
    result = check_guess(guess, random_num)
    if result == 0:
        print('You guessed it!')
        exit(0)
    elif result == 1:
        print(check_variance(guess, random_num))
        if attempts == 2:
            print('One more try')
        elif attempts < 3:
            print('Give it another go!')
        else:
            print('No more tries. The answer was ' + str(random_num) + '. Reload Game')
    attempts += 1
