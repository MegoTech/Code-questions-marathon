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

def count_char(string):
    dic_list = {}
    res_list = []
    for i in string:
        key = i
        if key not in dic_list:
            dic_list[key] = 1
        else:
            dic_list[key] += 1

    for key, val in reversed(sorted(dic_list.items(), key=lambda x: x[1])):
        res_list.append((key, val))

    return res_list

string = 'hello world'
print(count_char(string))