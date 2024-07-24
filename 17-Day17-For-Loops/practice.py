#Write a program to print the multiplication table of a given number.
N = int(input("enter any number: "))
# result = 1
for i in range(1,11):
  result = N * i
  print(result)

#   Find Maximum in a List:
# Write a program to find the maximum value in a list of numbers.

# python
# Copy code
# # Example: numbers = [3, 5, 2, 8, 1]
# # Output: 8
my_list = []
N = input("enter the numbers by spaces: ")
my_list = N.split()

numbers = [int(i) for i in my_list]

#print("the list is: ", my_list)
max_number = max(numbers)
print(max_number)
