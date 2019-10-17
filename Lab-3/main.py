'''
The rational operation are used to create
boolean expression ("True or False")
here is a general format of the if statement
in Python!

if condition: (if clause)
    statement
    statement
    etc.

(alternative dual condition)
you use if-else statement

if condition:
    statement
    statement
    etc.
else:
    statements
    statements
[Nested conditioning decision]
if condition:
    statements
    etc.
else:
    if condition:
        statements
        statments
    else:
        if condition:
            statements
            statements
            etc
        else:
            if condition:
                statements
                etc.

if condition :
    statements
    etc
elif condition:
    statement
    etc
elif condition:
    statment

'''

def average():
    test1=int(input("Enter the first test"))
    test2=int(input('Enter the second test'))
    test3=int(input("Enter the third test"))
    average=(test1+test2+test3)/3.0
    print('The average score is', format(average,'.1f'))

    if average>=90:
        print('Congrates!')
        print('This is a great average!')
    else:
        print('Your average is not greater than 90')
        if average<90 and average>=50:
            print("you are in average range")
        else:
            print('you failed!')

    '''
    True && True = True (both has to be true )
    True && False = False 
    False && True = False
    False && False =False
    -----------------------
    True || True = True 
    True || False =True
    False || True = True
    False || False =False
    
    '''
#average()
name1='Mark'
name2="Mark"

if name1==name2:
    print('The name are the same')
else:
    print('The name are NOT the same!')

def salequota(sales):
    if sales>= 50000:
        sales_quate_met=True
    else:
        sales_quate_met=False
    return sales_quate_met

#print(salequota(60000))
def sales():
    quota=int(input('Please enter the sales quata'))
    name=input('Please enter your name')
    if salequota(quota):
        print('you met the sales quota')
        if name=='Hesam':
            print(' you met your sales quota two consecutive '
                  'years and you win a \nFrance vacation!')
        else: print('good job! keep it up!')
    else:
        print('The sales quota is not met!')
        if name=='Tony'or name=='Alex':
            print(name, 'you are fired!')
        elif name=='Robert':
            print('This is your last warning!')
#sales()
'''
1) Display " Tell me the military time?"
    Input Time
  if 4:00am <Time < 12:00 pm
    Display" good morning"
  else if 12:00pm <Time < 6:00 pm
    Display" good afternoon"
    else if 6:00pm <Time < 11:00 pm
        Display" good evening"
    else if 11:pm < Time < 4:00 am
        Display" good night"

    Display" good afternoon"


'''

time=int(input('Tell me the military time'))

if (time>400 and time<=1200):
    print('Good morning sunshine!')
elif(time>1200 and time<1800):
    print("Good afternoon pumpkin")
elif(time>=1800 and time <2300):
    print("good evening muffin")
elif((time>=2300 and time<2400)or(time<400 and time>0000)):
    print('good night sleep tight')
else: print('Wrong input apple tartilla')