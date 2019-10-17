'''
Condition control (While loop)
    we dont know how many times you want to repeat

while condition:
    statements
    statements
    etc.
 one of the usage of while is input validation control!

count control (For loop)

'''

MAX_TEMP=40

def temp_check():
    temp=float(input('Enter the substanc\'s'
                     ' temprature\n'))

    while temp>MAX_TEMP:
        print('The temp is to hot!')
        print('Turn down the thermostat down and wait')
        temp = float(input('Enter the substance\'s'
                           ' temperature\n'))
    print('The temperature is acceptable')
    print('Check it again in 15 minutes.!')
#temp_check()

# input validation loops!
def num_game():
    Guess_num=7
    num=int(input("Guess the number?"))
    while num!=Guess_num:
        if num>Guess_num:
            print('The number is too high!')
            num = int(input("Guess the number?"))
        else:
            print('The number is too low!')
            num = int(input("Guess the number?"))
    print('You got it! good job!')

#num_game()

for count in [1,2,3,4,5]:
    print(count)
for name in ['Hesam','Tony','Alex']:
    print(name)

for i in range(5):
    print(i)
    print('Hello')

for i in range(1,6): #[1,6)
    print(i)

for i in range(1,11,2): # range(begin,end+1, inc.)
    print(i)
print('===============')
for i in range(10,-1,-1):
    print(i)
print('===============')
for i in range(1,12,11):
    print(i)

def table():
    interval=int(input('Please set the interval\n'))
    print('Number\t\tSquare')
    print('=================')

    for number in range(1,interval+1):
        square=number**2
        print(number,'\t\t',square)

table()