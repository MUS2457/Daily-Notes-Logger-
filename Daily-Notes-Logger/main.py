import logic



while True :
    user = input("Enter your text .('Add' to add notes ,or 'View' to view it or 'Exit') to quit.").capitalize().strip()

    if user == 'Add':
        logic.add_note()   # this programm was written on my work break for practice only ,but it fully works and hundle erors
    elif user == 'View':
        logic.view_notes() 
    elif user == 'Exit':
        print("Goodbye, the program is closed.")
        break
    elif user == '':
        print("The text cannot be empty.")
        continue 
    else:
        print("Invalid option, try again.")
