def selectionSort(nums):
    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        print(nums)
    return nums

nums = [64, 25, 12, 22, 11]
selectionSort(nums)