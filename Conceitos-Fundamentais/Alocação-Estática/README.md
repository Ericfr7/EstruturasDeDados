# Alocação de Memória Estática

## O que é Alocação Estática?

A alocação estática de memória ocorre quando o espaço de memória para variáveis é alocado durante a compilação do programa, e o tamanho permanece fixo durante toda a execução. Isso significa que o compilador determina exatamente quanto espaço será necessário e onde esse espaço será alocado antes mesmo do programa começar a executar.

## Características da Alocação Estática

1. **Tempo de alocação**: Ocorre durante a compilação ou no início da execução do programa

2. **Duração**: A memória permanece alocada durante toda a vida útil do programa ou escopo da variável

3. **Localização na memória**: Geralmente na área de dados estáticos ou na pilha (stack)

4. **Tamanho fixo**: O tamanho da memória alocada não pode ser alterado durante a execução

5. **Desalocação automática**: A memória é liberada automaticamente quando o escopo da variável termina (para variáveis locais) ou quando o programa finaliza (para variáveis globais)

## Exemplos Comuns de Alocação Estática

- Variáveis locais em funções
- Arrays de tamanho fixo declarados em tempo de compilação
- Variáveis globais
- Variáveis estáticas

## Vantagens

- Acesso rápido aos dados (endereços conhecidos em tempo de compilação)
- Não há sobrecarga de gerenciamento de memória em tempo de execução
- Menor probabilidade de vazamento de memória (memory leaks)
- Previsibilidade no uso de recursos

## Desvantagens

- Inflexibilidade: tamanho fixo ao longo da execução
- Possível desperdício de memória (quando se aloca mais do que o necessário)
- Limitações para estruturas que precisam crescer ou diminuir dinamicamente
- Problemas com recursão profunda (pode causar estouro de pilha)

## Casos de Uso Ideais

- Dados de tamanho fixo e conhecido
- Sistemas embarcados com recursos limitados
- Aplicações críticas onde previsibilidade é essencial
- Estruturas de tamanho pequeno e constante