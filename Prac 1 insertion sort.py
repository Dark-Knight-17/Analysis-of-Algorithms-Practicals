def insertionSort(alist):
   for index in range(1,len(alist)): 
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue
     
alist = [55,23,98,14,69,28,47,51,21]
insertionSort(alist)
print(alist)
