def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i],arr[min_index] = arr[min_index],arr[i]


arr = [3,5,1,6,10,9,8]
print("Before sorted: " + str(arr))
SelectionSort(arr)
print("Sorted: " + str(arr))