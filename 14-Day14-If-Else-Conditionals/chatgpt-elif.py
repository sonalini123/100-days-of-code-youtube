# Grade Classification
# Write a program that assigns a grade based on a score. Use the following ranges:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
score = int(input("enter the number: "))

if (score >=90 and score <=100):
    print("grade is A")
elif score >=80 and score <=89:
    print("grade is B")
elif score >=70 and score <=79: 
    print("grade is C")
elif score <= 69 and score >= 69:
    print("grade is D")       
else:
    print("fail F")

# Day of the Week
# Write a program that takes a number (1-7) as input and prints the corresponding day of the week (1 for Monday, 2 for Tuesday, etc.).

number = int(input("enter the number: "))
if (number == 1 and number <=7):
 print("monday")
elif number == 2:
    print("tuesday")
elif number == 3:
    print("wednesday")
elif number == 4:
    print("thursday")
elif number == 5:
    print("friday")
elif number == 6:
    print("saturday") 
elif number == 7:
    print("sunday") 
else:
    print("wrong number")              

# Nested Discount Calculation
# Write a program that calculates the discount on a product based on the following rules:

# If the price is above $100, apply a 10% discount.
# If the price is above $200, apply an additional 5% discount.
# Print the final price after discounts.

price = int(input("enter the price: "))
if price > 100:
    discount = 0.01 * price
    # final_price = price + discount
    # print("the final_price is" ,final_price)
if price > 200:
    discount = 0.05 * price
final_price = price + discount
print("the final price is", final_price)    

# Write a program that classifies a person based on age into the following groups:

# If the person is below 18, print "Child".
# If the person is 18 or above but below 60, check:
# If the person is between 18 and 25, print "Young Adult".
# If the person is between 26 and 59, print "Adult".
# If the person is 60 or above, print "Senior".

age = int(input("enter the age:  "))
if age < 18:
    print("child")
elif age >= 18 and age < 60:
    if age >= 18 and age <=25:
        print("young adult")
if age >= 26 and age <= 59:
    print("adult")
if age >= 60:
    print("senior")                 

# Nested Login System
# Write a program that checks login credentials. Use the following conditions:

# If the username is "admin":
# Check if the password is "admin123". If correct, print "Access granted."
# If incorrect, print "Invalid password."
# If the username is "user":
# Check if the password is "user123". If correct, print "Access granted."
# If incorrect, print "Invalid password."
# If the username is neither "admin" nor "user", print "Invalid username."

username = input("enter username: ")
password = input("enter password: ")
if username == "admin":
  print("check if password = admin123 ")
  if password == "admin123":
     print("access granted")

  elif password != "admin123":
   print("invalid password")
if username == "user":
   if password == "user123":
     print("access granted")
   elif password != "user123":
    print("invalid password")
else:
 if username != "admin" or username != "admin":
      print("invalid username")

      # Nested Temperature Classification
# Write a program that classifies the weather based on temperature:

# If the temperature is below 0, print "Freezing".
# If the temperature is between 0 and 30:
# If the temperature is between 0 and 15, print "Cold".
# If the temperature is between 16 and 30, print "Warm".
# If the temperature is above 30, print "Hot".

temp = int(input("enter the temp: "))
if temp == 0:
    print("freezing")
if 0 <= temp <=30:
    if 0 <= temp <= 15:
        print("cold")     
    elif 16<= temp <=30:
        print("warm")
else:
    if temp > 30:
        print("hot")        