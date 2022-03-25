def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(arr)
        if not swapped: # 정렬할 부분이 없다.
            print(i, j)
            break
    return arr

arr = [1,2,9,7,5]
bubbleSort(arr)