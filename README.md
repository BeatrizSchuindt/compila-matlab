# Compilador Mini-MATLAB (2025/2)

## 🎯 Objetivo Geral

Desenvolver um **compilador funcional**, baseado em uma **gramática ANTLR**, capaz de realizar **análise léxica e sintática** de programas simples inspirados na linguagem **MATLAB**.  

O compilador lê arquivos `.m`, identifica tokens, valida a estrutura sintática e gera automaticamente uma **árvore sintática (AST)** em formato de imagem.

---

## 🧩 Estrutura do Projeto

```
COMPILA-MATLAB/
│
├── exemplos/                → Programas de teste (.m)
│   ├── erro_lexico.m        → Teste de erro léxico
│   ├── erro_sintatico.m     → Teste de erro sintático
│   ├── ok.m                 → Programa simples válido
│   ├── pascal.m             → Caso de teste 1: Triângulo de Pascal
│   ├── triangulos_ok.m      → Caso de teste 2: Classificação de Triângulos
│   └── *.tree.png / *.svg   → Árvores sintáticas geradas automaticamente
│
├── grammar/
│   └── matlab.g4            → Gramática principal ANTLR (Mini-MATLAB)
│
├── src/
│   ├── ast_graphviz.py      → Renderiza a árvore sintática (AST)
│   ├── error.py             → Trata erros léxicos e sintáticos
│   ├── main.py              → Ponto de entrada do compilador
│   └── gen/grammar/         → Código Python gerado pelo ANTLR
│
├── antlr-4.13.2-complete.jar → Ferramenta ANTLR usada para gerar lexer/parser
├── Proposta do trabalho - Compilador.pdf → Especificação do professor
└── README.md                → Documentação e guia de apresentação
```

---

## 🧱 1. Especificação da Gramática (Mini-MATLAB)

A gramática define uma linguagem simplificada inspirada no MATLAB, contendo:

### Tipos de Dados
- `int` — números inteiros  
- `real` — números decimais  

### Entrada/Saída
```matlab
a = input('Digite um valor: ');
disp(a);
```

### Estruturas de Controle
**Condicional:**
```matlab
if a > 0
    disp('Valor positivo');
elseif a == 0
    disp('Valor neutro');
else
    disp('Valor negativo');
end
```

**Repetição:**
```matlab
n = 1;
while n <= 5
    disp(['Contador: ', num2str(n)]);
    n = n + 1;
end
```

### Expressões
- **Aritméticas:** `+, -, *, /, ()`
- **Lógicas:** `&&, ||, !, ==, !=, >, <, >=, <=`

A gramática foi construída no formato **LL(1)**, sem recursão à esquerda, e com **fatoração aplicada** para evitar ambiguidades.

---

## 🧾 2. Analisador Léxico

**Objetivo:** Identificar os tokens válidos e rejeitar símbolos não reconhecidos.  
**Mensagens de erro:**
```
ERRO LÉXICO [linha 5, col 12]: Símbolo '#' inválido.
```

---

## 🧮 3. Analisador Sintático

**Objetivo:** Verificar se o programa segue a estrutura definida na gramática.  
**Mensagens de erro:**
```
ERRO SINTÁTICO [linha 8, col 3] token='}': Esperado ';' antes de '}'.
```

---

## 🌳 4. Visualização da AST

A árvore sintática é gerada automaticamente em:
- `PNG` → Para visualização no relatório  
- `SVG` → Para inspeção vetorial

Os **tokens terminais** aparecem em **azul claro**, e as **regras da gramática** em **cinza claro**.

---

## 🧰 5. Execução do Compilador

### 💻 Comando
```bash
python -m src.main exemplos/triangulos_ok.m
```

### ✅ Saída esperada
```
OK: gerei exemplos/triangulos_ok.tree.png
OK: gerei exemplos/triangulos_ok.tree.svg
```

---
## 🧪 6. Casos de Teste

### 🧮 6.1 Triângulo de Pascal
**Objetivo:** validar a estrutura de repetição `while` e o uso de laços aninhados.  
**Arquivo:** `exemplos/pascal.m`

```matlab
n = input('Digite o número de linhas: ');

if n > 0
    for linha = 1:n
        valor = 1;
        for coluna = 1:linha
            fprintf('%d ', valor);
            valor = valor * (linha - coluna) / coluna;
        end
        fprintf('\n');
    end
else
    disp('Valor inválido!');
end
```

🧩 **Valida:**
- Estruturas `for` e `if`  
- Operações aritméticas e de comparação  
- Controle de fluxo e formatação de saída  

---

### 🔺 6.2 Classificação de Triângulos
**Objetivo:** testar expressões lógicas e condicionais aninhadas.  
**Arquivo:** `exemplos/triangulos_ok.m`

```matlab
a = input('Digite o valor do lado A: ');
b = input('Digite o valor do lado B: ');
c = input('Digite o valor do lado C: ');

if (a < b + c && b < a + c && c < a + b)
    if (a == b && b == c)
        disp('Triângulo equilátero');
    elseif (a == b || b == c || a == c)
        disp('Triângulo isósceles');
    else
        disp('Triângulo escaleno');
    end
else
    disp('Medidas inválidas');
end
```

🧩 **Valida:**
- Operadores lógicos `&&` e `||`  
- Estruturas condicionais aninhadas (`if`, `elseif`, `else`)  
- Avaliação de múltiplas condições em MATLAB  

---

## ⚙️ 7. Tratamento de Erros

| Tipo de Erro | Exemplo no MATLAB | Mensagem exibida |
|---------------|-------------------|------------------|
| Léxico | `#` | `ERRO LÉXICO [linha 3, col 5]: Símbolo '#' inválido.` |
| Sintático | `{` | `ERRO SINTÁTICO [linha 2, col 7] token='{': Esperado expressão.` |


## 🧩 8. Conclusões

O compilador **Mini-MATLAB** implementa corretamente as fases de **análise léxica e sintática**, exibindo **erros detalhados** e **árvores sintáticas automáticas** para facilitar o entendimento do processo de compilação.

**Aprendizados:**
- Estruturação de gramáticas **LL(1)** no ANTLR  
- Integração entre lexer, parser e renderização de AST  
- Visualização da sintaxe com **Graphviz**  
- Desenvolvimento modular e documentação clara

**Próximos passos:**
- Implementar **análise semântica** (verificação de tipos e variáveis)  
- Gerar **código intermediário**  
- Criar um **interpretador simples** para os programas `.m`

---

## 🧩 09. Comandos úteis

```bash
# Gerar o lexer e parser com ANTLR
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/gen/grammar grammar/matlab.g4

# Executar o compilador em um exemplo
python -m src.main exemplos/pascal.m
```
