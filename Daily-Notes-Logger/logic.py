import storage
from datetime import datetime

def add_note():
    while True:
        user = input("Your text: ").strip()  # keep original text
        
        if user == "":
            print("Text cannot be empty, try again!")
            continue
        else:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_note = f"[{now}] {user}"
            storage.save_note(new_note)  
            print("Note saved!")
            break

def view_notes():
    notes = storage.read_all_notes()  # get all notes as a list
    
    if not notes:  # empty list
        print("No notes yet.")
    else:
        print("\n--- Your Notes ---")
        for note in notes:
            print(note)
        print("-" * 20 + "\n")
