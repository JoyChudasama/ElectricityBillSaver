# Hashtag can be used to make a single line comment.
'''
For multiple lines you use triple single quotation.
You can write multiple comments lines.
'''

# Author is Hesam Akbari.

#1) Learn how to output things!

print("Hesam Akbari")
print('Hesam Akbari')
print("I'm a student in Cestar College")
print('I am a student in "Cestar" College')
print("I'm a student in \"Cestar\" college")
print(""" I'm a student in "Cestar" College""")
print("""One
     Two
  Three
Four""")
print('____________________')
print("One\n two\n three\n")
print('____________________')
print("One\t\ttwo\t\tthree\t\t")
#I'm a student in "Cestar" College.

# Variable?
age=25
money=13.75
name='Hess'
last_name='Akbari'
print(age)
print(money)
print(name,age)
print("My name is ",name)
print("My last name is ",last_name)
# variable manipulation!

a=7
b=2
c=a+b
d=a*b
e=a/b
f=a//b  # Floor!
g=a**b #5^2 exponant power!
h=a%2 # modulus (Remainder)
'''
3
2.6
2
'''
print("The sum of",a,"and",b,"=",c)
print(a,"*",b,"=",d)
print(e)
print(f)
print(g)

print(a/b)

# Input!

num1=int(input("Please enter the first integer!: "))
num2=int(input("Please enter the second integer!: "))
num3=int(input("Please enter the third integer!: "))
average=(num1+num2+num3)/3
# () %
#/* priority over +-
print("the average of %d and %d and %d is %.1f"%(num1,num2,num3,average))
print("The average is",format(average,'.1f'))

# Calculating the batting average!
# Batting average=hits/time at bat

'''
//Declare the necessary variable
Declare Integer hits
Declare Integer atBat
Declare Real battingAverage
(Input)
//Get the number of hits

Display "Enter the players' number of hits"
Input hits

Display" Enter the players' number of time at bat."
Input atBat

(process)
// calculate the batting average.
set battingAverage=hits/atBat

(output)
// Display the batting average.

Display" The player's batting average is", battingAverage.





'''

hits=int(input("Enter the players' number of hits.\n"))
atBat=int(input(" Enter the players' number of time at bat.\n"))
battingAverage=hits/atBat
print("The players' batting average is %.2f"%battingAverage)