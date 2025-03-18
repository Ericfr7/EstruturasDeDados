class No:
    """Representa um nó em uma lista encadeada."""
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    """Implementação simples de uma lista encadeada para demonstrar alocação dinâmica."""
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def adicionar(self, valor):
        """Adiciona um novo nó ao final da lista."""
        novo_no = No(valor)  # Alocação dinâmica: um novo nó é criado no heap
        
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            # Percorre até o último nó
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        
        self.tamanho += 1
    
    def remover(self, valor):
        """Remove um nó com o valor especificado."""
        if self.cabeca is None:
            return False
        
        # Caso especial: remover o primeiro nó
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo  # O nó será coletado pelo garbage collector
            self.tamanho -= 1
            return True
        
        # Caso geral: procurar e remover
        atual = self.cabeca
        while atual.proximo and atual.proximo.valor != valor:
            atual = atual.proximo
        
        if atual.proximo:
            atual.proximo = atual.proximo.proximo  # O nó removido será coletado pelo garbage collector
            self.tamanho -= 1
            return True
        
        return False
    
    def imprimir(self):
        """Imprime todos os elementos da lista."""
        valores = []
        atual = self.cabeca
        
        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
            
        print(" -> ".join(valores) if valores else "Lista vazia")

def demonstrar_alocacao_dinamica():
    print("\nDemonstração de alocação dinâmica com Lista Encadeada:")
    print("-" * 60)
    
    # Cria uma nova lista encadeada (estrutura de dados dinâmica)
    lista = ListaEncadeada()
    
    # Adiciona elementos (cada elemento é alocado dinamicamente)
    print("Adicionando elementos à lista (alocação dinâmica de nós):")
    for i in range(1, 6):
        lista.adicionar(i * 10)
        print(f"Adicionado {i * 10}. ", end="")
        lista.imprimir()
    
    print("\nRemovendo elementos da lista (liberação dinâmica de memória):")
    valores_para_remover = [30, 10, 50]
    for valor in valores_para_remover:
        removido = lista.remover(valor)
        if removido:
            print(f"Removido {valor}. ", end="")
        else:
            print(f"Valor {valor} não encontrado. ", end="")
        lista.imprimir()
    
    print("\nAdicionando novos elementos após remoção:")
    for i in range(3):
        novo_valor = (i + 1) * 100
        lista.adicionar(novo_valor)
        print(f"Adicionado {novo_valor}. ", end="")
        lista.imprimir()
    
    print("\nNúmero de elementos na lista:", lista.tamanho)
    print("-" * 60)
    print("Quando a função terminar, a lista e todos os seus nós")
    print("serão coletados pelo garbage collector de Python.")

def demonstrar_lista_dinamica():
    print("\nDemonstração de alocação dinâmica com lista Python:")
    print("-" * 60)
    
    # Cria uma lista vazia (alocação dinâmica gerenciada pelo Python)
    lista = []
    print(f"Lista inicial: {lista} (Tamanho: {len(lista)})")
    
    # Adiciona elementos dinamicamente
    print("\nAdicionando elementos (a lista cresce dinamicamente):")
    for i in range(1, 6):
        lista.append(i * 5)
        print(f"Após adicionar {i * 5}: {lista} (Tamanho: {len(lista)})")
    
    # Remove elementos
    print("\nRemovendo elementos:")
    for _ in range(2):
        removido = lista.pop()
        print(f"Após remover {removido}: {lista} (Tamanho: {len(lista)})")
    
    # Insere elementos em posições específicas
    print("\nInserindo elementos em posições específicas:")
    lista.insert(1, 100)
    print(f"Após inserir 100 na posição 1: {lista} (Tamanho: {len(lista)})")
    
    # Realoca a lista com novos elementos
    print("\nRealocando com novos elementos:")
    lista.extend([200, 300, 400])
    print(f"Após estender: {lista} (Tamanho: {len(lista)})")
    
    print("-" * 60)

if __name__ == "__main__":
    print("Demonstração de Alocação Dinâmica de Memória")
    
    # Demonstra alocação dinâmica com estrutura personalizada
    demonstrar_alocacao_dinamica()
    
    # Demonstra alocação dinâmica com lista nativa do Python
    demonstrar_lista_dinamica()