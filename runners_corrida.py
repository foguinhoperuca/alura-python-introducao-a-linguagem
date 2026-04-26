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
