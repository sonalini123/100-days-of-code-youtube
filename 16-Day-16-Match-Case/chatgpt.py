# Write a program that takes a single argument and uses match to return
# "It's an integer!" if the argument is an integer, "It's a string!" if it's a string, and "Unknown type" otherwise.

user_input = input("enter anything: ")

try:
   value = int(user_input)
except ValueError:
   value = user_input
   
match value:
  case int():
    print("this is an integer") 
  case str():
    print("this is a string")
  case _:
    print("unknown type")  

# Write a function that takes a single argument and uses match with a 
# guard (an if statement) to print "Positive" if the argument is a positive number, "Negative" if it's a negative number, and "Zero" if it's zero.

user_input = int(input("enter any number: "))

match user_input:
 case x if x > 0:
    print("positive")
 case x if x < 0:
    print("negative")
 case x if x == 0:
    print("Zero")
 case _:
    print("not a number")         

# Write a function that takes a single argument and uses match to print "One", "Two", or "Three"
#  if the argument is 1, 2, or 3 respectively. For any other value, print "Other number".
user_input = int(input("enter 1,or 2 or 3: "))
match user_input:
    case x if x == 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("other num")                            