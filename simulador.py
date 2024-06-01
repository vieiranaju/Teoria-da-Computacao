import json
import csv
import time

def lerJson(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def lerCsv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        return [row for row in reader]

def simular(automato, input_string):
    estados_ativos = {automato['initial']}
    for read in input_string:
        novos_estados_ativos = set()
        for estado in estados_ativos:
            for transition in automato['transitions']:
                if transition['from'] == estado and transition['read'] == read:
                    novos_estados_ativos.add(transition['to'])
        if not novos_estados_ativos:
            return 0  
        estados_ativos = novos_estados_ativos
    return 1 if any(state in automato['final'] for state in estados_ativos) else 0

def main():
    automatos = ['Exemplos/ex1.json', 'Exemplos/ex2.json', 'Exemplos/ex3.json']
    entradas = ['Exemplos/ex1_input.csv', 'Exemplos/ex2_input.csv', 'Exemplos/ex3_input.csv']
    
    for aut_file, input_file in zip(automatos, entradas):
        print(f"{aut_file} e {input_file}")
        aut = lerJson(aut_file)
        entradas = lerCsv(input_file)

        start_time = time.time()

        for row in entradas:
            input_string = row[0]
            expected = int(row[1])
            aceita = simular(aut, input_string)
            print(f"Entrada: {input_string} - Aceita: {aceita} - Esperada: {expected}")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tempo de execução: {elapsed_time:.4f} segundos\n")

if __name__ == "__main__":
    main()
