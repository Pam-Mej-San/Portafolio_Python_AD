operador= input ('Introduce una operación matemática (+,-,*,/): ')

num1=float(input('Introduce el primer número: '))
num2=float(input ('Introduce el segundo número: '))

if operador == '+':
    resultado= num1 + num2
    print(round(resultado,3))
elif operador == '-':
    resultado= num1-num2 
    print(round(resultado,3))
elif operador == '*':
    resultado= num1*num2
    print(round(resultado,3))
elif operador == '/':
    resultado= num1/num2 
    print(round(resultado,3))
else: 
    print(f'{operador} no es un dato válido')


