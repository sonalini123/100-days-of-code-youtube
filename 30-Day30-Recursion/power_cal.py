def power(x,n):
 if  n==0:
  return 1
 if n==1:
  return x
 else:
  return x * power(x,n-1)
 
x=2;
n=3;
print(power(x,n))
