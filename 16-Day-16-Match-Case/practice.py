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