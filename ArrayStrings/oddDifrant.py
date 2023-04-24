# You are given an array of equal-length strings words.
# Assume that the length of each string is n.
#
# Each string words[i] can be converted into a difference integer
# array difference[i] of length n - 1
# where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2.
# Note that the difference between two letters is the difference between their positions
# in the alphabet i.e. the position of 'a' is 0, 'b' is 1, and 'z' is 25.
#
# For example, for the string "acb", the difference integer array is [2 - 0, 1 - 2] = [2, -1].
# All the strings in words have the same difference integer array, except one.
# You should find that string.
#
# Return the string in words that has different difference integer array.

# Example 1:
# Input: words = ["abcd","eacd","eccd","eecd","eeed"]
# Output: "eecd"
# Explanation: The difference arrays of all the strings are:
# ["eacd" - "abcd"] = [4, 1, -1, 0]
# ["eccd" - "eacd"] = [-1, 1, 0, 0]
# ["eecd" - "eccd"] = [0, 0, -1, 0]

def find_difference(words: list[str]) -> str:
    #implement your code here
    return ""


#~~~~~~~~~~~~~~~~~~test~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    print(find_difference(["abcd","eacd","eccd","eecd","eeed"]))
    if find_difference(["abcd","eacd","eccd","eecd","eeed"]) == "eacd":
        print("pass 1 test")
    else:
        print("fail 1 test")
    if find_difference(["aaa","bob","ccc","ddd"]) == "bob":
        print("pass 2 test")
    else:
        print("fail 2 test")

