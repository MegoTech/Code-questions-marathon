#this quastion is for 28.03.2023 daily coding problem

#Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

#Return k after placing the final result in the first k slots of nums.

#Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
def remove_duplicates(nums: list) -> int:
    # Fill this in.
    ##style 1
    # i = 0
    # while i < len(nums):
    #     if nums[i] == nums[i + 1]:
    #         nums.remove(nums[i])
    #     else:
    #         i += 1
    #
    # return len(nums)
    ##style 2
    # for j in range(1, len(nums)):
    #     if nums[i] != nums[j]:
    #         i += 1
    #         nums[i] = nums[j]
    # return i + 1
    #implement your code here
    return 0
