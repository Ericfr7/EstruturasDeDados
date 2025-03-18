# Filas

## O que são Filas?

Filas são estruturas de dados lineares que seguem o princípio FIFO (First In, First Out), ou "Primeiro a Entrar, Primeiro a Sair". Isso significa que o primeiro elemento adicionado à fila será o primeiro a ser removido.

Uma fila pode ser visualizada como uma fila real (como uma fila de pessoas em um banco), onde as pessoas entram no final da fila e são atendidas pela ordem de chegada.

## Operações Principais

As operações básicas em uma fila são:

1. **Enfileirar (Enqueue)**: Adiciona um elemento ao final da fila.
   - Complexidade: O(1)

2. **Desenfileirar (Dequeue)**: Remove o elemento do início da fila e o retorna.
   - Complexidade: O(1)

3. **Frente (Front/Peek)**: Retorna o elemento do início da fila sem removê-lo.
   - Complexidade: O(1)

4. **Verificar se está vazia (isEmpty)**: Verifica se a fila está vazia.
   - Complexidade: O(1)

5. **Tamanho (Size)**: Retorna o número de elementos na fila.
   - Complexidade: O(1)

## Tipos de Implementações

### Fila Baseada em Array

Pode ser implementada utilizando um array circular para otimizar o uso de espaço.

**Vantagens**:
- Acesso rápido ao primeiro e último elemento
- Uso eficiente de memória (quando implementada como array circular)

**Desvantagens**:
- Tamanho máximo fixo (a menos que seja redimensionada)
- Redimensionamento pode ser ineficiente

### Fila Baseada em Lista Encadeada

Pode ser implementada utilizando uma lista encadeada, onde novos elementos são adicionados ao final e removidos do início.

**Vantagens**:
- Tamanho dinâmico
- Não requer redimensionamento
- Fácil inserção e remoção

**Desvantagens**:
- Maior uso de memória devido aos ponteiros
- Não permite acesso aleatório

## Variações de Filas

### Fila de Prioridade

Uma fila onde cada elemento tem uma prioridade associada e os elementos são atendidos com base na sua prioridade, não na ordem de chegada.

### Fila Circular

Uma fila implementada como um buffer circular, onde o final da fila pode estar conectado ao início.

### Deque (Double-Ended Queue)

Uma fila que permite inserções e remoções tanto no início quanto no final da fila.

## Aplicações

1. **Gerenciamento de processos em sistemas operacionais**: Para escalonar processos e tarefas.

2. **Buffers de impressoras e dispositivos de E/S**: Para armazenar temporariamente dados a serem processados.

3. **Sistemas de atendimento ao cliente**: Para gerenciar filas de espera.

4. **Algoritmos de busca em largura (BFS)**: Para explorar todos os nós de um mesmo nível antes de avançar.

5. **Processamento de transações bancárias**: Para garantir que as transações sejam processadas na ordem em que foram recebidas.

6. **Simulação de eventos discretos**: Para modelar sistemas onde eventos ocorrem em uma sequência ordenada pelo tempo.

## Implementação em Python

```python
class Fila:
    def __init__(self):
        self.itens = []
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def enfileirar(self, item):
        self.itens.append(item)
    
    def desenfileirar(self):
        if self.esta_vazia():
            raise Exception("Não é possível desenfileirar de uma fila vazia")
        return self.itens.pop(0)
    
    def frente(self):
        if self.esta_vazia():
            raise Exception("A fila está vazia")
        return self.itens[0]
    
    def tamanho(self):
        return len(self.itens)
```

Esta implementação utilizando uma lista é simples, mas a operação `pop(0)` tem complexidade O(n) porque requer o deslocamento de todos os elementos. Para uma implementação mais eficiente, pode-se usar uma lista encadeada ou o módulo `collections.deque` do Python, que oferece operações O(1) em ambas as extremidades.