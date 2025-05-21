# Sistema de Cadastro e Avaliação de Alunos

Este é um programa simples em Python que permite cadastrar até três alunos, calcular suas médias e classificar seu desempenho com base em suas notas.

## Funcionalidades

O programa solicita informações e notas de até **3 alunos**, e realiza as seguintes tarefas:

- Valida o e-mail de cada aluno.
- Recebe 3 notas por aluno.
- Calcula a média das notas.
- Classifica o desempenho de acordo com a média.

### Classificação de Desempenho

| Média       | Status        |
|-------------|----------------|
| 9.0 a 10.0  | Excelente      |
| 7.0 a 8.9   | Bom            |
| 5.0 a 6.9   | Regular        |
| Abaixo de 5 | Insuficiente   |

## Exemplo de uso

```bash
$ python avaliacao_alunos.py
Nome do aluno: Ana
E-mail: ana@example.com
Nota 1: 8
Nota 2: 9
Nota 3: 10

Nome do aluno: Beto
E-mail: beto[sem_arroba]gmail.com
E-mail inválido. Ignorando aluno.

Nome do aluno: Carlos
E-mail: carlos@example.com
Nota 1: 6
Nota 2: 5
Nota 3: 7

Análise de desempenho:
Ana - Média: 9.0 - Status: Excelente
Carlos - Média: 6.0 - Status: Regular
