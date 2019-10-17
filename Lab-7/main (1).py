# In Python there no array in traditional way!
# declare int Array[SIZE]

# lists are similar to arrays but they are not the same

even_number=[2,4,6,8,10,12]
names=['Hesam',"Alex",'Tony',"Robert"] # list of names

print(even_number) # in most of the program if you print
#the array like that it shows you the memory location
#of the array although in Python it shows all of it!
print(even_number[0]) # for printing the first element
print(even_number[1])
print(even_number[2])
print(even_number[3])
print(even_number[4])
print(even_number[5])
# index is always size-1 ....
#print(even_number[6]) # out of range...
def sum_alist():
    # for going through a list we need a counted control
    # loop ( For loop)
    sum = 0 # Declare the variable sum!
    for index in range(len(even_number)):
        # NOT that by defult in program logic
        # the length function is length()
        sum=sum+even_number[index]
    print ('The sum of ',even_number,'is ',sum)
    print('The arevage is : ',sum/len(even_number))
sum_alist()

my_list=[10,20,30,40]
index=0
while index <len(my_list):
    print(my_list[index])
    index+=1 # increment by one!!
    # you can either use while or for to go through
    # your list(Array)

# I have an array(list) I want to go through to find something!

scores=[87,75,98,100,82,72,88,92,62,78]

# Create a boolean variable which act as a flag!
def find_the_mark():
    found=False
    mark=int(input('Tell me what mark you want me to find?'))

    index=0
    while found==False and index < len(scores):
        if scores[index]==mark:
            found=True
        else:
            index+=1 # when you use while loop you need
          #index incrementation...
    if found:
        print('you earned', mark,"on test number",str(index+1))
    else:
        print("Sorry we couldnt find it!")

# how we sent a list(array) to a module or function!

# In Python there is no declaring arrays[list]

def set_to_zero(lists):
    index=0
    while index<len(lists):
        lists[index]=0
        index+=1
print(scores)
def get_total(value_list):
    total=0
    for num in value_list:
        total+=num
    return total
print('The total is',get_total(scores))
set_to_zero(scores)
print(scores)
print('The total is',get_total(scores))

# 2D and 3D arrays list

my_list=[[1, 2, 3 , 4],
         [5, 6, 7 , 8],
         [9,10, 11,12]] # 3X4

print(my_list)
print(my_list[1]) # 2D arrays the first set of []
# indicates the row index number (index+1= row number)
print(my_list[1][2])

print('=================')
# we need a for loop for each dimension...

row=0
while row < len(my_list): # the row number
    col=0
    while col< len(my_list[row]):
        print('my_list[',row,'][',col,']=',my_list[row][col])
        col+=1
    row+=1

print('=============')
# Declare a 2D array(list)
my_list=[[0,0,0],[0,0,0],[0,0,0]]
print(my_list)
def fill_up():
    while True:
        row=int(input('Enter the row : '))
        col=int(input('Enter the col: '))
        val=int(input('Enter the value: '))
        # turn the col and row numbers to col and row
        #index!
        row-=1 # subtracing by one
        col-=1 # subtracing by one
        my_list[row][col]=val
        print('You entered:',val,'For row',str(row+1)
              ,'and col:',str(col+1))
        print(my_list)
        confirm=input('do you have another one?')
        if (confirm=='no' or confirm=='No'):
            break

# 3 dimension...


my_list1=[[[[1,2],[3,4]]
        ,[[5,6],[7,8]]],
        [[[9,10],[11,12]]
        ,[[13,14],[15,16]]],
        [[[17,18],[19,20]]
        ,[[21,22],[23,24]]]]
print(my_list1)
print(my_list1[1])
print(my_list1[1][1])
print(my_list1[1][1][0][1])
print(len(my_list1))
print(len(my_list1[2]))
print(len(my_list1[2][1]))
print(len(my_list1[2][1][1]))
print(my_list1[2][1][1][1])
# for each dimension I need a loop!
for x in range(len(my_list1)):
    #print(x)
    for y in range(len(my_list1[x])):

        for z in range(len(my_list1[x][y])):

            for t in range(len(my_list1[x][y][z])):

                print('mylist1[',x,'][',y,'][',z,'][',t,']=',
                      my_list1[x][y][z][t])