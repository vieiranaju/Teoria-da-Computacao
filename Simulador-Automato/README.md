<h1 align="center">Simulador de Autômatos Finitos</h1> 
<p align="center">Trabalho realizado na matéria de Teoria da Computação, de implementar um Simulador de Autômatos Finitos</p>

## 🚀 Funcionalidades
- [x] Deterministico
- [ ] Não deterministico (Funciona, mas as vezes da erro)


O código contém uma função para leitura de arquivos JSON, uma pra CSV, duas funções para verificar estados, sendo uma delas direcionada a estados vazios, uma função de simular, que verifica todas as possiveis transções para cada simbolo lido passsando pelas verificações de novos estados e adicionando a uma lista de estados atuais, caso tenham mais de um, e então retorna 1 para caso exista um estado final correspondente ao resultado, e 0 caso não. A função main recebe como parâmetro os arquivos que serão utilizadas, e faz a leitura dos mesmos, e então escreve os resultados da simulação junto ao tempo de execução no arquivo de saida. 


## 💻 Sobre o projeto

A ferramenta recebe um arquivo do tipo JSON com as especificações do automato desejado no seguinte padrão:

```
{
    "initial": 0,
    "final": [2],
    "transitions": [
      {
        "from": 0,
        "to": 0,
        "read": "a"
      },
      {
        "from": 0,
        "to": 1,
        "read": "a"
      },
      {
        "from": 1,
        "to": 2,
        "read": "b"
      },
      {
        "from": 2,
        "to": 2,
        "read": "a"
      },
      {
        "from": 2,
        "to": 2,
        "read": "b"
      }
    ]
  }
```

Junto com um arquivo CSV com as entradas, da seguinte forma:

```
aab;1
aaab;1
bbaa;0
abba;1
abab;1
aaa;0
bbb;0
```

E então o arquivo de saida, que armazena a palavra, o resultado esperado, o resultado final, ou seja, se a palavra foi aceita ou não pelo automato, e o tempo de execução:

```
aab;1;1;0.000018
aaab;1;1;0.000012
bbaa;0;0;0.000002
abba;1;1;0.000008
abab;1;1;0.000008
aaa;0;0;0.000008
bbb;0;0;0.000002
```

## ⚙️ Executando 

Para executar o programa utiliza-se o comando 
```
$ python simulador.py Exemplos/ex1.json Exemplos/ex1_input.csv Exemplos/ex1_output.out.csv
```

E é necessario que contenha o nome dos três arquivos a serem utilizados para funcionar
