#this program calculates retail prices

# MARK_UP is used as a global constant for
#the makeup percentage

MARK_UP=2.5

def main():
    # Variable to control the loop
    another='y'
    while another=='y' or another=='Y':

        show_retail()

        #do this again?
        another=input("Do you have another item"
                      "(Enter y for yes?")

def show_retail():
    # get the item wholesale cost
    wholesale=float(input("Enter the item's whole sale cost"))

    #validation loop
    while wholesale <0:
        print("Error: Cost cannot be negative")
        wholesale = float(input("Enter the item's whole sale cost"))

    retail =wholesale * MARK_UP
    print('The retail price is $', format(retail,',.2f'))
main()