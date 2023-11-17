x = int(input('enter the first number: '))
y = int(input('enter the second number: '))
op = input('enter the operation: ')
if op == '+':
    res = x+y
elif op == '-':
        res = x-y
elif op == '*':
    res = x*y
elif op == '/':
    res=x/y
print('result: ', res)