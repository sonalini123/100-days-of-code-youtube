def fib(n):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  else:
    return (fib(n-1) + (n-2))
n=10
fib_series=[fib(i)for i in range(n)]
print(fib_series)
  