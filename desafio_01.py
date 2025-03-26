# O programa deve começar solicitando ao usuário que insira seu nome.

nome= input("Digite seu nome: ")

# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.

salario = float(input("Digite o valor do seu salario: "))

# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, 
# que também pode ser um número decimal.

bonus = float(input("Digite o valor o bonus: "))

# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus

valor_do_bonus = 1000 + salario * bonus 
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato:
#  "Olá [nome], o seu valor bônus foi de 5000".

print(f"ola{nome}, o seu bonus foi de {valor_do_bonus} ")