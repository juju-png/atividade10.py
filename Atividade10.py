# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
velocidade = float(input("digite a velocidade do veiculo"))
limite_velocidade= 60

diferença_de_velocidade= velocidade - limite_velocidade

if velocidade > limite_velocidade:
    valor_multa = 7 * diferença_de_velocidade
    
    print(f"velocidade excedida em {diferença_de_velocidade} km/h.")
    print(f"Valor da multa a ser pago: R$ {valor_multa:2f}")
    
else: 
    print("velocidade dentro do limitepermitido. Sem multa")
