def search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        center = (start+end)//2
        if nums[center] == target:
            return center
        elif nums[center] > target:
            end = center-1
        else:
            start = center+1

    return -1

print(search([-1,0,3,5,9,12], target=3))
