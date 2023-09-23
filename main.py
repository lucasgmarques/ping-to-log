import os
import datetime

def executa_ping(domain, counts=1, timeout=None):
    print(f"Testando {domain} ...")
    
    response = os.popen(f"ping -c {counts} {domain} -W {timeout}").read()
    
    if f"{counts} received" in response:
        print(f"{domain} - UP")
    else:
        print(f"{domain} - DOWN")

    data_formatada = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M")

    with open("log.txt", "a+") as file:
         file.write(f"{domain:<20}    {data_formatada:>20}\n")

def le_log():
    # Ler a saída do arquivo
    with open("log.txt", "r") as file:
        log_file = file.read()

    return log_file
    
def main():
  while True:
    print("Testa conexão:")
    print("1 - Ping")
    print("2 - Exibir último log")
    print("0 - Sair")

    option = int(input("Digite uma opção: "))

    if option == 0:
        print("Saindo ...")
        break
      
    elif option == 1:
        domains = input("Digite o domínio (ou separe por vírgula se mais de um): ").split(",")

        for domain in domains:
            domain = domain.strip()    
            executa_ping(domain, timeout=2)
    
    elif option == 2:
        log = le_log()
        print("Exibindo log ...")
        print("----- PINGS REALIZADOS -----")
        print(log)
    
    else:
        print("Opção inválida. Tente novamente.")
  
# Executa o programa
if __name__ == '__main__':
  main()
