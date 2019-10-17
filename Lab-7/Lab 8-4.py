def main():

    endPro, totalScores, averageScores, score, number, counter = decVar()
    while endPro == "No":

        endPro, totalScores, averageScores, score, number, counter = decVar()
        number = getNum()
        totalScores = getscore(totalScores,number)
        averageScores=getAverage(totalScores,number)
        printAve(averageScores)

        endPro=input("\nDo You Want To End The Program? Yes or No? :")

        while not (endPro == 'yes' or endPro == 'no'):
            print("Please enter Yes or No :")
            endPro = input("Do you want to end the program?  Yes or No : ")
def decVar():

    endPro="No"
    totalScores=0.0
    averageScores=0.0
    score=0
    number=0
    counter=1

    return endPro, totalScores,averageScores, score, number, counter

def getNum():

    number=int(input("\n\t\t\t\tHow Many Students Took The Test? :"))

    while number < 2 or number > 30:
        print("Please enter a number between 2 and 30 (Try Again) :")

    return number

def getscore(totalScores,number):

    for counter in range(number):
        score=int(input("\nEnter Their Scores : "))

        while score < 0 or score > 100:
            print("\n\t\t\t\tPlease Enter a Number Between 0 And 100 (Try Again) :")

            score=int(input("\nEnter Their Scores :"))
        totalScores=totalScores + score

    return totalScores

def getAverage(totalScores,number):

    averageScores= totalScores / number

    return averageScores

def printAve(averageScores):

    print("\n\t\t\t\tThe Average Score Is %d"%averageScores)

main()