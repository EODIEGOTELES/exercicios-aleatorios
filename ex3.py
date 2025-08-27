import math

# Lê o comprimento dos catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calcula a hipotenusa
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Mostra o resultado com duas casas decimais
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")