'''
In Python we have list instead of array!
A list is similar that a traditional array!

'''

even_number=[2,4,6,8,10,12,14]
names=['Hesam',"Alex","Tony","Robert"]
print(even_number)
print(even_number[0])
print(even_number[3])
print(even_number[4])
print(names)
print(names[0])
print(names[3])
print(names[2])
sum=0
for index in range(len(even_number)):
    print(even_number[index])
    sum=sum+even_number[index]

print("The sum of ",even_number,"is ",sum)
print("The average is ",sum/len(even_number))

my_list=[10,20,30,40]
index=0
while index < len(my_list):
    print(my_list[index])
    index+=1

scores=[87,75,98,100,82,72,88,92,62,78]

#create a boolean variable to act as a flag
found=False
#mark=100
mark=int(input("Tell me what mark you want to find"))
index=0
while found==False and index < len(scores):
    if scores[index]==mark:
        found=True
    else:
        index+=1

if found:
    print("you earned",mark," on test number ",str(index+1))
else:
    print("We could not find it")

#==========Function, Modules and Lists...
def set_to_zero(numbers):
    index=0
    while index<len(numbers):
        numbers[index]=0
        index+=1


def get_total(value_list):
    total=0
    for num in value_list:
        total+=num
    return total

my_list=[1,2,3,4,5]
print(my_list)
sum=get_total(my_list)
average=sum/len(my_list)

print("The sum of array ",my_list,"is ",sum)
print("The average of array ",my_list,"is ",average)
set_to_zero(my_list)

sum=get_total(my_list)
average=sum/len(my_list)

print("The sum of array ",my_list,"is ",sum)
print("The average of array ",my_list,"is ",average)
print(my_list)

# 2D and 3D arrays or lists!!

my_list=[[1,2,3,],
         [4,5,6,],
         [7,8,9,]] #3X3

print(my_list)
print(my_list[1])
print(my_list[1][2])
print(my_list[2][0])
NUM_ROWS=3
NUM_COLS=3
for index in range(NUM_ROWS):
    for index1 in range(NUM_COLS):
        print("Row: ",str(index+1),"Column:",str(index1+1),
              "=",my_list[index][index1])

my_list=[[1,2],
         [1,2,3],
         [1,2,3,4]]
print("===============================")
print(my_list)
for index in range(len(my_list)):
    for index1 in range(len(my_list[index])):
        print("Row: ",str(index+1),"Column:",str(index1+1),
              "=",my_list[index][index1])

my_list=[[0,0,0],[0,0,0],[0,0,0]]

print(my_list)
row=0

while row < len(my_list):
    col = 0
    while col <len(my_list[row]):
        my_list[row][col]=int(input('Enter a score:'))
        print("you entered:",my_list[row][col],
              "for row",str(row+1),'and column',str(col+1))
        print(my_list)
        col+=1
    row+=1

print(my_list)
print('=======================')
my_list=[[0,0,0],[0,0,0],[0,0,0]]
print(my_list)

while True:
    row=int(input(" Enter the row:"))
    col=int(input("Enter the col:"))
    val=int(input('Enter the value:'))
    row-=1
    col-=1
    my_list[row][col]=val
    print("you entered:",val,"for row:",str(row+1),"and col:",str(col+1))
    print(my_list)

    confirm=input("do you have another number")

    if(confirm=='no'or confirm=='No'):
        break

my_list1=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(my_list1)
for index3 in range(len(my_list1)):
    for index4 in range(len(my_list1[index3])):
        for index5 in range(len(my_list1[index3][index4])):
            print("the value of my_list1[",index3,"]","[",index4,"]","[",index5,"] is"
                  ,my_list1[index3][index4][index5])


