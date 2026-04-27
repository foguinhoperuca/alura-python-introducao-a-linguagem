"""
See .aider.chat.history.md#2026-04-26T13:47:33
Original prompt:
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.
####     Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?
####     Exemplo de Entrada: Digite o nome incorreto: Carlos Digite o nome correto: João
####     Saída esperada: O nome Carlos foi substituído por João. Lista atualizada: ['Ana', 'João', 'Pedro']
"""


def update_participant_name(participants, old_name, new_name):
    if old_name in participants:
        index = participants.index(old_name)
        participants[index] = new_name
        print(f"The name {old_name} was replaced by {new_name}.")
    else:
        print(f"{old_name} not found in the list.")

    return participants


def main():
    # Example list of participants
    participants = ['Ana', 'Carlos', 'Pedro']

    # Get input from the user
    old_name = input("Digite o nome incorreto: ")
    new_name = input("Digite o nome correto: ")

    # Update the participant name
    updated_participants = update_participant_name(participants, old_name, new_name)

    # Display the updated list
    print("Lista atualizada:", updated_participants)


if __name__ == "__main__":
    main()
