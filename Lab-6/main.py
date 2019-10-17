# Generate a random  number and ask
# user to guess what it is and give the user
#hints to guess the right answer.

import random
n=20
'''
random.randrang()

'''
#print(random.random())
#print(random.uniform())
def guessgame():
    to_be_guessed=int(n*random.random())+1
    guess=0 # initialize the variable guess

    while guess!=to_be_guessed:
        guess=int(input("New Number: "))
        if guess>0:
            if guess> to_be_guessed:
                print("Number too large!")
            elif guess<to_be_guessed:
                print("Number too small")
        else:
            print("Sorry that you are giving up!")
            break
    else:
        print("Congrants you made it!")

#guessgame()

def devide(x,y):
    try:
        result =x/y
    except ZeroDivisionError:
        print("Devided by zero")
        a = int(input("Number1?"))
        b = int(input("Number2?"))
        devide(a, b)
    else:
        print("The result is ",result)
    finally:
        print("Executing finally clause!")
a=int(input("Number1?"))
b=int(input("Number2?"))
#devide(a,b)

# Write you own validation loop!
while True:
    try:
        age=int(input("Please enter your age"))
    except ValueError:
        print("Sorry, I didn't underestand that!")
        continue
    if age <0:
        print("Sorry, your resopnse must NOT be negative")

    else:
        break
        # Age was successfully parsed and
        #we're happy with the value and we
        #are ready to exit

if age >=18:
    print("you are able to vote in Canada!")
else:
    print("You are not eligible to vote in Canada")
