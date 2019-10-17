'''
Modularizing progam is breaking it down to smaller
module(Function)

In order to create a module in Python you need
to defined it!

def module_name():
      statements
      statements
      etc
# its customary to use 4 space to differentiate
between the header and the body the module  !
ALIGNMENT IS THE KEY TO KEEP THE SCOPE INTACT
'''
import birds

SALES_TAX=0.13

def message():#3#9
    print("My name is Hesam")#4#10
    print("I'm the king of Python")#5#11
print("Thats all!")#1
message()#2 #6
print('_________')#7
message()#8#12
#Global variables
#Local Variables!
def double_number():
    #value=0
    result=value*2
    print('The result is', result)

value=int(input("Give me a number and I double it!"))
double_number()
#print()

# A module can accept more than one input!

def show_sum(num1,num2):#2#11
    result=num1+num2#3#12
    print('Your sum of %d and %d is %d'%(num1,num2,result))#4#13
def get_inputs():#7
    n1=int(input('Please enter the fist number'))#8
    n2=int(input('Please enter the second number'))#9
    show_sum(n1, n2)#10#14
show_sum(3,5)#1#5
get_inputs()#6#15


birds.main()
print('______')
birds.california()
print('______')
birds.texas()

