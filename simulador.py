import json
import csv
import time
import sys

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

def main(aut_file, input_file, output_file):
    print(f"{aut_file} e {input_file}")
    aut = lerJson(aut_file)
    entradas = lerCsv(input_file)
    if not entradas:
        return

    try:
        with open(output_file, 'w', newline='') as arquivo_saida:
            writer = csv.writer(arquivo_saida, delimiter=';')
            for row in entradas:
                input_string = row[0]
                expected = int(row[1])
                start_time = time.time()
                aceita = simular(aut, input_string)
                end_time = time.time()
                elapsed_time = end_time - start_time

                writer.writerow([input_string, expected, aceita, f"{elapsed_time:.6f}"])
                print(f"Entrada: {input_string} - Aceita: {aceita} - Esperada: {expected} - Tempo: {elapsed_time:.6f} segundos")
    except Exception as e:
        print(f"Erro ao escrever no arquivo de saída {output_file}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python simulador.py <arquivo_do_automato.aut> <arquivo_de_testes.in> <arquivo_de_saida.out>")
        sys.exit(1)
    
    aut_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    main(aut_file, input_file, output_file)