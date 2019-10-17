# bubble sort! (check the pictures)

def bubbleSort(nList):

    for passnum in range(len(nList)-1,0,-1):

        for i in range(passnum):
            print(nList)
            if nList[i]>nList[i+1]:
                temp=nList[i]
                nList[i]=nList[i+1]
                nList[i+1]=temp
    return nList

nList=[5,1,4,2,8]

bubbleSort(nList)