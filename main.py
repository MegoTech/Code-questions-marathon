
from RemoveDuplicates import remove_duplicates


#here is the test code

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pased = 0
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    if k == 2 and nums[:k] == [1, 2]:
        pased += 1
        print("Test 1 Passed")
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    if k == 5 and nums[:k] == [0, 1, 2, 3, 4]:
        pased += 1
        print("Test 2 Passed")
    if pased == 2:
        print('Done! Good Job! Alufffffffffffffffff!!!!!!')
    elif pased == 1:
        print('only one test passed, try again')
    else:
        print('No test passed, try again')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
