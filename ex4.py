import math

# Lê o valor do ângulo em graus
angulo_graus = float(input("Digite o valor do ângulo em graus: "))

# Converte o ângulo de graus para radianos
angulo_radianos = math.radians(angulo_graus)

# Calcula o seno, cosseno e tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Mostra os resultados com duas casas decimais
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")