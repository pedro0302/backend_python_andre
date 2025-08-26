#Sistema de Recomendação de Consumo de Água Diária

# Entrada de dados
nome = input("Digite seu nome: ")
whatsapp = input("Digite seu número do WhatsApp: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Cálculo da recomendação de água (35  por kg de peso)
agua_ml = peso * 35
agua_litros = agua_ml / 1000  # converter para litros

# Saída formatada
print("\n= Resultado =")
print(f"Nome: {nome}")
print(f"WhatsApp: {whatsapp}")
print(f"Peso: {peso:.1f} kg")
print(f"Altura: {altura:.2f} m")
print(f"IMC: {imc:.2f}")
print(f"Recomendação de água por dia: {agua_ml:.0f} ml ({agua_litros:.2f} litros)")