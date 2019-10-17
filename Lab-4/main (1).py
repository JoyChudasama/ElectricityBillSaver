'''
Repetition structure:

1) Condition Controlled :
    1- While loop
        [the condition has to be true]
        [check the condition first]
    2- do-while loop
           [the condition has to be true]
        [do the task first then check the  condition]
    3- do unit loop [ check the condition first and
    [ the condition has to be false]
2) Count controlled:
     for loop

while condition:
    statement
    statement
    etc.
'''
MAX_TEMP=40
def temp_check():
    temp=float(input('Enter the substance\'s '
                     'temperature \n '))
    while temp>MAX_TEMP:
        print('The temp is too hot!')
        print('Turn down the thermostat down'
              ' and wait')
        temp = float(input('Enter the substance\'s '
                           'temperature again! \n '))
    print('The temp is acceptable')
    print('check in again in 15 minutes')
#temp_check()
import random
def num_game():
    confirm='y'
    while confirm=='y':
        Guess_num=7 # this is a number user has to guess in
        #order to win the game..
        num=int(input("Guess a number!"))#7
        counter=1
        while num!=Guess_num:
            # the input number is higher than guess num
            if num>Guess_num:
                print('The number is too high!')
                num = int(input("Guess another number!"))
                # the input number is lower than guess number
            else: # num<Guess_num
                print('The number is too low')
                num = int(input("Guess another number!"))
            counter=counter+1

        print('you got it ! good job!')
        print('it took you only',counter,'time to guess!')
        confirm=input('if you like to play another game'
                      'type "y" otherwise type "n"')
    print('The game is over!')
#num_game()
# count control... [for loop!]
# we know the number of time we are going to repeat
# a group of task...
sum=0
for count in [0,1,2,3,4]:
    sum=sum+count
    print(count)
print(sum)
print('========')
for i in range(5): # range generates a list of numbers
    # from [0,5)
    #print(i)
    print('Hello')
print('========')
for i in range(2,9):
    print(i)
print('========')
for i in range(10,21,10):
    print(i)
print('=========')
for i in range(10,-1,-2):
    print(i)

print('========')
for i in range(1,12,11):
    print(i)

#=====================#
def calculate():
    Time=int(input("How many numbers you need"
                   " to get the average of"))
    count=1
    total=0
    while count<=Time:
        num=int(input('Enter the number %d'%(count)))
        total=total+num
        count=count+1
    print('The sum is',total)
    print('The average is',format(total/Time,'.2f'))



def main():
    print("Welcome to the program")
    confirm="yes"
    while confirm =="yes":
        calculate()
        confirm=input('Please type "yes" to continue')
    print('Thanks for using the our program')

main()