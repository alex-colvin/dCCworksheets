# To be a good problem solver, it is important to be able to break problems down. One way to go about this is to write out the steps it will take to solve the problem. These steps are written down in English in a manner that is easily explainable to someone who may not be technical. The idea is that in order to code something out, you first need to have a good understanding of what it is you are attempting to solve.
# For each of the four problem solving problems below, write out the steps it will take to go about solving the problem. For example, once you are done writing out the steps for the “reverse a string” problem, you would then write out the code to solve the problem. You would then repeat the process for each ensuing problem. Ideally, this will be a good habit that you will develop and carry forward with you for all problems you encounter at devCodeCamp and beyond.
# Problems to solve
# 1.Reverse a string
# a.Write code that takes a string as input and returns the string reversed
# b.i.e. “Hello” will be returned as “olleH”
#First define the straing variable
string = 'antidisestablishmentarianism'
#Define a function
def reverse_string (string):
    #get the length of a string so we can subtract 1 and index the last letter
    length = len(string)
    #get the index of the last letter to start the word backwards
    index = length - 1
    #define variable to write letters to
    new_string = ''
    #for loop to iterate through all the letters in the string
    for letter in string:
        #append letters to new stringin reverse order
        new_string += string[index]
        #change index to count backwards
        index -= 1
    return new_string
new_string = reverse_string(string)
print(new_string)
# 2.Capitalize letter
# a.Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
#Define the string in a variable
capital = 'wwww wwww wwww wwww wwww wwww'
#Define the function
def capitalize_first_letter(string):
    #define new variable to right to
    new_string = ''
    #define new variable to catch letters after spaces
    n = ''
    actual_count_of_number_in_string = 0
    #for loop to iterate through string
    for letter in string:
        #if statement to catch first letter of the string
        if string.index(letter) == 0 and actual_count_of_number_in_string == 0:
            #add upper case letter to new string
            new_string += letter.upper()
            actual_count_of_number_in_string += 1
        #elif statement to find spaces and change variable n to next higher index
        elif letter == ' ':
            n = actual_count_of_number_in_string + 1
            #don't forget to add the space to the new string
            new_string += letter
            actual_count_of_number_in_string += 1
        #elif statement to catch letters after spaces whose index is equal to n
        elif actual_count_of_number_in_string == n:
            #added upper case letter to new string
            new_string += letter.upper()
            actual_count_of_number_in_string += 1
        #for all other letters
        else:
            #add letter to string
            new_string += letter 
            actual_count_of_number_in_string += 1   
    return new_string
first_letters_capital = capitalize_first_letter(capital)
print (first_letters_capital)
# 3.Palindrome
# a.A word, phrase, or sequence that reads the same backward as forward i.e. madam
# b.Write code that takes a user input and checks to see if it is a Palindrome and reports the result
#Define the funtion
def palindrome_check():
    #get the users input
    user_input = input("Do you know what a palindrome is? Prove it! Enter your palindrome :")
    #since we just created a function to reverse a string (above) we'll use that
    test_string = reverse_string(user_input)
    if user_input.lower() == test_string.lower():
        print(f"You really know your palindromes. {user_input.upper()} spelled backwards is {test_string.upper()}")
    else:
        print(f"{user_input} is not a palindrome.")
palindrome_check()
# 4.BONUS CHALLENGE: Compress a string of characters
# a.For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"
#looks like we are just counting the letters that happen back to back and concatenating that letter with the number of times it occured
#Define the string
string = "aaabbbbbccccaacccbbbaaabbbaaa"
#Define the function
def compression_function (string):
    #Create new string variable to write compressed segments to
    new_string = ''
    #string to hold multiple repeating letters
    repeating_letter_string = ''
    #string to convert repeating_letter_string to desired compression format
    compress_format_string = ''
    #string to check when letters change. Initially set to first letter
    previous_letter = string[0]
    #variable to count actual number in the string
    actual_count_of_number_in_string = 1
    #for loop to iterate through the string
    for letter in string:
        #if statement to check for repeating letters
        if letter == previous_letter and len(string) != actual_count_of_number_in_string:
            #add letter to repeating_letter_string variable
            repeating_letter_string += letter
            #add 1 to the actual_count variable
            actual_count_of_number_in_string +=1
        #elif the last letter int he string
        elif len(string) == actual_count_of_number_in_string:
            #add letter to repeating_letter_string variable
            repeating_letter_string += letter
            #format repeating letters into compression by getting the length of the string followed by the letter
            compress_format_string = str(len(repeating_letter_string)) + repeating_letter_string[0]
            #append to new string
            new_string += compress_format_string
        else: #when the letters change
            #format repeating letters into compression by getting the length of the string followed by the letter
            compress_format_string = str(len(repeating_letter_string)) + repeating_letter_string[0]
            #append to new string
            new_string += compress_format_string
            #reset repeating letter string with new letter
            repeating_letter_string = letter
            #reset previous letter variable
            previous_letter = letter
            #add 1 to the actual_count variable
            actual_count_of_number_in_string +=1
    return new_string
new_string = compression_function(string)
print(new_string)

        







