# top = 30
top = int(input('How many Fibonacci numbers do you want to see? '))
n1 = 0
n2 = 1
count = 0
if top <= 0:
   print("Please enter a positive integer!")
elif top == 1:
   print("Fibonacci sequence up to",top,":")
   print(n1)
else:
   print("Fibonacci sequence up to",top,":")
   while count < top:
       print('{:>5}'.format(count+1,), ':', '{:>20}'.format(n1, end='\n'))
       fib = n1 + n2
       n1 = n2
       n2 = fib
       count += 1