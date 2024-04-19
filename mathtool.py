#Math multi-tool
#Main purpose of this mini project was to learn about the def function and using it to combine previous projects into one
import random as r
#2D perimeter
def perimeter():
    length = float(input('What is the length? '))
    width = float(input('What is the width? '))
    answer = length * 2 + width * 2
    print('The answer is: ',answer)
    global repeat
    repeat = input('Do you want to use this tool again? (yes/no) ')

#2D area
def twod_area():
    length = float(input('What is the length? '))
    width = float(input('What is the width? '))
    answer = length * width
    print('The answer is: ',answer)
    global repeat
    repeat = input('Do you want to use this tool again? (yes/no) ')

#3D area
def thrd_area():
    length = float(input('What is the length? '))
    width = float(input('What is the width? '))
    height = float(input('What is the height? '))
    answer = length * width * height
    print('The answer is: ',answer)
    global repeat
    repeat = input('Do you want to use this tool again? (yes/no) ')

#Basic facts calculator
def basic():
    x = float(input('First number in the equation: '))
    operator = str(input('What is the operator? (1 = +, 2 = -, 3 = x, 4 = ÷) '))
    y = float(input('Second number in the equation: '))
    if operator == '1':
        print('The answer is: ', x + y)

    elif operator == '2':
        print('The answer is: ', x - y)

    elif operator == '3':
        print('The answer is: ', x * y)
    
    elif operator == '4':
        print('The answer is: ', x / y)

    else:
        print('Double check the operator number and try again!')

    global repeat
    repeat = input('Do you want to use this tool again? (yes/no) ')

def numbergame():
    impossible = input("Do you want to play impossible mode? (yes/no) ")
    maxnumber = float(input("What's the maximum number that can be picked? "))
    lives = float(input("How many lives do you want? "))
   
    if impossible == 'no' or impossible == 'No': # type: ignore
        answer = r.randint(0, maxnumber)

    elif impossible == 'yes' or impossible == 'Yes':
        answer = r.uniform(0, maxnumber) 

    guess = float(input('Take a guess: '))
    #checking answer
    while True:
        if lives == 1:
            print('GAME OVER!!!')
            print('The answer was: ', answer,'!!!')
            break

        elif guess == answer:
                print('Correct!!! You won with',lives,'guesses left!')
                break
        elif guess < answer:
                print('Too low!')
                lives = lives - 1
                print('You have',lives,'lives left, make them count!')
                guess = float(input('Take a guess: '))

        elif guess > answer:
                print('Too high!')
                lives = lives - 1
                print('You have',lives,'lives left, make them count!')
                guess = float(input('Take a guess: '))
    global repeat
    repeat = input('Do you want to use this tool again? (yes/no) ')
    

#Loop function
repeat = 'yes'

while repeat == 'yes' or repeat == 'Yes':

    print('What kind of calculation would you like to do? ')
    mode = input('Enter b for basic calculator, p for 2D perimeter, 2da for 2D area, 3da for 3D area or ng for number guessing game: ')

    if mode == 'p' or mode == 'P':
        perimeter()

    elif mode == '2da' or mode == '2DA' or mode == '2Da' or mode == '2dA':
        twod_area()

    elif mode == '3da' or mode == '3DA' or mode == '3Da' or mode == '3dA':
        thrd_area()
    
    elif mode == 'b' or mode == 'B':
        basic()

    elif mode == 'ng' or mode == 'NG' or mode == 'Ng' or mode == 'nG':
        numbergame()

    else:
        print("Computer says no... *coughs*")#Little britain reference ;-)
        print("Make sure you haven't miss typed!")
        mode = input('Enter b for basic calculator, p for 2D perimeter, 2da for 2D area, 3da for 3D area or ng for number guessing game: ')

#Thank you for looking into my code 
