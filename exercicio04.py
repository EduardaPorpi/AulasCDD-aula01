nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu sálario: "))
filhos = int(input(f"{nome} quantos filhos você tem? "))
abono = filhos * 150
print(f"Olá {nome}, com {idade} anos seu sálario é de R${salario} com um abono salarial de R${abono}")
percentual = int(input("Digite qual a porcentagem do seu aumento: "))
aumento = (salario * percentual / 100) + salario
print(f"Com um aumento de {percentual}% seu sálario irá para R${aumento} com um abono salarial de R${abono}")
ferias = (aumento / 3)
print(f"{nome} seu abono de férias será de R${ferias}")
inss = (aumento * 0.08)
imposto_de_renda = (aumento * 0.15)
descontos = (aumento - inss) - imposto_de_renda
salario_final = (aumento + abono + ferias) - inss - imposto_de_renda
print(f"O desconto de INSS é de R${inss}")
print(f"O desconto do IR é de R${imposto_de_renda}")
print(f"{nome} você tem disponivel para gastar R${salario_final}")
