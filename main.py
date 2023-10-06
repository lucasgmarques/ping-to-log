import os
import datetime
from prettytable import PrettyTable

# formato da data
FORMATO_DATA = "%y-%m-%d_%h-%m-%s"

def formata_log():
    """
    retorna o nome do arquivo de log formatado com a data atual.
    """
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime(FORMATO_DATA)
    log_name = f"log_{formatted_date}.txt"
    return log_name

def verifica_disponibilidade_site(site, count=2):
    """
    verifica a disponibilidade de um site usando o comando 'ping' via os.system().
    retorna o outputado.
    """
    try:
        # executa o comando ping
        execute_ping = f"ping -c {count} {site}"
        output = os.system(execute_ping)

        # verifica o código de retorno
        if output == 0:
            return f"O site {site} está disponível."
        return f"O site {site} não está disponível."

    except exception as e:
        return f"erro ao verificar {site}: {str(e)}"

def cria_log(log_file, output):
    """
    cria um arquivo de log com o conteúdo fornecido.
    """
    try:
        print(f"Salvando em {log_file}...")
        with open(log_file, "w") as file:
            table = PrettyTable()
            table.field_names = ['data', 'horário', 'url', 'ip', 'status']
            print(table)
            file.write(output)
    except exception as e:
        print(f"erro ao escrever o arquivo de log: {e}")

def main():
    """
    função principal que solicita ao usuário uma lista de sites
    """
    # solicita ao usuário que insira os sites separados por espaços
    sites = input("Digite os sites que deseja verificar (separados por vírgula): ").split(",")

    outputs = {}

    for site in sites:
        output = verifica_disponibilidade_site(site.strip())
        outputs[site] = output

    log_file = formata_log()

    # cria o conteúdo do arquivo de log com os outputs
    output = ""
    for site, output in outputs.items():
        output += f"site: {site}\n{output}\n\n"

    cria_log(log_file, output)
    print(f"Verificação de disponibilidade concluída. outputado no arquivo '{log_file}'.")

if __name__ == '__main__':
    main()
