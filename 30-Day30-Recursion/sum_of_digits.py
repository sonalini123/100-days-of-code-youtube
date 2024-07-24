def sum_of_num(n):
   if (n<10):
      return n
   else:
      return n % 10 + sum_of_num(n//10)
   
n=12345
print(sum_of_num(n))   
        