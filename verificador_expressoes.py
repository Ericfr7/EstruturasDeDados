"""
Verificador de Expressões Balanceadas

Este programa verifica se uma expressão matemática ou de programação
possui parênteses, colchetes e chaves balanceados.

Exemplos:
- Balanceados: "{[()]}", "(a + b) * [c - d]", "if (x == 1) { print(y); }"
- Não balanceados: "{[(])}", "(()", "if (x == 1) { print(y);"

Este programa demonstra o uso da estrutura de dados Pilha (LIFO - Last In, First Out).
"""

class Pilha:
    """
    Implementação de uma pilha utilizando lista.
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


def verificar_expressao(expressao):
    """
    Verifica se os parênteses, colchetes e chaves em uma expressão estão balanceados.
    
    Args:
        expressao: A expressão a ser verificada.
    
    Returns:
        True se a expressão estiver balanceada, False caso contrário.
    """
    pilha = Pilha()
    
    # Definindo os pares de caracteres correspondentes
    abertos = "({["
    fechados = ")}]"
    
    # Mapeamento entre caracteres de fechamento e seus correspondentes de abertura
    correspondentes = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for caractere in expressao:
        # Se for um caractere de abertura, empilha
        if caractere in abertos:
            pilha.empilhar(caractere)
        
        # Se for um caractere de fechamento
        elif caractere in fechados:
            # Se a pilha estiver vazia, não há correspondência
            if pilha.esta_vazia():
                return False
            
            # Verifica se o topo da pilha corresponde ao caractere de fechamento atual
            topo = pilha.desempilhar()
            if topo != correspondentes[caractere]:
                return False
    
    # A expressão está balanceada se, e somente se, a pilha estiver vazia no final
    return pilha.esta_vazia()


def mostrar_detalhes(expressao):
    """
    Mostra os detalhes do processamento da expressão, indicando o estado da pilha
    a cada passo.
    
    Args:
        expressao: A expressão a ser verificada.
    """
    pilha = Pilha()
    abertos = "({["
    fechados = ")}]"
    correspondentes = {')': '(', '}': '{', ']': '['}
    
    print(f"Expressão: {expressao}")
    print("Processamento passo a passo:")
    print("-" * 50)
    
    for i, caractere in enumerate(expressao):
        print(f"Caractere {i+1}: '{caractere}'")
        
        if caractere in abertos:
            pilha.empilhar(caractere)
            print(f"  Empilhando '{caractere}'")
        elif caractere in fechados:
            if pilha.esta_vazia():
                print(f"  Erro: Pilha vazia ao encontrar '{caractere}'")
                print("-" * 50)
                return False
            
            topo = pilha.desempilhar()
            if topo != correspondentes[caractere]:
                print(f"  Erro: Topo da pilha '{topo}' não corresponde a '{caractere}'")
                print("-" * 50)
                return False
            else:
                print(f"  Desempilhando '{topo}' que corresponde a '{caractere}'")
        else:
            print(f"  Ignorando (não é um símbolo de abertura ou fechamento)")
        
        print(f"  Estado atual da pilha: {pilha.itens}")
        print()
    
    resultado = pilha.esta_vazia()
    if not resultado:
        print(f"  Erro: Pilha não está vazia no final. Símbolos não fechados: {pilha.itens}")
    else:
        print("  Expressão balanceada!")
    
    print("-" * 50)
    return resultado


def main():
    """Função principal do programa."""
    print("==== Verificador de Expressões Balanceadas ====")
    print("Este programa verifica se os parênteses, colchetes e chaves")
    print("em uma expressão estão corretamente balanceados.")
    print()
    
    # Exemplos para demonstração
    exemplos = [
        "{[()]}",
        "{[(])}",
        "((()))",
        "((())",
        "(a + b) * [c - d]",
        "if (x == 1) { print(y); }",
        "if (x == 1) { print(y);"
    ]
    
    print("Exemplos pré-definidos:")
    for i, exemplo in enumerate(exemplos, 1):
        resultado = "balanceada" if verificar_expressao(exemplo) else "não balanceada"
        print(f"{i}. '{exemplo}' está {resultado}")
    
    print("\nDeseja testar uma expressão personalizada? (s/n)")
    opcao = input("> ").lower()
    
    if opcao == 's':
        while True:
            print("\nDigite a expressão para verificar (ou 'sair' para encerrar):")
            expressao = input("> ")
            
            if expressao.lower() == 'sair':
                break
            
            print("\nDeseja ver o processamento detalhado? (s/n)")
            detalhes = input("> ").lower()
            
            if detalhes == 's':
                resultado = mostrar_detalhes(expressao)
            else:
                resultado = verificar_expressao(expressao)
                estado = "balanceada" if resultado else "não balanceada"
                print(f"A expressão está {estado}\n")
    
    print("\nObrigado por usar o Verificador de Expressões Balanceadas!")


if __name__ == "__main__":
    main()
