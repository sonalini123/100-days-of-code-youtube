#Write a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)

#Write a for loop to find the sum of the first 100 natural numbers.
sum = 0
for i in range(1,101):
    sum += i
    print(sum)

#Write a for loop to print each character in the string "Hello, World!".

for i in ("Hello, world!"):
    print(i)

#Write a for loop to print all even numbers between 1 and 20.

for i in range (1,21):
    if (i%2 == 0):
       print(i) 
       or
for i in range (2,21,2):
    print(i)

#Write a for loop to reverse the string "Python".
string = "python"
reversed_string = ''
for i in string:
    reversed_string = i + reversed_string
    print(reversed_string)    