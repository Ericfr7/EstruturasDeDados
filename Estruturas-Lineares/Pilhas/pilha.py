class Pilha:
    """
    Implementação de uma pilha utilizando uma lista em Python.
    Uma pilha segue o princípio LIFO (Last In, First Out).
    """
    def __init__(self):
        """Inicializa uma pilha vazia."""
        self.itens = []
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0
    
    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        self.itens.append(item)
    
    def desempilhar(self):
        """Remove e retorna o item do topo da pilha."""
        if self.esta_vazia():
            raise IndexError("Não é possível desempilhar de uma pilha vazia")
        return self.itens.pop()
    
    def topo(self):
        """Retorna o item do topo da pilha sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("A pilha está vazia")
        return self.itens[-1]
    
    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return len(self.itens)
    
    def __str__(self):
        """Retorna uma representação em string da pilha."""
        return str(self.itens)


class PilhaLimitada:
    """
    Implementação de uma pilha com capacidade máxima limitada.
    """
    def __init__(self, capacidade=10):
        """Inicializa uma pilha com capacidade limitada."""
        self.capacidade = capacidade
        self.itens = []
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.itens) == 0
    
    def esta_cheia(self):
        """Verifica se a pilha está cheia."""
        return len(self.itens) >= self.capacidade
    
    def empilhar(self, item):
        """Adiciona um item ao topo da pilha, se houver espaço."""
        if self.esta_cheia():
            raise IndexError("Não é possível empilhar em uma pilha cheia")
        self.itens.append(item)
    
    def desempilhar(self):
        """Remove e retorna o item do topo da pilha."""
        if self.esta_vazia():
            raise IndexError("Não é possível desempilhar de uma pilha vazia")
        return self.itens.pop()
    
    def topo(self):
        """Retorna o item do topo da pilha sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("A pilha está vazia")
        return self.itens[-1]
    
    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return len(self.itens)
    
    def espaco_disponivel(self):
        """Retorna o espaço disponível na pilha."""
        return self.capacidade - len(self.itens)
    
    def __str__(self):
        """Retorna uma representação em string da pilha."""
        return str(self.itens)


class PilhaEncadeada:
    """
    Implementação de uma pilha utilizando uma lista encadeada.
    Esta implementação é útil quando não queremos limitar o tamanho da pilha
    e queremos evitar o redimensionamento de arrays.
    """
    class No:
        """Classe interna que representa um nó na lista encadeada."""
        def __init__(self, valor):
            self.valor = valor
            self.proximo = None
    
    def __init__(self):
        """Inicializa uma pilha encadeada vazia."""
        self.topo_no = None
        self.tamanho_atual = 0
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return self.topo_no is None
    
    def empilhar(self, item):
        """Adiciona um item ao topo da pilha."""
        novo_no = self.No(item)
        novo_no.proximo = self.topo_no
        self.topo_no = novo_no
        self.tamanho_atual += 1
    
    def desempilhar(self):
        """Remove e retorna o item do topo da pilha."""
        if self.esta_vazia():
            raise IndexError("Não é possível desempilhar de uma pilha vazia")
        
        item = self.topo_no.valor
        self.topo_no = self.topo_no.proximo
        self.tamanho_atual -= 1
        return item
    
    def topo(self):
        """Retorna o item do topo da pilha sem removê-lo."""
        if self.esta_vazia():
            raise IndexError("A pilha está vazia")
        return self.topo_no.valor
    
    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return self.tamanho_atual
    
    def __str__(self):
        """Retorna uma representação em string da pilha."""
        if self.esta_vazia():
            return "[]"
        
        valores = []
        atual = self.topo_no
        while atual:
            valores.append(atual.valor)
            atual = atual.proximo
        
        # A ordem é invertida para mostrar o topo no final da lista
        return str(valores[::-1])


# Exemplos de aplicações com pilhas
def verificar_parenteses_balanceados(expressao):
    """
    Verifica se os parênteses, colchetes e chaves em uma expressão estão balanceados.
    
    Args:
        expressao: A expressão a ser verificada.
        
    Returns:
        True se os parênteses estiverem balanceados, False caso contrário.
    """
    pilha = Pilha()
    mapeamento = {')': '(', '}': '{', ']': '['}
    
    for char in expressao:
        # Se for um caractere de abertura, empilhar
        if char in '({[':
            pilha.empilhar(char)
        # Se for um caractere de fechamento, verificar o topo da pilha
        elif char in ')}]':
            # Se a pilha estiver vazia ou o topo não corresponder ao caractere de abertura esperado
            if pilha.esta_vazia() or pilha.desempilhar() != mapeamento[char]:
                return False
    
    # A expressão está balanceada se a pilha estiver vazia no final
    return pilha.esta_vazia()


def converter_decimal_para_binario(numero_decimal):
    """
    Converte um número decimal para sua representação binária.
    
    Args:
        numero_decimal: O número decimal a ser convertido.
        
    Returns:
        A representação binária do número como uma string.
    """
    pilha = Pilha()
    
    # Tratar caso especial
    if numero_decimal == 0:
        return "0"
    
    # Converter para binário usando a pilha
    while numero_decimal > 0:
        resto = numero_decimal % 2
        pilha.empilhar(resto)
        numero_decimal //= 2
    
    # Construir a representação binária
    binario = ""
    while not pilha.esta_vazia():
        binario += str(pilha.desempilhar())
    
    return binario


def avaliar_expressao_posfixa(expressao):
    """
    Avalia uma expressão matemática na notação posfixa (RPN).
    
    Args:
        expressao: A expressão em notação posfixa como uma lista de tokens.
        
    Returns:
        O resultado da avaliação da expressão.
    """
    pilha = Pilha()
    
    for token in expressao:
        # Se for um número, empilhar
        if isinstance(token, (int, float)):
            pilha.empilhar(token)
        # Se for um operador, desempilhar operandos, calcular e empilhar resultado
        else:
            if token == "+":
                b = pilha.desempilhar()
                a = pilha.desempilhar()
                pilha.empilhar(a + b)
            elif token == "-":
                b = pilha.desempilhar()
                a = pilha.desempilhar()
                pilha.empilhar(a - b)
            elif token == "*":
                b = pilha.desempilhar()
                a = pilha.desempilhar()
                pilha.empilhar(a * b)
            elif token == "/":
                b = pilha.desempilhar()
                a = pilha.desempilhar()
                pilha.empilhar(a / b)
    
    return pilha.desempilhar()


# Exemplo de uso
if __name__ == "__main__":
    print("=== Pilha Básica ===")
    pilha = Pilha()
    print(f"Pilha inicial: {pilha}")
    
    print("\nEmpilhando elementos...")
    for i in range(1, 6):
        pilha.empilhar(i * 10)
        print(f"Empilhado {i * 10}, pilha atual: {pilha}")
    
    print(f"\nElemento no topo da pilha: {pilha.topo()}")
    print(f"Tamanho da pilha: {pilha.tamanho()}")
    
    print("\nDesempilhando elementos...")
    while not pilha.esta_vazia():
        print(f"Desempilhado {pilha.desempilhar()}, pilha atual: {pilha}")
    
    print("\n=== Verificação de Parênteses Balanceados ===")
    expressoes = [
        "{[()()]}",
        "{[(])}",
        "((()))",
        "((())",
        "(a + b) * (c - d)",
        "[(a + b) * {c - d]}"
    ]
    
    for expr in expressoes:
        resultado = "balanceada" if verificar_parenteses_balanceados(expr) else "não balanceada"
        print(f"A expressão '{expr}' está {resultado}")
    
    print("\n=== Conversão Decimal para Binário ===")
    decimais = [0, 2, 5, 10, 15, 42, 255]
    
    for decimal in decimais:
        binario = converter_decimal_para_binario(decimal)
        print(f"Decimal {decimal} em binário: {binario}")
    
    print("\n=== Avaliação de Expressão Posfixa ===")
    # Exemplo: (3 + 4) * 5 - 6 em notação posfixa é 3 4 + 5 * 6 -
    expressao_posfixa = [3, 4, '+', 5, '*', 6, '-']
    resultado = avaliar_expressao_posfixa(expressao_posfixa)
    print(f"Resultado da expressão posfixa {expressao_posfixa}: {resultado}")
    
    # Exemplo: 5 + ((1 + 2) * 4) - 3 em notação posfixa é 5 1 2 + 4 * + 3 -
    expressao_posfixa = [5, 1, 2, '+', 4, '*', '+', 3, '-']
    resultado = avaliar_expressao_posfixa(expressao_posfixa)
    print(f"Resultado da expressão posfixa {expressao_posfixa}: {resultado}")