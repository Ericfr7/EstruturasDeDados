from collections import deque

class Fila:
    """
    Implementação de uma fila utilizando a estrutura deque do Python,
    que oferece operações eficientes tanto no início quanto no final.
    """
    def __init__(self):
        """Inicializa uma fila vazia."""
        self.itens = deque()
    
    def esta_vazia(self):
        """Verifica se a fila está vazia."""
        return len(self.itens) == 0
    
    def enfileirar(self, item):
        """Adiciona um item ao final da fila."""
        self.itens.append(item)
    
    def desenfileirar(self):
        """Remove e retorna o item do início da fila."""
        if self.esta_vazia():
            raise IndexError("Não é possível desenfileirar de uma fila vazia")
        return self.itens.popleft()
    
    def frente(self):
        """Retorna o item do início da fila sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        return self.itens[0]
    
    def tamanho(self):
        """Retorna o número de itens na fila."""
        return len(self.itens)
    
    def __str__(self):
        """Retorna uma representação em string da fila."""
        return str(list(self.itens))


class FilaCircular:
    """
    Implementação de uma fila circular usando um array.
    A fila circular é uma otimização de espaço para filas baseadas em arrays.
    """
    def __init__(self, capacidade=10):
        """Inicializa uma fila circular com a capacidade especificada."""
        self.capacidade = capacidade
        self.itens = [None] * capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho_atual = 0
    
    def esta_vazia(self):
        """Verifica se a fila circular está vazia."""
        return self.tamanho_atual == 0
    
    def esta_cheia(self):
        """Verifica se a fila circular está cheia."""
        return self.tamanho_atual == self.capacidade
    
    def enfileirar(self, item):
        """Adiciona um item ao final da fila circular."""
        if self.esta_cheia():
            raise IndexError("Não é possível enfileirar em uma fila cheia")
        
        self.itens[self.fim] = item
        self.fim = (self.fim + 1) % self.capacidade
        self.tamanho_atual += 1
    
    def desenfileirar(self):
        """Remove e retorna o item do início da fila circular."""
        if self.esta_vazia():
            raise IndexError("Não é possível desenfileirar de uma fila vazia")
        
        item = self.itens[self.inicio]
        self.itens[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho_atual -= 1
        return item
    
    def frente(self):
        """Retorna o item do início da fila circular sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        return self.itens[self.inicio]
    
    def tamanho(self):
        """Retorna o número de itens na fila circular."""
        return self.tamanho_atual
    
    def __str__(self):
        """Retorna uma representação em string da fila circular."""
        if self.esta_vazia():
            return "[]"
        
        resultado = []
        indice = self.inicio
        for _ in range(self.tamanho_atual):
            resultado.append(self.itens[indice])
            indice = (indice + 1) % self.capacidade
        
        return str(resultado)


class FilaPrioridade:
    """
    Implementação simples de uma fila de prioridade.
    Itens com menor valor de prioridade são atendidos primeiro.
    """
    def __init__(self):
        """Inicializa uma fila de prioridade vazia."""
        self.itens = []
    
    def esta_vazia(self):
        """Verifica se a fila de prioridade está vazia."""
        return len(self.itens) == 0
    
    def enfileirar(self, item, prioridade):
        """
        Adiciona um item à fila de prioridade.
        Os itens são ordenados pelo valor de prioridade (crescente).
        """
        elemento = (prioridade, item)
        
        # Insere o elemento na posição correta para manter a ordenação
        if self.esta_vazia():
            self.itens.append(elemento)
        else:
            inserido = False
            for i, (p, _) in enumerate(self.itens):
                if prioridade < p:
                    self.itens.insert(i, elemento)
                    inserido = True
                    break
            if not inserido:
                self.itens.append(elemento)
    
    def desenfileirar(self):
        """Remove e retorna o item de maior prioridade (menor valor)."""
        if self.esta_vazia():
            raise IndexError("Não é possível desenfileirar de uma fila vazia")
        
        # Retorna apenas o item, sem a prioridade
        return self.itens.pop(0)[1]
    
    def frente(self):
        """Retorna o item de maior prioridade sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        return self.itens[0][1]
    
    def tamanho(self):
        """Retorna o número de itens na fila de prioridade."""
        return len(self.itens)
    
    def __str__(self):
        """Retorna uma representação em string da fila de prioridade."""
        return str([(p, i) for p, i in self.itens])


# Exemplo de uso
if __name__ == "__main__":
    print("=== Fila Simples ===")
    fila = Fila()
    print(f"Fila inicial: {fila}")
    
    print("\nEnfileirando elementos...")
    for i in range(1, 6):
        fila.enfileirar(i * 10)
        print(f"Enfileirado {i * 10}, fila atual: {fila}")
    
    print(f"\nElemento na frente da fila: {fila.frente()}")
    print(f"Tamanho da fila: {fila.tamanho()}")
    
    print("\nDesenfileirando elementos...")
    while not fila.esta_vazia():
        print(f"Desenfileirado {fila.desenfileirar()}, fila atual: {fila}")
    
    print("\n=== Fila Circular ===")
    fila_circular = FilaCircular(5)
    print(f"Fila circular inicial: {fila_circular}")
    
    print("\nEnfileirando elementos na fila circular...")
    for i in range(1, 6):
        fila_circular.enfileirar(i * 5)
        print(f"Enfileirado {i * 5}, fila atual: {fila_circular}")
    
    print(f"\nElemento na frente da fila circular: {fila_circular.frente()}")
    print(f"Tamanho da fila circular: {fila_circular.tamanho()}")
    
    print("\nDesenfileirando alguns elementos...")
    for _ in range(3):
        print(f"Desenfileirado {fila_circular.desenfileirar()}, fila atual: {fila_circular}")
    
    print("\nEnfileirando mais elementos...")
    for i in range(6, 8):
        fila_circular.enfileirar(i * 5)
        print(f"Enfileirado {i * 5}, fila atual: {fila_circular}")
    
    print("\n=== Fila de Prioridade ===")
    fila_prioridade = FilaPrioridade()
    print(f"Fila de prioridade inicial: {fila_prioridade}")
    
    print("\nEnfileirando elementos com prioridades...")
    prioridades = [(3, "Tarefa 3"), (1, "Tarefa 1"), (2, "Tarefa 2"), 
                   (5, "Tarefa 5"), (4, "Tarefa 4")]
    
    for prioridade, tarefa in prioridades:
        fila_prioridade.enfileirar(tarefa, prioridade)
        print(f"Enfileirado '{tarefa}' com prioridade {prioridade}, fila atual: {fila_prioridade}")
    
    print(f"\nElemento na frente da fila de prioridade: {fila_prioridade.frente()}")
    print(f"Tamanho da fila de prioridade: {fila_prioridade.tamanho()}")
    
    print("\nDesenfileirando elementos por ordem de prioridade...")
    while not fila_prioridade.esta_vazia():
        print(f"Desenfileirado {fila_prioridade.desenfileirar()}, fila atual: {fila_prioridade}")