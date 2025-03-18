# Estruturas de Dados

Este repositório contém exemplos práticos e explicações sobre estruturas de dados fundamentais para o curso de Ciência da Computação.

## Problema Prático

### Verificador de Expressões Balanceadas

O problema escolhido para aplicação prática é a verificação de expressões matemáticas ou de programação quanto ao balanceamento de parênteses, colchetes e chaves.

Este é um problema clássico que pode ser resolvido eficientemente usando uma estrutura de dados do tipo pilha. A ideia é percorrer a expressão caractere por caractere:

- Quando encontramos um caractere de abertura (`(`, `[`, `{`), empilhamos ele.
- Quando encontramos um caractere de fechamento (`)`, `]`, `}`), desempilhamos o último caractere de abertura e verificamos se eles formam um par válido.
- Se em algum momento tentarmos desempilhar de uma pilha vazia, ou se ao final do processamento a pilha não estiver vazia, a expressão não está balanceada.

Esse problema demonstra perfeitamente o princípio LIFO (Last In, First Out) das pilhas, onde o último parêntese aberto deve ser o primeiro a ser fechado.

O código para resolver este problema está disponível no arquivo `verificador_expressoes.py`.

## Estrutura do Repositório

- **Introdução**: Conceitos básicos de estruturas de dados
- **Definição-Importância**: Como as estruturas de dados impactam o desempenho
- **Conceitos-Fundamentais**: Variáveis, tipos e alocação de memória
- **Estruturas-Lineares**: Implementações de listas, filas e pilhas
- **verificador_expressoes.py**: Aplicação prática usando pilhas