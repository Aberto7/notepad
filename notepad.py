import tkinter as tk
from tkinter import messagebox

def save_note():
    note = text.get("1.0", tk.END)
    with open("notes.txt", "w") as file:
        file.write(note)
    messagebox.showinfo("Note Saved", "Your note has been saved successfully.")

def clear_note():
    text.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Notepad")

# Create text area for note
text = tk.Text(root, height=20, width=50)
text.pack()

# Create buttons for save and clear
save_button = tk.Button(root, text="Save Note", command=save_note)
save_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear Note", command=clear_note)
clear_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Load existing note if available
try:
    with open("notes.txt", "r") as file:
        note = file.read()
        text.insert(tk.END, note)
except FileNotFoundError:
    pass

# Start the Tkinter event loop
if __name__ == "__main__":
    root.mainloop()
