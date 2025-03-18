# Pilhas

## O que são Pilhas?

Pilhas são estruturas de dados lineares que seguem o princípio LIFO (Last In, First Out), ou "Último a Entrar, Primeiro a Sair". Isso significa que o último elemento adicionado à pilha será o primeiro a ser removido.

Uma pilha pode ser visualizada como uma pilha de pratos, onde o último prato colocado (no topo) é o primeiro a ser retirado.

## Operações Principais

As operações básicas em uma pilha são:

1. **Empilhar (Push)**: Adiciona um elemento ao topo da pilha.
   - Complexidade: O(1)

2. **Desempilhar (Pop)**: Remove o elemento do topo da pilha e o retorna.
   - Complexidade: O(1)

3. **Topo (Top/Peek)**: Retorna o elemento do topo da pilha sem removê-lo.
   - Complexidade: O(1)

4. **Verificar se está vazia (isEmpty)**: Verifica se a pilha está vazia.
   - Complexidade: O(1)

5. **Tamanho (Size)**: Retorna o número de elementos na pilha.
   - Complexidade: O(1)

## Tipos de Implementações

### Pilha Baseada em Array

Pode ser implementada utilizando um array, onde o topo da pilha é representado pelo último elemento.

**Vantagens**:
- Implementação simples
- Acesso rápido ao topo da pilha
- Uso eficiente de memória

**Desvantagens**:
- Tamanho máximo fixo (a menos que seja redimensionada)
- Redimensionamento pode ser ineficiente

### Pilha Baseada em Lista Encadeada

Pode ser implementada utilizando uma lista encadeada, onde o topo da pilha é representado pelo primeiro nó.

**Vantagens**:
- Tamanho dinâmico
- Não requer redimensionamento
- Fácil inserção e remoção

**Desvantagens**:
- Maior uso de memória devido aos ponteiros
- Não permite acesso aleatório

## Aplicações

1. **Avaliação de expressões matemáticas**: Para converter expressões infixa para posfixa e para avaliar expressões posfixa.

2. **Verificação de parênteses balanceados**: Para verificar se os parênteses em uma expressão estão balanceados.

3. **Conversão de números decimais para binários**: Para converter números para diferentes bases.

4. **Algoritmos de backtracking**: Como busca em profundidade (DFS) em grafos.

5. **Gerenciamento da memória de chamadas de função**: Para armazenar endereços de retorno e variáveis locais.

6. **Desfazer/refazer operações em editores de texto**: Para manter um histórico de ações.

7. **Navegação em páginas web (botão voltar)**: Para armazenar as páginas visitadas.

## Exemplo de Uso: Verificação de Parênteses Balanceados

Um problema clássico que demonstra o uso de pilhas é verificar se uma expressão possui parênteses, colchetes e chaves balanceados. Por exemplo, a expressão "{[()()]}" está balanceada, enquanto "{[(])" não está.

O algoritmo funciona assim:
1. Percorrer a expressão caractere por caractere.
2. Se encontrar um caractere de abertura (`(`, `[`, `{`), empilhar.
3. Se encontrar um caractere de fechamento (`)`, `]`, `}`), verificar se o topo da pilha é o caractere de abertura correspondente. Se for, desempilhar. Senão, a expressão não está balanceada.
4. Ao final, se a pilha estiver vazia, a expressão está balanceada. Caso contrário, não está.

## Implementação em Python

```python
class Pilha:
    def __init__(self):
        self.itens = []
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def empilhar(self, item):
        self.itens.append(item)
    
    def desempilhar(self):
        if self.esta_vazia():
            raise Exception("Não é possível desempilhar de uma pilha vazia")
        return self.itens.pop()
    
    def topo(self):
        if self.esta_vazia():
            raise Exception("A pilha está vazia")
        return self.itens[-1]
    
    def tamanho(self):
        return len(self.itens)
```

Esta implementação utilizando uma lista é eficiente para pilhas, pois as operações `append()` e `pop()` sem argumentos têm complexidade amortizada O(1).