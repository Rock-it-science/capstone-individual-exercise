from parseInput import parseInput
from sortArray import sortArray

# Take input from user as a string
str_in = input("Enter numbers separated by commas: ")

# Feed input through both functions and print the result
print(sortArray(parseInput(str_in)))