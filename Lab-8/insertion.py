def insertion_Sort(aList):

    for index in range(1,len(aList)):
        currentvalue=aList[index]
        position=index

        # finding the position of the number to insert!
        while position >0 and aList[position-1]>currentvalue:
            aList[position]=aList[position-1]
            position-=1 # position=position-1
        aList[position]=currentvalue
        print(aList)
    return aList

aList=[85,12,59,45,72,51]
print(aList)
insertion_Sort(aList)




