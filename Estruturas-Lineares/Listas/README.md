# Listas

## O que são Listas?

Listas são estruturas de dados lineares que armazenam elementos em uma sequência ordenada. Diferentemente de arrays, que têm tamanho fixo, as listas podem crescer ou diminuir dinamicamente conforme necessário.

As listas podem ser implementadas de diferentes formas, sendo as principais:

1. **Listas baseadas em arrays** (também chamadas de listas sequenciais)
2. **Listas encadeadas** (simples, duplas ou circulares)

## Principais Operações

### Operações Básicas

- **Inserção**: Adicionar um elemento na lista
  - No início: O(1) para listas encadeadas, O(n) para arrays
  - No final: O(1) para listas encadeadas (com ponteiro para o final) e arrays dinâmicos amortizados
  - Em posição arbitrária: O(n) no pior caso

- **Remoção**: Remover um elemento da lista
  - No início: O(1) para listas encadeadas, O(n) para arrays
  - No final: O(1) para listas duplamente encadeadas ou arrays
  - Em posição arbitrária: O(n) no pior caso

- **Acesso**: Ler ou modificar um elemento
  - Por índice: O(1) para arrays, O(n) para listas encadeadas
  - Por valor: O(n) no pior caso para ambas implementações

- **Busca**: Encontrar um elemento específico
  - Busca linear: O(n)
  - Busca binária (apenas em listas ordenadas): O(log n)

## Tipos de Listas

### Lista Encadeada Simples

Uma lista encadeada simples consiste em nós, onde cada nó contém um valor e uma referência para o próximo nó. A lista mantém uma referência para o primeiro nó (cabeça).

**Vantagens**:
- Inserção e remoção eficientes no início da lista
- Tamanho dinâmico
- Não requer realocação de memória quando cresce

**Desvantagens**:
- Acesso sequencial (não permite acesso direto por índice)
- Maior uso de memória devido aos ponteiros
- Navegação apenas em uma direção

### Lista Duplamente Encadeada

Uma lista duplamente encadeada é semelhante à lista encadeada simples, mas cada nó contém referências tanto para o próximo nó quanto para o nó anterior.

**Vantagens**:
- Permite navegação em ambas as direções
- Remoção eficiente em qualquer posição (desde que se tenha uma referência ao nó)
- Facilita implementação de iteradores bidirecionais

**Desvantagens**:
- Maior uso de memória (dois ponteiros por nó)
- Maior complexidade de implementação

### Lista Circular

Uma lista circular é uma lista encadeada onde o último nó aponta de volta para o primeiro nó, formando um ciclo.

**Vantagens**:
- Permite percorrer a lista continuamente
- Útil para aplicações que requerem processamento cíclico de dados

**Desvantagens**:
- Lógica mais complexa para evitar loops infinitos durante travessias
- Maior dificuldade na detecção do fim da lista

## Aplicações

- **Histórico de navegação**: para ir para frente e para trás (lista duplamente encadeada)
- **Playlists de música**: para organizar e navegar entre músicas
- **Editores de texto**: para representar linhas de texto
- **Implementação de outras estruturas**: como pilhas, filas e deques
- **Gerenciamento de memória**: para controlar blocos de memória livre/ocupada

## Implementação em Python

```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def adicionar_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.tamanho += 1
    
    def adicionar_final(self, valor):
        if not self.cabeca:
            self.adicionar_inicio(valor)
            return
            
        novo_no = No(valor)
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no
        self.tamanho += 1
    
    def remover(self, valor):
        if not self.cabeca:
            return False
        
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return True
        
        atual = self.cabeca
        while atual.proximo and atual.proximo.valor != valor:
            atual = atual.proximo
        
        if atual.proximo:
            atual.proximo = atual.proximo.proximo
            self.tamanho -= 1
            return True
        
        return False
    
    def buscar(self, valor):
        atual = self.cabeca
        posicao = 0
        
        while atual:
            if atual.valor == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        
        return -1
    
    def imprimir(self):
        valores = []
        atual = self.cabeca
        
        while atual:
            valores.append(str(atual.valor))
            atual = atual.proximo
        
        return " -> ".join(valores) if valores else "Lista vazia"
```