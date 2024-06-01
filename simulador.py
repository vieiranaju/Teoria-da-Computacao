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
    #Retorna uma lista com as palavras 

def simular(automato, input_string):
    estados_ativos = {automato['initial']}

    #Para cada simbolo lido cria um conjunto de estados ativos
    for read in input_string:
        novos_estados_ativos = set()

        #Verifica as possiveis transições
        for estado in estados_ativos:
            for transition in automato['transitions']:
                if transition['from'] == estado and transition['read'] == read:
                    novos_estados_ativos.add(transition['to'])
                    #Adiciona o novo estado no conjunto caso seja possivel atualizar

        if not novos_estados_ativos:
            return 0  
        estados_ativos = novos_estados_ativos
        #Novos estados passam a ser o estado atual pro proximo simbolo

    return 1 if any(state in automato['final'] for state in estados_ativos) else 0
    #No final da leitura, se algum estado na lista de estados atuais for final retorna 0

def main():
    automatos = ['Exemplos/ex1.json', 'Exemplos/ex2.json', 'Exemplos/ex3.json']
    entradas = ['Exemplos/ex1_input.csv', 'Exemplos/ex2_input.csv', 'Exemplos/ex3_input.csv']
    
    for aut_file, input_file in zip(automatos, entradas):
        print(f"{aut_file} e {input_file}")
        aut = lerJson(aut_file)
        entradas = lerCsv(input_file)
        #Lê cada um dos arquivos e entradas

        start_time = time.time()

        for row in entradas:
            input_string = row[0]
            expected = int(row[1])
            aceita = simular(aut, input_string)
            print(f"Entrada: {input_string} - Aceita: {aceita} - Esperada: {expected}")
            #Verifica cada elemento da lista de palavras e simula o automato correspondente

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Tempo de execução: {elapsed_time:.4f} segundos\n")

if __name__ == "__main__":
    main()
