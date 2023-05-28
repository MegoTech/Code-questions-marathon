# Write a code for a program that reads in a string and counts how many times each character
# appears. Then, print out a list of tuples where each tuple contains a character and its corresponding
# count. Starting from the most frequent letter to the least frequent one. For example:
# Input: 'hello world';
# Output:  [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
#
# Write your code tied and clear on your Python and upload your solution to github. Do not forget to
# pay attention to running-time issues and consider the additional following challenge: Try to solve
# this problem with the least number of lines of code. To do it, consider using a lambda function to
# define a custom sorting order for the list of tuples representing the character counts or Counter
# class from the collections module.

def count_char_moshe(string: str) -> list:
    #implement your code here
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    list = []
    for i in dict:
        list.append((i, dict[i]))
    list.sort(key=lambda x: x[1], reverse=True)
    return list

if __name__ == '__main__':

    print(count_char_moshe("hello world"))