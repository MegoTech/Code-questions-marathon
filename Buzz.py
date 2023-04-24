# #this questin is for the 04/04/2023 day challenge
#
# Given an integer n,
# return a string array answer(1 - indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible
# by
# 3 and 5.
# answer[i] == "Fizz" if i is divisible
# by
# 3.
# answer[i] == "Buzz" if i is divisible
# by
# 5.
# answer[i] == i( as a
# string) if none of the above conditions are true.

def fizz_buzz(n: int) -> list:
    #implement your solution here
    return [str(i) if i % 3 and i % 5 else "Fizz" * (not i % 3) + "Buzz" * (not i % 5) for i in range(1, n + 1)]