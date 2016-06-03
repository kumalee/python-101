def fib(n):
  if n == 0: 
    return 0
  elif n < 2:
    return 1
  else:
    return fib(n-2) + fib(n-1)

def fib2(n):
  return 0 and n==0 or 1 and n<2 or fib2(n-1)+fib2(n-2)

def fib3(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
