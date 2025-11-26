Daily Notes Logger 📝

A simple Python CLI app to save and view notes with timestamps. Fully modular, using logic.py and storage.py.

Features

Add notes with automatic timestamp

View all saved notes

Modular design (separate logic & storage)

Persistent storage in notes.txt

Requirements

Python 3.x

How to Run

Open terminal / command prompt

Navigate to project folder

Run:

python main.py


Follow the on-screen menu:

Add → write a new note

View → see all notes

Exit → quit program

Project Structure
main.py       # CLI menu
logic.py      # add_note() & view_notes()
storage.py    # save_note() & read_all_notes()
notes.txt     # stores all notes
