#birds=100 #global
def main(): # Call the texas modules
    texas()
    #print(birds)
    # call the california modules
    california()
    #print(birds)
#main()
def texas():
    #global birds
    birds=5000 # local variable
    print('Texas has ',birds,'birds')
#print(birds)
def california():
    #global birds
    birds=8000
    print('California has',birds,'birds')
#main()
#print(birds)

