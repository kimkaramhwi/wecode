def move_zeroes(nums):
  last_zero = 0
  
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[i], nums[last_zero] = nums[last_zero], nums[i]
      last_zero += 1
      
  return nums
nums = [1,0,9,0,12]
print(move_zeroes(nums))