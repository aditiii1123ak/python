def insertion_sort(array):
    for a in range(1,len(array)):
        b=a
        while b > 0 and array[b] < array[b-1]:
            array[b-1],array[b] = array[b],array[b-1]
            b-=1
            print(array)
            #driver code       
array=[]
insertion_sort(array)
