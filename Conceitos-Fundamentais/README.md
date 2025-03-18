# Conceitos Fundamentais: Variáveis, Tipos de Dados e Alocação de Memória

## Variáveis e Tipos de Dados

### Variáveis

Variáveis são nomes simbólicos que referem-se a um valor armazenado na memória do computador. Elas permitem:  
- Armazenar e manipular dados
- Reutilizar valores em diferentes partes do código
- Tornar o código mais legível e manutenível

Em linguagens de programação, as variáveis podem ser declaradas de diferentes formas, dependendo da linguagem:

```python
# Python
nome = "João"  # Tipagem dinâmica
```

```java
// Java
String nome = "João";  // Tipagem estática
```

### Tipos de Dados

Tipos de dados definem a natureza dos dados que podem ser armazenados em uma variável e as operações que podem ser realizadas sobre esses dados. Os tipos de dados comuns incluem:

1. **Tipos Primitivos**:
   - Inteiros (`int`): 1, 42, -10
   - Números de ponto flutuante (`float`): 3.14, -0.001
   - Caracteres (`char`): 'a', 'Z', '9'
   - Booleanos (`bool`): true, false

2. **Tipos Compostos**:
   - Strings: "Olá, mundo"
   - Arrays/Listas: [1, 2, 3, 4]
   - Objetos/Estruturas: { nome: "João", idade: 25 }

## Relação com Alocação de Memória

Quando declaramos variáveis, o sistema operacional aloca espaço na memória para armazenar seus valores. O tamanho do espaço alocado depende do tipo de dado:

| Tipo de Dado | Tamanho Típico | Exemplo |
|--------------|----------------|----------|
| Boolean | 1 byte | true, false |
| Char | 1-2 bytes | 'a', '1' |
| Integer | 4 bytes | 42, -500 |
| Float | 4 bytes | 3.14, -0.01 |
| Double | 8 bytes | 3.141592653589793 |
| Referência/Ponteiro | 4-8 bytes | Endereço de memória |

A relação entre variáveis, tipos de dados e alocação de memória é fundamental para entender:
- Como os dados são representados internamente
- Como otimizar o uso de memória
- Como funcionam estruturas de dados mais complexas