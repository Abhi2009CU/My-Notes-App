import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import os

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")
root.configure(bg="#2f3136")

def files(name,words):
    if name:
        if words is None:
            words = " "
        else:
            pass
        with open(f"notes/{name}.txt", "w") as file:
            file.write(words)
    else:
        return [file for file in os.listdir("notes") if file.endswith(".txt")]

def homepage():
    tk.Button(root, text="+", width=10, font=("Arial", 15), command=lambda:open_note(True,False), background="skyblue", foreground="white").pack(side="top", anchor="e", padx=5, pady=5)
    for i in files(None,None):
        note_name = os.path.splitext(i)[0] 
        tk.Button(root, text=note_name, width=10, font=("Arial",15), command=lambda n=note_name:open_note(False, n), background="grey", foreground="white").pack(side="top", anchor="w", padx=5, pady=5)
    #Has a button for deleting note
    

def open_note(newNote, note_name):
    if newNote:
        note_name = simpledialog.askstring("Note Name","Name of Note: ")
        files(note_name,None)
    if note_name:
        new_note = tk.Toplevel()
        new_note.configure(bg="#2f3136")
        new_note.title(note_name)
        new_note.geometry("450x520")
        
        new_note_text = tk.Text(new_note, width=40, height=20, font=("Arial", 15), bg="#2f3136", fg="white")
        new_note_text.insert("1.0", open(f"notes/{note_name}.txt", "r").read())
        new_note_text.pack(side="top", anchor="center", padx=5, pady=5)
        
        tk.Button(new_note, width=40,height=1,text="Save", command=lambda:save(note_name,new_note_text), bg="skyblue",fg="black").pack()
        
        new_note.mainloop()
    else:
        messagebox.showinfo("Error", "Title Invalid\nCancelling Note")
    
def save(note_name,note_text):
    note_text = note_text.get("1.0", tk.END).strip()
    files(note_name,note_text)

def delete_note():
    pass
    #Deletes the note from the files
homepage()
root.mainloop()