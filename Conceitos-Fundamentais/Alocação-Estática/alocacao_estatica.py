def demonstracao_alocacao_estatica():
    """
    Demonstração de alocação estática de memória em Python.
    
    Apesar de Python gerenciar a memória automaticamente, podemos
    demonstrar conceitos de alocação estática através de seus equivalentes.
    """
    # Variáveis com alocação "estática" (alocadas na pilha)
    # (Em Python isso é abstraído, mas o conceito é análogo)
    
    # Tipos primitivos com tamanho fixo
    inteiro = 42                  # Normalmente 4 bytes (varia conforme implementação)
    flutuante = 3.14159           # Normalmente 8 bytes (double)
    booleano = True               # 1 byte
    
    # Array estático (tamanho definido na criação)
    # Em Python, listas são dinâmicas, mas podemos simular arrays estáticos
    tamanho_fixo = 5
    array_estatico = [0] * tamanho_fixo  # Cria um array com 5 elementos, tamanho fixo
    
    # Demonstração de operações com o array estático
    print("Array estático inicial:", array_estatico)
    
    # Modificar elementos (permitido)
    for i in range(tamanho_fixo):
        array_estatico[i] = i * 10
    
    print("Array estático após modificação:", array_estatico)
    
    # Tentar adicionar elemento (simulando comportamento estático)
    try:
        # Isto geraria um erro em um verdadeiro array estático
        # Em Python, as listas são dinâmicas, então precisamos simular a restrição
        if len(array_estatico) >= tamanho_fixo:
            raise IndexError("Não é possível adicionar elementos a um array estático")
        else:
            array_estatico.append(60)
    except IndexError as e:
        print(f"Erro: {e}")
    
    # Demonstração de matriz estática (2D)
    linhas, colunas = 3, 4
    matriz_estatica = [[0 for _ in range(colunas)] for _ in range(linhas)]
    
    print("\nMatriz estática (3x4):")
    for linha in matriz_estatica:
        print(linha)
    
    # Quando a função termina, todas as variáveis locais são automaticamente
    # removidas da pilha (desalocadas), demonstrando o ciclo de vida estático

if __name__ == "__main__":
    print("Demonstração de Alocação Estática de Memória")
    print("-" * 50)
    demonstracao_alocacao_estatica()
    
    # Neste ponto, as variáveis da função já foram desalocadas automaticamente
    print("-" * 50)
    print("Função finalizada. Todas as variáveis locais já foram desalocadas da pilha.")
    print("Esta é uma característica importante da alocação estática:")
    print("o gerenciamento automático do ciclo de vida das variáveis baseado em escopo.")