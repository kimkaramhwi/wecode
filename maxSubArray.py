def maxSubArray(nums):

    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i-1]+nums[i])
    print(nums)
    return max(nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))