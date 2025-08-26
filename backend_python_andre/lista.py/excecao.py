try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("O resultado é:", resultado)
except ValueError: 
    print("você não digitou um número válido.")
except ZeroDivisionError:
    print("Ocorreu um erro ao tentar dividir por zero.")
    
