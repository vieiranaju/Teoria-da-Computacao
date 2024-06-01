import json
import csv
import time

def lerJson(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def lerCsv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        return [row[0] for row in reader]

def simular(automato, input_string):
    estadoAtual = automato['initial']
    for read in input_string:
        transitions = automato['transitions']
        for transition in transitions:
            if transition['from'] == estadoAtual and transition['read'] == read:
                estadoAtual = transition['to']
                break
        else:
            return 0  
    return 1 if estadoAtual in automato['final'] else 0  

def main():
    aut = lerJson('Exemplos/ex2.json')
    entradas = lerCsv('Exemplos/ex2_input.csv')

    start_time = time.time()

    for input_string in entradas:
        aceita = simular(aut, input_string)
        print(f"Entrada: {input_string} - Aceita: {aceita}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo de execução: {elapsed_time:.4f} segundos")

if __name__ == "__main__":
    main()
