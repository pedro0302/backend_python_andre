valor_hora = 25
hora_trabalhadas = 160

# Cálculo do salário bruto
salario_bruto = valor_hora + hora_trabalhadas

#Cálculo dos descontos 
#Cálculo dos descontos 
desconto_ir = salario_bruto * 0.11 # 11%
desconto_inss = salario_bruto * 0.08 # 8%
descontos_sindicato = salario_bruto * 0.05 # 5%

# Cálculo do salário líquido
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + descontos_sindicato)

# Exibição dos resultados
print(f'Salário Bruto: R$ {salario_bruto:.2f}')
print(f'Desconto IR: R$ {desconto_ir:.2f}')
print(f'Desconto INSS: R$ {desconto_inss:.2f}') 
print(f'Desconto Sindicato: R$ {descontos_sindicato:.2f}')
print(f'Salário Líquido: R$ {salario_liquido:.2f}')