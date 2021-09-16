from parseInput import parseInput
from sortArray import sortArray

# Take input from user as a string
str_in = input("Enter numbers separated by commas: ")
print(sortArray(parseInput(str_in)))