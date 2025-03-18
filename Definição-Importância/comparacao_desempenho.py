import time
import random

def busca_linear(lista, elemento):
    """Implementação de busca linear em uma lista."""
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

def busca_binaria(lista, elemento):
    """Implementação de busca binária em uma lista ordenada."""
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

# Criar uma lista de tamanho n
def comparar_desempenho(tamanho=10000, repeticoes=10):
    """Compara o desempenho entre busca linear e binária."""
    # Criar lista ordenada para teste
    lista = sorted([random.randint(0, tamanho*10) for _ in range(tamanho)])
    
    # Elementos para buscar (existentes na lista)
    elementos_busca = [lista[random.randint(0, tamanho-1)] for _ in range(repeticoes)]
    
    # Teste de busca linear
    tempo_inicio = time.time()
    for elemento in elementos_busca:
        busca_linear(lista, elemento)
    tempo_linear = time.time() - tempo_inicio
    
    # Teste de busca binária
    tempo_inicio = time.time()
    for elemento in elementos_busca:
        busca_binaria(lista, elemento)
    tempo_binario = time.time() - tempo_inicio
    
    print(f"Tamanho da lista: {tamanho} elementos")
    print(f"Tempo médio de busca linear: {tempo_linear/repeticoes:.6f} segundos")
    print(f"Tempo médio de busca binária: {tempo_binario/repeticoes:.6f} segundos")
    print(f"A busca binária foi {tempo_linear/tempo_binario:.2f} vezes mais rápida")

if __name__ == "__main__":
    print("Comparação de desempenho entre busca linear e binária:\n")
    # Testar com listas de diferentes tamanhos
    for tamanho in [1000, 10000, 100000]:
        comparar_desempenho(tamanho)
        print()
        
    print("Este exemplo demonstra como a escolha da estrutura de dados e algoritmo")
    print("corretos (lista ordenada + busca binária) pode melhorar drasticamente")
    print("o desempenho em comparação com abordagens menos eficientes (busca linear).")