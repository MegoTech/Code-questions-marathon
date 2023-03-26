
from RemoveDuplicates import remove_duplicates


#here is the test code

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    if k == 2 and nums[:k] == [1, 2]:
        print("Test 1 Passed")
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    if k == 5 and nums[:k] == [0, 1, 2, 3, 4]:
        print("Test 2 Passed")
    print('Done! Good Job! Alufffffffffffffffff!!!!!!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
