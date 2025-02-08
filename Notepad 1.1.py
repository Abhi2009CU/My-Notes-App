#imports
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import os
import time

#initializing root
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")
root.configure(bg="#2f3136")
# root.resizable(False, False)

#functions
    
def files(name,words):
    if name:
        if words is None:
            words = " "
        with open(f"notes/{name}.txt", "w") as file:
            file.write(words)
    else:
        return [file for file in os.listdir("notes") if file.endswith(".txt")]


def homepage():
    for widget in root.winfo_children():
        widget.destroy()
    operation_frame = tk.Frame(root, bg="#2f3136")
    operation_frame.pack(fill="x", expand=False, padx=5, pady=5)
    
    tk.Button(operation_frame, text="Delete", width=10, font=("Arial", 15), command=lambda: delete_note(None,delete=False), background="red", foreground="black").pack(side="right", padx=5, pady=5)
    tk.Button(operation_frame, text="+", width=10, font=("Arial", 15), command=lambda: open_note(True, False), background="skyblue", foreground="white").pack(side="left", padx=5, pady=5)
    
    notes_frame = tk.Frame(root, bg="#2f3136")
    notes_frame.pack(fill="both", expand=False, padx=5, pady=5)
    
    row = 0
    column = 0
    button_width = 100
    
    max_columns = 4
    for i in files(None, None):
        note_name = os.path.splitext(i)[0]
        note_button = tk.Button(notes_frame, text=note_name, width=10, font=("Arial", 15), command=lambda n=note_name: open_note(False, n), background="grey", foreground="white")
        note_button.grid(row=row, column=column, padx=5, pady=5)
        column += 1
        if column >= max_columns:
            column = 0
            row += 1


def open_note(newNote, note_name):
    if newNote:
        note_name = simpledialog.askstring("Note Name","Name of Note: ")
        if os.path.exists(f"notes/{note_name}.txt"):
            messagebox.showinfo("Error", "Note already exists\nCancelling Note")
            homepage()
        elif os.path.exists(f"notes/{note_name}.txt") == False:
            files(note_name,None)
        homepage()
    
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


def delete_note(note_name, delete: bool):
    inOld = False
    if delete:
        if messagebox.askyesno("Delete Note", f"Are you sure you want to delete {note_name}?\n REALLY THINK ABOUT THIS, YOU CAN'T UNDO IT!!!"):
            os.remove(f"notes/{note_name}.txt")
            if inOld:
                for widget in note_name.winfo_children():
                    widget.destroy()
            homepage()  # Refresh the homepage to update the list of notes
    if not delete:
        inOld = True
        for widget in root.winfo_children():
            widget.destroy()
            
        notes_frame = tk.Frame(root, bg="#2f3136")
        notes_frame.pack(fill="both", expand=True, padx=5, pady=5)
                
        row = 0
        column = 0
        button_width = 90
        max_columns = 4
        
        for i in files(None, None):
            note_name = os.path.splitext(i)[0]
            note_button = tk.Button(notes_frame, text=note_name, width=10, font=("Arial", 15), command=lambda n=note_name: delete_note(n,True), background="Red", foreground="white")
            note_button.grid(row=row, column=column, padx=5, pady=5)
            column += 1
            if column >= max_columns:
                column = 0
                row += 1
        
homepage()
root.mainloop()