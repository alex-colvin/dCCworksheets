# Problems to solve

# 1. Write a function that takes in a string of “Packers” and takes the first and last character of the string, concatenates them together to form a new string variable, then print that string to the console
# Define the function 
def get_first_last_letter (string):
    #Capture the first letter of the string and store as a variable. 
    first_letter = string[0]
    #Capture the second letter of the string and store as a variable. 
    last_letter = string[-1]
    #Concatenate the letters and store as a variable
    first_and_last = first_letter + last_letter
    #Return concatenated string
    return first_and_last
#Capture function output as a variable
first_and_last = get_first_last_letter('Packers')
#Print the variable
print(first_and_last)
# a. Expected outcome: “Ps”



# 2. Peanut Butter Jelly

# a. Write a function that prints every number from 0 to 100 to the console
# b. If a number is divisible by 3, print 'peanut butter’ instead of the number
# c. If a number is divisible by 5, print ‘jelly’ instead of the number
# d. If a number is divisible by 3 and 5, print ‘peanut butter jelly’ instead of the number
# Define the function 
def peanut_butter_jelly ():
    #create a for loop that cycles through the range
    for number in range (0,100,1):
         #since it is the most selective, find numbers divisible by 3 and 5 print 'peanut butter jelly'
        if number % 3 == 0 and number % 5 == 0:
            print('peanut butter jelly')
        #find numbers divisible by 3 and print 'peanut butter'
        elif number % 3 == 0:
            print('peanut butter')
        #find numbers divisible by 5 and printer 'jelly'
        elif number % 5 == 0:
            print('jelly')
        else:
            print(number)
peanut_butter_jelly()



# 3. Write a function that takes in a single parameter called “word”. This parameter will be a string.
#define the parameter
def letter_with_index (word):
# a. Inside the function, create a variable called “final_result” and set it equal to an empty string.
    final_result = ''
# b. Loop over the letters in the word 
    for letter in word:
        # capture letters index in variable
        index = word.index(letter)
        #concatenat letter and index
        letter_index = letter + str(index)
        # append the letter and its index to the final_result variable.
        final_result += letter_index
    # c. return the final_result variable.
    return final_result
#capture function call in string
weird_string = letter_with_index('World Peace')
# c. Print to the terminal the final_result variable.
# d. Example Input: “World Peace”
# e. Example Output: “W0o1r2l3d4 5P6e7a8c9e10”
print(weird_string)
# 4. Write a function that takes in a single parameter called “ingredients”. This parameter will be a List.
def ingredient_search (ingredients):
    # a. Inside of the function, take user input that asks if the user knows what ingredient they want to search for
    user_input = input('What ingredient would you like to search for? ')
    #need to define ingredient before the loop
    ingredient = ''
    #while loop to keep to restart the operation until the ingredient matches user input
    while ingredient != user_input:
        # b. Check the List parameter and see if the user’s input is an element in the List.
            #need to cycle throught the list
        for ingredient in ingredients:
            # i. If the ingredient is present, 
            if user_input == ingredient:
                #return the string ingredient from the function
                return user_input
                break
        # ii. If the ingredient is not there, ask the user if they want to search again and restart the operation
        user_input = input('The ingredient is not there. Try another ingredient.')
            

#Need to create a list
ingredients = ['flour','butter','milk','eggs','sugar','baking soda','oil']
ingredient_match = ingredient_search(ingredients)
print(ingredient_match)

# 5. Write a function that takes in a list of strings, the logic of the function should reverse the order of the values inside the list then return it back as a new list

# a. Note: Cannot use list.reverse() for this problem

# i. Input: [“Yellow”, “Purple”, “Orange”]

# ii. Output: [“Orange”, “Purple”, “Yellow”]


# 6. Write a function that takes in a single parameter called ‘names’.

# a. When you call the function, pass in a list containing 6 different names.

# b. The function should create and return a new list filled with any name from the ‘names’ parameter that contains more than 4 characters.

# c. Ex Input: [‘Rebecca’, ‘Sam’, ‘Bob’, ‘Dante’, ‘Monica’, ‘Brad’]

# d. Ex Output: [‘Rebecca’, ‘Dante’, ‘Monica’]