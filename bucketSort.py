# Bucket sort in python
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    
             
def bucketSort(x):
    arr = []
    slot = 10 
                 
    for i in range(slot):
        arr.append([])
         
    # Put array elements in different buckets
    for j in x:
        index = int(slot*j)
        arr[index].append(j)
     
    # Sort individual buckets
    for i in range(slot):
        arr[i] = insertionSort(arr[i])
         
    # concatenate the result
    k = 0
    for i in range(slot):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
 
# Driver Code
x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))
