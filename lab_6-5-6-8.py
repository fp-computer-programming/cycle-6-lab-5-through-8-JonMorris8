"""
*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_6-5
Create a program that will take a list (of numbers) of any length and return the highest and lowest value in the list. If the list does not have at least 2 unique numbers, return the string: “error: list does not meet specifications”)
hint: test the program on lists of 0,1,2 + lengths, as well as lists that do and do not meet specifications! 
"""
#author-Jon_morris

if len(set(lst)) < 2:
    return "error: list does not meet specification"
else:
    return min(lst), max(lst)

my_list = [3, 5, 1, 8, 2, 9]
result = find_extremes(my_list)
print(result)

________________________________________________________________________________
"""
Create a Python file named lab_6-6

Create a program that asks a user to input 5 unique words.
Construct a list of the 5 input values, in the order that the user gave them.
Have the program display a list where each index corresponds to the length of the word given by the user at the corresponding index.
You may assume accurate input values. NO LOOPS
"""
#author- Jon Morris
#ask user to input 5 words
word1 = input("enter word 1: ")
word2 = input("enter word 2: ")
word3 = input("enter word 3: ")
word4 = input("enter word 4: ")
word5 = input("enter word 5: ")

#make a list of 5 input values in order user gave
word_list = [word1, word2, word3, word4, word5]

#show a list of each index corresponds to the lenght given by the user
length_list = [len(word1), len(word2), len(word3), len(word4), len(word5)]
print(length_list)
_________________________________________________________________________________
"""
Create a Python file named lab_6-7
Create a program that asks a user to input 3 numeric values
Construct a list of the 3 input values, in the order that the user gave them.
Have the program display a list with each of the values as integers that have been doubled 
You may assume accurate input values.
"""
#author-Jon Morris
#ask to make a input with 3 number values
num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))        
num3 = int(input("enter number 3:"))

#ask to list 3 input values in the oprder that the user gave them
num_list = [num1, num2, num3]

#display a list with each of the values as integers that have been doubled
doubled_list = [num*2 for num in num_list]


_________________________________________________________________________________
"""
Create a Python file named lab_6-8
Create a program that asks a user to input 3 numeric values
Construct a list of the 3 input values, in the order that the user gave them.
Have the program display the string “even” if all numbers in the list are even.
Have the program display the string “odd” if all numbers in the list are odd.
Have the program display the string “mixed” if the numbers in the list are both even and odd.
You may assume accurate input values. You may NOT use a loop. 
"""
#author- Jon Morris
#ask for 3 numeric values
num1 = int(input("enter number 1:"))
num2 = int(input("enter number 2:"))        
num3 = int(input("enter number 3:"))

#construct a list of the 3 input values in the order the user gave them
num_list = [num1, num2, num3]

#display whether the numbers in the list are all even, all odd, or mixed
if all(num % 2 == 0 for num in num_list):
    print("even")
elif all(num % 2 == 1 for num in the num_list):
    print("odd")
else:
    print("mixed")