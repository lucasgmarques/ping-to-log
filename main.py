import os
import datetime

# Constante para o formato da data
FORMATO_DATA = "%Y-%m-%d_%H-%M-%S"

def formata_log():
    """
    Retorna o nome do arquivo de log formatado com a data atual.
    """
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime(FORMATO_DATA)
    log_name = f"log_{formatted_date}.txt"
    return log_name

def verifica_disponibilidade_site(site, count=2):
    """
    Verifica a disponibilidade de um site usando o comando 'ping' via os.system().
    Retorna o resultado.
    """
    try:
        # Executa o comando ping via os.system()
        execute_ping = f"ping -c {count} {site}"
        result = os.system(execute_ping)

        # Verifica o código de retorno para determinar o result
        if result == 0:
            return f"O site {site} está disponível."
        
        return f"O site {site} não está disponível."

    except Exception as e:
        return f"Erro ao verificar {site}: {str(e)}"

def cria_log(log_file, content):
    """
    Cria um arquivo de log com o conteúdo fornecido.
    """
    try:
        print(f"Salvando em {log_file}...")
        with open(log_file, "w") as file:
            file.write(content)
    except Exception as e:
        print(f"Erro ao escrever o arquivo de log: {e}")

def main():
    # Solicita ao usuário que insira os sites separados por espaços
    sites = input("Digite os sites que deseja verificar (separados por vírgula): ").split(",")

    results = {}

    for site in sites:
        result = verifica_disponibilidade_site(site.strip())
        results[site] = result

    log_file = formata_log()

    # Cria o conteúdo do arquivo de log com os results
    content = ""
    for site, result in results.items():
        content += f"Site: {site}\n{result}\n\n"

    cria_log(log_file, content)
    print(f"Verificação de disponibilidade concluída. results no arquivo '{log_file}'.")

if __name__ == '__main__':
    main()
