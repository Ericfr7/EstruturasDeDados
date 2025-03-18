class No:
    """
    Classe que representa um nó em uma lista encadeada.
    Cada nó contém um valor e uma referência para o próximo nó.
    """
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    """
    Implementação de uma lista encadeada simples.
    """
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def esta_vazia(self):
        """Verifica se a lista está vazia."""
        return self.cabeca is None
    
    def tamanho_lista(self):
        """Retorna o tamanho da lista."""
        return self.tamanho
    
    def adicionar_inicio(self, valor):
        """Adiciona um elemento no início da lista."""
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.tamanho += 1
    
    def adicionar_final(self, valor):
        """Adiciona um elemento no final da lista."""
        novo_no = No(valor)
        
        # Se a lista estiver vazia, o novo nó será a cabeça
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            # Percorre até o último nó
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            # Adiciona o novo nó após o último
            atual.proximo = novo_no
        
        self.tamanho += 1
    
    def adicionar_posicao(self, valor, posicao):
        """Adiciona um elemento em uma posição específica."""
        # Verificações de limites
        if posicao < 0 or posicao > self.tamanho:
            raise IndexError("Posição fora dos limites")
        
        # Caso especial: adicionar no início
        if posicao == 0:
            self.adicionar_inicio(valor)
            return
        
        # Caso especial: adicionar no final
        if posicao == self.tamanho:
            self.adicionar_final(valor)
            return
        
        # Caso geral: adicionar no meio
        novo_no = No(valor)
        atual = self.cabeca
        
        # Percorre até a posição anterior
        for _ in range(posicao - 1):
            atual = atual.proximo
        
        # Insere o novo nó entre o atual e o próximo
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        
        self.tamanho += 1
    
    def remover_inicio(self):
        """Remove o elemento do início da lista e retorna seu valor."""
        if self.cabeca is None:
            raise ValueError("Não é possível remover de uma lista vazia")
        
        valor = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        self.tamanho -= 1
        return valor
    
    def remover_final(self):
        """Remove o elemento do final da lista e retorna seu valor."""
        if self.cabeca is None:
            raise ValueError("Não é possível remover de uma lista vazia")
        
        # Caso especial: lista com apenas um elemento
        if self.cabeca.proximo is None:
            valor = self.cabeca.valor
            self.cabeca = None
            self.tamanho -= 1
            return valor
        
        # Caso geral: mais de um elemento
        atual = self.cabeca
        
        # Percorre até o penúltimo nó
        while atual.proximo.proximo:
            atual = atual.proximo
        
        # Remove o último nó e retorna seu valor
        valor = atual.proximo.valor
        atual.proximo = None
        self.tamanho -= 1
        return valor
    
    def remover_valor(self, valor):
        """Remove a primeira ocorrência de um valor específico."""
        if self.cabeca is None:
            return False
        
        # Caso especial: remover o primeiro nó
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return True
        
        # Caso geral: procurar o valor e remover
        atual = self.cabeca
        while atual.proximo and atual.proximo.valor != valor:
            atual = atual.proximo
        
        # Se encontrou o valor
        if atual.proximo:
            atual.proximo = atual.proximo.proximo
            self.tamanho -= 1
            return True
        
        return False
    
    def buscar(self, valor):
        """
        Busca um valor e retorna sua posição na lista.
        Retorna -1 se o valor não for encontrado.
        """
        atual = self.cabeca
        posicao = 0
        
        while atual:
            if atual.valor == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        
        return -1
    
    def obter(self, posicao):
        """Retorna o valor na posição especificada."""
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição fora dos limites")
        
        atual = self.cabeca
        for _ in range(posicao):
            atual = atual.proximo
        
        return atual.valor
    
    def imprimir(self):
        """Retorna uma representação em string da lista."""
        valores = []
        atual = self.cabeca
        
        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
        
        return " -> ".join(valores) if valores else "Lista vazia"


# Demonstração de uso
if __name__ == "__main__":
    lista = ListaEncadeada()
    
    print("Inserindo elementos no início:")
    for i in range(5, 0, -1):
        lista.adicionar_inicio(i)
        print(f"Adicionado {i} no início: {lista.imprimir()}")
    
    print("\nInserindo elementos no final:")
    for i in range(6, 9):
        lista.adicionar_final(i)
        print(f"Adicionado {i} no final: {lista.imprimir()}")
    
    print("\nInserindo elemento na posição 3:")
    lista.adicionar_posicao(10, 3)
    print(f"Lista após inserção: {lista.imprimir()}")
    
    print("\nRemovendo elementos:")
    print(f"Removido do início: {lista.remover_inicio()}, nova lista: {lista.imprimir()}")
    print(f"Removido do final: {lista.remover_final()}, nova lista: {lista.imprimir()}")
    
    valor_para_remover = 10
    removido = lista.remover_valor(valor_para_remover)
    print(f"Removido valor {valor_para_remover}: {removido}, nova lista: {lista.imprimir()}")
    
    print("\nBuscando valores:")
    valor_busca = 4
    posicao = lista.buscar(valor_busca)
    print(f"Posição do valor {valor_busca}: {posicao}")
    
    print("\nObtendo valor por posição:")
    pos = 2
    valor = lista.obter(pos)
    print(f"Valor na posição {pos}: {valor}")
    
    print(f"\nTamanho da lista: {lista.tamanho_lista()}")
    print(f"A lista está vazia? {lista.esta_vazia()}")