#Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must appear
# as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

def towArrayIntersection(nums1: list[int], nums2: list[int]) -> list[int]:

    return []
#create a new function and the name is will be towArrayIntersection with your name
#like this:
# def towArrayIntersectionYourName(nums1: list[int], nums2: list[int]) -> list[int]:
#   #implement your code here
#   return []

#implement your code here


#~~~~~~~~~~~~~~~~~~test~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    print(towArrayIntersection([1,2,2,1], [2,2]))
    if towArrayIntersection([1,2,2,1], [2,2]) == [2,2]:
        print("pass 1 test")
    else:
        print("fail 1 test")
    if towArrayIntersection([4,9,5], [9,4,9,8,4]) == [4,9]:
        print("pass 2 test")
    else:
        print("fail 2 test")



