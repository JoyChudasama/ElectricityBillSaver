# Two libraries
# math and random library!

import math # math purposes
import random # random number purposes.

def rand():
    # 5 random integers between 1 and 100
    # and print them!
    for count in range(5):  # [0,5) start from zero by default
        number=random.randint(1,100) # random int number [1,100]
        print(number)
rand()

# all for generating integers!
print('=============')
number=random.randrange(10) # a random integer in a range [0,10)
print(number)

print('=============')
number=random.randrange(5,10) # a random integer in a range [5,10)
print(number)
print('=============')
number=random.randrange(0,101,10) # a random integer in a range [5,10)
#[0,10,20,30,40,50,60,70,80,90,100]
print(number)

# non integer numbers (real numbers)
print('===========')
number=random.uniform(1.0,10.0) # choose a real number between 1 to 10
print(format(number,'.2f'))

print('=============')
number=random.random()  # [0% to 100%]
print(number)

def circle_Area():
    redius=float(input('Please enter the radius'))
    area=math.pi*math.pow(redius,2)
    print('The area of circle with redius of %.2f '
          'is %.2f'%(redius,area))
#circle_Area()

print(math.inf)
print(math.sin(math.radians(30))) # its in radiant

# String manipulation in Python...

name='Hesam'
strlength=len(name) # length is the function get the length of a string
print(strlength)

message='This is '+"one sting"+' Now'
print(message)
Capname=name.upper()
print(Capname)
lowCapname=Capname.lower()
print(lowCapname)

# how do we find things in string?
string='Four score and seven years a go'
position=string.find('seven')
print(position)

full_name='Patty Lynn Smith'
first_name=full_name[:5]
print(first_name)
middle_name=full_name[6:10]
print(middle_name)
last_name1=full_name[11:]
last_name2=full_name[-5:]
print(last_name1)
print(last_name2)
fullyname=full_name[:]
print(fullyname)

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(letters[0:26:10])

# break! we start 2:30!

# Lets write a program ....
# ask user to give the name and student number
# they pass or failed!
# tell them pass/failed

def get_name():
    name=input('Please enter the name: ')
    return name

def get_student_number():
    stn=input('Enter the student number')
    return stn
def get_status(name,stn):
    status=True
    for nm in ['hesam','tony','lovepreet']:
        if nm==name:
            for num in ['C0777777','C0333333','C0111111']:
                if num==stn:
                    status=False
    return status
def main():
    confirm='y'
    while confirm=='y' or confirm=="Y":
        name=get_name()
        stn=get_student_number()
        print(stn.upper())
        status=get_status(name.lower(),stn.upper())
        if status:
            print('Congrat\'s', name,"you passed!")
        else:
            print('Sorry', name,'you failed!')
        confirm=input('if you like to continue type "Y" for'
                      ' yes and "N" for no')

main()
