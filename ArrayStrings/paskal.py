from typing import List, Any

#this question is from the 02/04/2023 day challenge

# Given an integer numRows,
# return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#                     |1|
#                    |1|1|
#                   |1|2|1|
#                  |1|3|3|1|
#                 |1|4|6|4|1|
#               |1|5|10|10|5|1|


def generate_triangle(numRows: int) -> List[List[int]]:
    triangle = []
    for i in range(numRows):
        triangle.append([])
        triangle[i].append(1)
        for j in range(1, i):
            triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        if i != 0:
            triangle[i].append(1)
    return triangle




