
'''
Problem 1
Create a new string with the following sentence:

“You learn more from failure than from success."

Use the 1st, 4th, and last charachter to create a new string.
'''

my_string = "You learn more from failure than from success."

new_string = my_string[0] + my_string[3] + my_string[-1]

print(new_string)

'''
Problem 2
Use the same string variable from above
Use the replace() method to replace the "." with an "!"
'''
print(new_string.replace(".", "!"))\

'''
Problem 3
Use the string variable below and create a new variable that has all of the charachters from the original string as lowercase charachters
'''
new_str= "“WHEN YOU Change your thougHts, remember to ALSO change your world.”"
lower_str = new_str.lower()
print(lower_str)

'''
Problem 4
Take the new_str variable from above and make all of charachters uppercase
'''
new_str = new_str.upper();
print(new_str)

'''

String Excercises- Advanced
Complete the following practice excercises below to build up your skills with manipulating strings.

Problem 1

Create a new string with the following sentence:

“You learn more from failure than from success."


Use the 1st, 4th, and last charachter to create a new string.

[ ]

Start coding or generate with AI.
Problem 2

Use the same string variable from above
Use the replace() method to replace the "." with an "!"

[ ]

Start coding or generate with AI.
Problem 3

Use the string variable below and create a new variable that has all of the charachters from the original string as lowercase charachters

[ ]
new_str= "“WHEN YOU Change your thougHts, remember to ALSO change your world.”"
Problem 4

Take the new_str variable from above and make all of charachters uppercase

[ ]
Problem 5

Use the string variable below and the startswith() method to check and see if the string starts with the charachter "Z".
Check if it starts with the charachter "t"
'''
new_str= "There are no traffic jams along the extra mile."
print(new_str.startswith("Z"))
print(new_str.startswith("t"))

'''
Problem 6

Use the same new_str variable and the index() method to identify the index of charachter "j"
'''
print(new_str.index("j"))

'''
Problem 7
Use the same new_str variable
Use the count() method to find the number of times "t" and "o" appear in a string
Create a print statement that has both results in one statement. You can use string concatenation, fstring, or any other way you can think of!
'''
a = new_str.count("t")
b = new_str.count("o")
print("The letter 't' appears {} times and the letter 'o' appears {} times.".format(a,b))

print(f"The letter 't' appears {a} times and the letter 'o' appears {b} times.")

'''
Problem 8

Using the string below, find the length of the given string.
'''
greeting= "Good Morning!"
print(len(greeting))

'''
Problem 9

Use the string below, and documentation on string methods to find if all the charachters in a string are alpha charachters.
'''
alphabet= "abcdefghijklmnopqrstuvwxyz"
print(alphabet.isalpha())

'''
Problem 10

Use the string below to complete the following:

Use the find() method for the value "y"
Use the index() method for the value "y"
Create a comment explaining the difference between the two methods
'''
learning= "Learning is fun!"
print(learning.find("y"))
# print(learning.index("y")) This throws an error

# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found

'''
Problem 11
Use the string below to count the number of times each charachter appears in a string.
'''
count_string= "Twinkle twinkle little star, how I wonder what you are"

for x in count_string:
    print(x + ":", count_string.count(x))
