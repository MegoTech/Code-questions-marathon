
from RemoveDuplicates import remove_duplicates
from BuyAndSell import best_deal
from TheKWeakestRows import the_k_weakest_rows
from paskal import generate_triangle
from oneTime import single_number
from Buzz import fizz_buzz

#here is the test code

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pased = 0
    #~~~~~~~~~~~~~~~this is the test for the RemoveDuplicates.py~~~~~~~~~~~~~~~#
    # nums = [1, 1, 2]
    # k = remove_duplicates(nums)
    # if k == 2 and nums[:k] == [1, 2]:
    #     pased += 1
    #     print("Test 1 Passed")
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # k = remove_duplicates(nums)
    # if k == 5 and nums[:k] == [0, 1, 2, 3, 4]:
    #     pased += 1
    #     print("Test 2 Passed")

    #~~~~~~~~~~~~~~~this is the test for the BuyAndSell.py~~~~~~~~~~~~~~~#
    # prices = [7, 1, 5, 3, 6, 4]
    # max_profit = best_deal(prices)
    # if max_profit == 5:
    #     pased += 1
    #     print("Test 1 Passed")
    # prices = [7, 6, 4, 3, 1]
    # max_profit = best_deal(prices)
    # if max_profit == 0:
    #     pased += 1
    #     print("Test 2 Passed")

    #~~~~~~~~~~~~~~~this is the test for the TheKWeakestRows.py~~~~~~~~~~~~~~~#

    # mat = [[1, 1, 0, 0, 0],
    #         [1, 1, 1, 1, 0],
    #         [1, 0, 0, 0, 0],
    #         [1, 1, 0, 0, 0],
    #         [1, 1, 1, 1, 1]]
    # k = 3
    # rows = the_k_weakest_rows(mat , k)
    # if rows == [2, 0, 3]:
    #     pased += 1
    #     print("Test 1 Passed")
    # mat = [[1, 0, 0, 0],
    #        [1, 1, 1, 1],
    #        [1, 0, 0, 0],
    #        [1, 0, 0, 0]]
    # k = 2
    # rows = the_k_weakest_rows(mat, k)
    # if rows == [0, 2]:
    #     pased += 1
    #     print("Test 2 Passed")

    #~~~~~~~~~~~~~~~this is the test for the paskal.py~~~~~~~~~~~~~~~#
    # numRows = 5
    # triangle = generate_triangle(numRows)
    # if triangle == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]:
    #     pased += 1
    #     print("Test 1 Passed")
    # numRows = 1
    # triangle = generate_triangle(numRows)
    # if triangle == [[1]]:
    #     pased += 1
    #     print("Test 2 Passed")

    #~~~~~~~~~~~~~~~~this is the test for the oneTime.py~~~~~~~~~~~~~~~~~~#
    print('this is testing for tow questions oneTime.py and Buzz.py')
    if single_number([2, 2, 1]) == 1:
        pased += 1
        print("test 1 passed")

    if single_number([4, 1, 2, 1, 2]) == 4:
        pased += 1
        print("test 2 passed")

    #~~~~~~~~~~~~~~~~this is the test for the Buzz.py~~~~~~~~~~~~~~~~~~#
    if fizz_buzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]:
        pased += 1
        print("test 1 passed")
    if fizz_buzz(5) == ["1","2","Fizz","4","Buzz"]:
        pased += 1
        print("test 2 passed")


    if pased == 4:
        print('Done! Good Job! Alufffffffffffffffff!!!!!!')
    elif pased == 3 or pased == 2:
        print('almost there !? 2 or 3 tests passed, try again')
    elif pased == 1:
        print('only one test passed, try again')
    else:
        print('No test passed, try again')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
