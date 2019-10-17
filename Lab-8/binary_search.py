import Selection_Sort
def binary_search(aList,item):
    first=0
    last=len(aList)-1
    found=False
    while first<=last and not found:
        mid_point=(first+last)//2 #// ceil
        #print(mid_point)
        if aList[mid_point]==item:
            found=True
            #print(found)
            location=mid_point
        else:
            if item<aList[mid_point]:
                last=mid_point-1
                #print(last)
            else:
                first=mid_point+1
                #print(first)
        #print(found)
    if found:
        return location
    else:
        return "Not found!"

testList=[985,54,20,59,34,12,78,321,212,1]
print("Unsorted list:")
print(testList)
testList=Selection_Sort.selection_sort(testList)
print("The sorted list is:")
print(testList)

item=int(input("Let me know what you want to find"))

location=binary_search(testList,item)

print(location)
