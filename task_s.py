def execute_task(task):
    if task == "imprimir":
        print("Esta é a tarefa de impressão.")
        return "Sucesso: A tarefa de impressão foi executada."
    elif task == "somar":
        result = 5 + 3
        print(f"O resultado da soma é {result}.")
        return "Sucesso: A tarefa de soma foi executada."
    elif task == "mostrar_data":
        from datetime import datetime
        current_date = datetime.now()
        print(f"A data e hora atuais são {current_date}.")
        return "Sucesso: A tarefa de mostrar a data foi executada."
    else:
        return "Falha: Tarefa desconhecida."

# Exemplo de uso:
task = input("Digite a tarefa a ser executada (imprimir, somar, mostrar_data): ")
result = execute_task(task)
print(result)

