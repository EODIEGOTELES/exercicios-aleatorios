import random

def gerar_numeros_mega_sena():
    """
    Gera seis números aleatórios para a Mega-Sena.
    """
    # Cria uma lista com todos os números possíveis (de 1 a 60)
    numeros_possiveis = list(range(1, 61))
    
    # Sorteia 6 números aleatórios da lista sem repetição
    numeros_sorteados = random.sample(numeros_possiveis, 6)
    
    # Ordena os números em ordem crescente
    numeros_sorteados.sort()
    
    return numeros_sorteados

# Chama a função e armazena os números sorteados
numeros = gerar_numeros_mega_sena()

# Imprime os números para o usuário
print("Os números da Mega-Sena sorteados são:")
print(numeros)