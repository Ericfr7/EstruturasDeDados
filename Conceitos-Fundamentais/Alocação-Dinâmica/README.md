# Alocação de Memória Dinâmica

## O que é Alocação Dinâmica?

A alocação dinâmica de memória ocorre durante a execução do programa, permitindo que a quantidade de memória alocada seja determinada em tempo de execução, e não durante a compilação. Isso significa que o programa pode solicitar memória conforme necessário e liberá-la quando não for mais utilizada.

## Características da Alocação Dinâmica

1. **Tempo de alocação**: Ocorre durante a execução do programa, conforme necessário

2. **Duração**: Persiste até ser explicitamente liberada (em linguagens com gerenciamento manual) ou até não haver mais referências ao objeto (em linguagens com garbage collector)

3. **Localização na memória**: Geralmente no heap (monte)

4. **Tamanho flexível**: O tamanho pode ser determinado em tempo de execução, permitindo estruturas que crescem e diminuem

5. **Desalocação**: Pode ser manual (em linguagens como C/C++) ou automática (em linguagens com garbage collector como Python, Java, C#)

## Exemplos Comuns de Alocação Dinâmica

- Listas encadeadas
- Árvores
- Grafos
- Arrays redimensionáveis (como ArrayList em Java ou List em C#)
- Objetos criados com operadores como `new` em Java/C# ou alocados com `malloc`/`calloc` em C

## Vantagens

- Flexibilidade: memória alocada conforme necessário
- Eficiência no uso de memória (aloca apenas o necessário)
- Capacidade de lidar com estruturas de dados de tamanho variável
- Possibilidade de criar estruturas complexas como listas encadeadas e árvores

## Desvantagens

- Overhead de gerenciamento de memória
- Possibilidade de vazamentos de memória (memory leaks) em linguagens com gerenciamento manual
- Fragmentação do heap
- Acesso geralmente mais lento que a memória alocada estaticamente

## Casos de Uso Ideais

- Quando o tamanho dos dados não é conhecido em tempo de compilação
- Estruturas de dados que precisam crescer ou diminuir durante a execução
- Manipulação de grandes volumes de dados
- Implementação de estruturas de dados complexas como árvores e grafos