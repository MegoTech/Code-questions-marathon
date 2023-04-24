#this question is for the 03/04/2023 day challenge

# Given a non-empty array of integers nums,
# every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity
# and use only constant extra space.

def single_number(nums: list) -> int:
    #implement your code here
    duplicity = {}
    for num in nums:
        if num in duplicity:
            duplicity[num] += 1
        else:
            duplicity[num] = 1
    for key, val in duplicity.items():
        if val == 1:
            return key

