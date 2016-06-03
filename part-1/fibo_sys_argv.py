from fibo import fib
import sys

if __name__=='__main__':
  n = int(sys.argv[1]) if len(sys.argv)>1 else 0 
  print fib(n)
