def calculator(n1, n2, oper):
    if oper == '+':
        return n1 + n2
    elif oper == '-':
        return n1 - n2
    elif oper == '*':
        return n1 * n2
    elif oper == '/':
        return n1 / n2
    elif oper == '//':
        return n1 // n2
    elif oper == '%':
        return n1 % n2
    else:
        print('Invalid operator..')
        return 0

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
op = input('Input operator among +, -, *, /, //, %: ')

print(calculator(num1, num2, op))
