def selection_sort(aList):
    for fillslot in range(len(aList)-1,0,-1):
        #finding the position of the Max in the array
        position_Of_Max=0
        for location in range(1,fillslot+1):
            if aList[location]>aList[position_Of_Max]:
                position_Of_Max=location


        # swap between the highest and the location
        temp=aList[fillslot]
        aList[fillslot]=aList[position_Of_Max]
        aList[position_Of_Max]=temp
        print(aList)
    return aList


aList=[29,72,98,13,87,66,52,51,36]
print(aList)

selection_sort(aList)
