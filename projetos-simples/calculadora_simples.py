def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Não é possível dividir por zero!"
    return x / y

print("Selecione a operação: +, -, *, /")
operation = input()

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operation == '+':
    print(add(num1, num2))
elif operation == '-':
    print(subtract(num1, num2))
elif operation == '*':
    print(multiply(num1, num2))
elif operation == '/':
    print(divide(num1, num2))
else:
    print("Operação inválida!")
