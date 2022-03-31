# 1. Happy Numbers 
# a. https://en.wikipedia.org/wiki/Happy_number 
# b. A happy number is a number defined by the following process: starting with any positive 
# integer, replace the number by the sum of the squares of its digits, and repeat the 
# process until the number equals 1. An example of a happy number is 19 
# c. Write a method that determines if a number is happy or sad 
#Define function
def happy_number ():
    user_input = input('Enter any positive number. I will tell you if it is happy ":D" or sad ":(" -')
    #variable to separate current number from user_input
    number = user_input
    #variable to write to and test off of
    sum_of_squares = 0
    #list to keep track of numbers to prevent infinite loop
    seen_numbers = [int(user_input)]
    #while statement for when number hasn't been determined to be happy or sad yet
    happy = ''
    while sum_of_squares != 1:
        #separates digits
        for digit in number:
            #adds and squares
            sum_of_squares += int(digit)**2
        #if sum is 1 number is happy
        if sum_of_squares == 1:
            happy = ':D'
            print (happy)
            break
        else:
            #check the seen numbers list
            for seen_number in seen_numbers:
                #if number repeats number is sad
                if sum_of_squares == seen_number:
                    happy = ':('
                    print (happy)
                    #to break the while loop
                    sum_of_squares = 1
                    break
            #break the while loop
            if sum_of_squares == 1:
                break
            #add number to seen numbers
            seen_numbers.append(sum_of_squares)
            #convert to string to iterate
            number = str(sum_of_squares)
            #reset sum of squares
            sum_of_squares = 0
    return happy
happy_number()
# 2. Prime Numbers 
# a. A prime number is a number that is only divisible by one and itself. 
# b. Write a method that prints out all prime numbers between 1 and 100  
#Define the function
def print_prime_number(number):
    #set variable for conditionals
    not_prime = False
    #for loop to check every number less than the number to divide the number by
    for num in range(2,number,1):
        #if number is divisible by another number it's not prime
        if number % num == 0:
            #not prime don't print number
            not_prime = True
            break
    #print prime number
    if not_prime == False:
        print (number)        
# 3. Fibonacci 
# a. A series of numbers in which each number (Fibonacci number) is the sum of the two 
# preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc. 
# b. Write a method that does the Fibonacci sequence starting at 1 
# c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a 
# number that a user inputs 
#define the function
def generate_Fibonacci ():
    #get user input
    user_input = int(input("Enter a number to Fibonaccize :"))
    #need two preceding numbers
    first_number = user_input
    second_number = 0
    if second_number == 0:
        second_number = first_number
    next_number = first_number + second_number
    #dont forget a list to append to
    fibonacci_sequence = [first_number, second_number, next_number]
    
    user_input = 'y'
    #while loop to let user control how long the list is in increments of 10 numbers
    while user_input.lower() == 'y':
        if user_input == 'y':
            #Fibonaccize 10 numbers
            for number in range(10):
                next_number = fibonacci_sequence[-1] + fibonacci_sequence [-2]
                fibonacci_sequence.append(next_number)
            for number in fibonacci_sequence:
                print (number)
        else:
            break
        user_input = input('Would you like to keep going?')
