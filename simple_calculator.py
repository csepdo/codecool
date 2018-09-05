while True:
    i = (input('Enter a numer (or a letter to exit): '))
    if i.isdigit():
        n1 = int(i)
        op = (input('Enter an operation: '))
        n2 = int(input('Enter another number: '))
        if op == 'add' or op == '+':
            result_add = str(n1 + n2)
            print('Result: '+result_add)
        elif op == 'min' or op == '-':
            result_min = str(n1 - n2)
            print('Result: '+result_min)
        elif op == 'mult' or op == '*':
            result_mult = str(n1 * n2)
            print('Result: '+result_mult)
        elif op == 'div' or op == '/':
            res_div = round(n1 / n2, 2)
            result_div = str(res_div)
            print('Result: '+result_div)
    else:
        exit()