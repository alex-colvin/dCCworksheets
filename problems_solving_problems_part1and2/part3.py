# 1. Given an array of integers, return indices of the two numbers such that they add up to a specific 
# target. You may assume that each input would have exactly one solution, and you may not use 
# the same element twice.
# a. Use Case:
# i. Given numbers in an array: [5, 17, 77, 50] 
# ii. Target: 55
#define array
array =[4, 5, 17, 77, 50]
#define target
target = 55
def exact_solution(array, target):
    #define success variable
    success = False
    #loop though the array.
    for number in array:
        #exlcude number
        rest_of_array = array.copy()
        rest_of_array.remove(number)
        #loop through the rest of the numbers
        for rest in rest_of_array:
            #if they match, print indices
            if (number + rest) == target:
                result = (array.index(number), rest_of_array.index(rest))
                #success flag to true to break other for loop
                success = True
                break
        if success == True:
            break
    return result
# 2. Palindrome is a word, phrase, or sequence that reads the same backward as forward i.e. 
# madam. Write code that takes a user input and checks to see if it is a Palindrome and reports 
# the result. You must handle spaces. 
#already wrote the code for this
import part2
part2.palindrome_check()
# 3. Given a list of integers, return a bool that represents whether or not all integers in the list can 
# form a sequence of incrementing integers
# a. Use case: 
# i. {5, 7, 3, 8, 6} → false (no 4 to complete the sequence)
# ii. {17, 15, 20, 19, 21, 16, 18} → true
#define the list
integers =[5, 7, 3, 8, 6, 4, 10]
def straight_check (integers):
#sort function is awesome
    integers.sort()
    straight_check = True
    previous_number = integers[0]
    for number in integers:
        if number != previous_number + 1 and number != integers[0]:
            straight_check = False
            break
        elif number != integers[0]:
            previous_number += 1
    return straight_check
# 4. Create a method that takes an array of positive and negative numbers. Return an array where 
# the first element is the count of the positive numbers and the second element is the sum of 
# negative numbers. 
# a. Use case: [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]
integers = [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]
def strange_request(integers):
    count = 0
    sum = 0
    for number in integers:
        if number > 0:
            count += 1
        else:
            sum += number
    result = [count, sum]
    return result
# 5. Create a method that accepts a string of space separated numbers and returns the highest and 
# lowest number as a string
# a. Use case: “3 9 0 1 4 8 10 2” → “0 10”
string = '3 9 0 1 4 8 10 2'
def high_low (string):
    integers = []
    for number in string.split():
        integers.append(int(number))
    integers.sort()
    result = (integers[0], integers[-1])
    return result
# 6. Create a method that accepts a string, check if it’s a valid email address and returns either true 
# or false depending on the valuation. Think about what is necessary to have a valid email 
# address.
# a. Use case:
# i. “mike1@gmail.com” → true
# ii. “gmail.com” → false
email = 'mike1@gmail.com'
def email_checker (email):
    #all strings are email until they fail a test 
    is_email = True
    #email address needs a top level domain suffix we'll just use a few for now
    tlds = ['.com','.org','.net','.int','.edu','.gov','.mil']
    for domain in tlds:
        if email.find(domain) != -1:
            break
        elif email.find(domain) == -1 and tlds[-1] == domain:
            is_email = False
    #email address needs an @ symbol
    if email.find('@') == -1:
        is_email = False
    #if we passed the last test perform the next 2
    if is_email == True:
        #email address needs text before the @ symbol. we'll just check that the index != 0
        if email.index('@') == 0:
            is_email = False
        #email address needs at least 1 character between @ and '.' for domain name
        if (email.index('@') + 1) == email.index('.'):
            is_email = False
    return is_email
# 7. Create a method that takes in a string and replaces each letter with its appropriate position in 
# the alphabet and returns the string
# a. Use case:
# i. “abc” → “1 2 3”
# ii. “coding is fun” → “3 15 4 9 14 7 9 19 6 21 14”
def abc_123 (string):
    #need a reference list
    abcs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = 'coding is fun'
    return_string = ''
    #for loop to iterate through string
    for letter in string:
        if letter != ' ':
            if letter == string[-1]:
                return_string += str((abcs.index(letter)+1))
            else:
                return_string += str((abcs.index(letter)+1)) + " "
    return return_string
# 8. A briefcase has a four-digit rolling-lock. Each digit is a number from 0-9 that can be rolled either 
# forwards or backwards. Write a method that returns the smallest number of turns it takes to 
# transform the lock from current combination to the target combination. One turn is equivalent 
# to rolling a number forwards or backwards by one. 
# a. Use case: 
# i. Current lock: 3893
# ii. Target lock: 5296
# for the first digit math is either 3 + x = 5 or 3 +10 -y = 5...x = 2 and y = 8
# 8 + x = (1)2 or 8 - y = 2...x =4 and y = 6 
# since the dial is 10 digits if one answer is more than 5 use the other 
# find which digit is less then add 10 and get the difference
current_lock = '3893'
target_lock = '5296'
def lock_cycles (current, target):
    # to cycle through second numer
    n = 0
    total_number_turns = 0
    #for loop to run through first number
    for digit in current_lock:
        #variables for lest typing
        first = int(digit)
        second = int(target_lock[n])
        #find which digit is less, add 10 to that then get your differences
        if first < second:
            if abs(first + 10 - second) <= 5:
                total_number_turns += abs(first + 10 - second)
                n+=1 
            else:
                total_number_turns += abs(second - first)
                n+=1
        elif first > second:
            if abs(first - second) <= 5:
                total_number_turns += abs(first - second)
            else:
                total_number_turns += abs(second + 10 - first)
                n+=1
        else:
            n+=1
    return total_number_turns
# 9. Happy Numbers
# a. A happy number is a number defined by the following process: starting with any positive 
# integer, replace the number by the sum of the squares of its digits, and repeat the 
# process until the number equals 1. An example of a happy number is 19
# 10. Given a number, return the reciprocal of the reverse of the original number, as a double. 
# a. Use case: If given 17, return 0.01408 (1/71)
import part2andhalf
part2andhalf.happy_number()