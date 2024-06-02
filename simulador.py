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

def atualizar_estados(estado_atual, automato, read):
    novos_estados = set()

    for transition in automato['transitions']:
        if transition['from'] == estado_atual and transition['read'] == read:
            novos_estados.add(transition['to'])
            #Adiciona o novo estado no conjunto caso seja possivel atualizar

    return novos_estados

def atualizar_estados_nulos(estados, automato):
    novos_estados = set()

    for estado in estados:
        for transicao in automato['transitions']:
            if transicao['from'] == estado and transicao['read'] is None:
                novos_estados.add(transicao['to'])

    return novos_estados

def simular_automato(automato, entrada):
    estados_atuais = {automato['initial']}

    for read in entrada:
        novos_estados = set()

        estados_atuais.update(atualizar_estados_nulos(estados_atuais, automato))
        
        for estado in estados_atuais:
            novos_estados.update(atualizar_estados(estado, automato, read))


        if not novos_estados:
            return 0

        estados_atuais = novos_estados

    # Verifica se algum dos estados atuais é um estado final
    return 1 if any(estado in automato['final'] for estado in estados_atuais) else 0


def main(aut_file, input_file, output_file):

    aut = lerJson(aut_file)
    entradas = lerCsv(input_file)
    if not entradas:
        return

    try:
        with open(output_file, 'w', newline='') as arquivo_saida:
            writer = csv.writer(arquivo_saida, delimiter=';')

            for row in entradas:
                input = row[0]
                expected = int(row[1])
                inicio = time.time()
                aceita = simular_automato(aut, input)
                fim = time.time()
                tempo = fim - inicio

                writer.writerow([input, expected, aceita, f"{tempo:.6f}"])
                
    except Exception as e:
        print(f"Erro no arquivo de saída {output_file}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python simulador.py <arquivo_do_automato.aut> <arquivo_de_testes.in> <arquivo_de_saida.out>")
        sys.exit(1)
    
    aut_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    main(aut_file, input_file, output_file)