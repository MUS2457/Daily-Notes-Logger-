def save_note(note_s):
    with open("notes.txt", "a") as f:
        f.write(note_s + "\n")

def read_all_notes():
    try:
        with open("notes.txt", "r") as f:
            content = f.read()
            notes = [line for line in content.split("\n") if line.strip() != ""]
            return notes
    except FileNotFoundError:
        return []  

