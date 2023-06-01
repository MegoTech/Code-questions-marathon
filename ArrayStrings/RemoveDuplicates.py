#this quastion is for 28.03.2023 daily coding problem

#Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

#Return k after placing the final result in the first k slots of nums.

#Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
def remove_duplicates(nums: list) -> int:
    n = 0
    for i in range(1 ,len(nums)):
       if nums[n] != nums[i]:
            n += 1
            nums[n] = nums[i]

    return nums[:max(nums)]

list1 = [1,1,2,3,4,5,5,5,6,6,7]
print(remove_duplicates(list1))




#~~~~~~~~~~~~~~~~~~test~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    remove_duplicates([1, 1, 2])
    if remove_duplicates([1, 1, 2]) == 2:
        print("pass 1 test")
    else:
        print("fail 1 test")
    if remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == 5:
        print("pass 2 test")
    else:
        print("fail 2 test")
