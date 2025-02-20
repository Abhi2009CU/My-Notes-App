
#imports
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, colorchooser
import time
import backend as db

#initializing root
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")
bg_color = db.bg_color(None, True)
if bg_color:
    root.configure(bg=db.bg_color(None, True))
# root.resizable(False, False)

#functions

def homepage():
    for widget in root.winfo_children():
        widget.destroy()
    operation_frame = tk.Frame(root, bg=db.bg_color(None, True))
    operation_frame.pack(fill="x", expand=False, padx=5, pady=5)
    
    
    settings_img = tk.PhotoImage(file="images/settings.png")
    settings_img = settings_img.subsample(5)
    setting_button =tk.Button(operation_frame, image=settings_img, command=lambda: settings(operation_frame), background=db.bg_color(None, True), foreground=db.bg_color(None, True), borderwidth=0, activebackground=db.bg_color(None, True))
    setting_button.image = settings_img
    setting_button.pack(padx=10, pady=10, side="left")
    
    home = tk.PhotoImage(file="images/Home.png")
    home = home.subsample(15)
    home_button =tk.Button(operation_frame, image=home, command=lambda: homepage(), background=db.bg_color(None, True), foreground=db.bg_color(None, True), borderwidth=0, activebackground=db.bg_color(None, True))
    home_button.image = home
    home_button.pack(padx=10, pady=10, side="left")
    
    add = tk.PhotoImage(file="images/add.png")
    add = add.subsample(5)
    add_button =tk.Button(operation_frame, image=add, command=lambda: open_note(True, None), background=db.bg_color(None, True), foreground=db.bg_color(None, True), borderwidth=0, activebackground=db.bg_color(None, True))
    add_button.image = add
    add_button.pack(padx=10, pady=10, side="left")
    
    delete = tk.PhotoImage(file="images/delete.png")
    delete = delete.subsample(5)
    delete_button = tk.Button(operation_frame, image=delete, command=lambda: delete_note(None,delete=False), background=db.bg_color(None, True), foreground=db.bg_color(None, True), borderwidth=0, activebackground=db.bg_color(None, True))
    delete_button.image = delete
    delete_button.pack(padx=10, pady=10, side="right")
    
    notes_frame = tk.Frame(root, bg=db.bg_color(None, True))
    notes_frame.pack(fill="both", expand=False, padx=5, pady=5)
    
    row = 0
    column = 0
    files = [item[0] for item in db.get_filename()]

    for note_name in files:
        note_button = tk.Button(notes_frame, text=note_name, width=10, font=("Arial", 15), command=lambda n=note_name: open_note(False, n), background="grey", foreground="white")
        note_button.grid(row=row, column=column, padx=5, pady=5)
        column += 1
        if column >= 4:
            column = 0
            row += 1

def color_change():
    bg_color = colorchooser.askcolor()
    if bg_color[1]:
        db.bg_color(bg_color[1], False)
        root.configure(bg=db.bg_color(None, True))
    homepage()
    
def settings(operation_frame):
    setting = tk.Toplevel()
    setting.configure(bg=db.bg_color(None, True))
    setting.title("Settings")
    setting.geometry("450x520")
    
    tk.Label(setting, text="Settings", font=("Arial", 20), bg=db.bg_color(None, True), fg="white").pack(pady=10)
    
    tk.Button(setting, text="Background Color", width=20, font=("Arial", 15), command=lambda: color_change(), background="red", foreground="black").pack(pady=10)
    
    setting.mainloop()
def open_note(newNote, note_name):
    if newNote:
        note_name = simpledialog.askstring("Note Name","Name of Note: ")
        clear = True
        if db.get_file_content(note_name):
            messagebox.showinfo("Error", "Note Already Exists")
            homepage()
            clear = False
        if note_name is None:
            homepage()
        if note_name and clear == True:  
            db.create_file(note_name, "")
        homepage()
        
    if note_name:
        new_note = tk.Toplevel()
        new_note.configure(bg=db.bg_color(None, True))
        new_note.title(note_name)
        new_note.geometry("450x520")
        
        new_note_text = tk.Text(new_note, width=40, height=20, font=("Arial", 15), bg=db.bg_color(None, True), fg="white")
        if db.get_file_content(note_name):
            new_note_text.insert("1.0", db.get_file_content(note_name)[0][0])
        if db.get_file_content(note_name) == []:
            new_note_text.insert("1.0", "")
        new_note_text.pack(side="top", anchor="center", padx=5, pady=5)
        
        tk.Button(new_note, width=40,height=1,text="Save", command=lambda:save(note_name,new_note_text), bg="skyblue",fg="black").pack()
        new_note.mainloop()
    else:
        messagebox.showinfo("Error", "Something definitely went wrong! Try doing something else lol :)")


def save(note_name,note_text):
    note_text = note_text.get("1.0", tk.END).strip()
    db.update_file(note_name, note_text)


def delete_note(note_name, delete: bool):
    
    inOld = False
    if delete:
        if messagebox.askyesno("Delete Note", f"Are you sure you want to delete {note_name}?\n REALLY THINK ABOUT THIS, YOU CAN'T UNDO IT!!!"):
            db.delete_file(note_name)
            if inOld:
                for widget in note_name.winfo_children():
                    widget.destroy()
        homepage() 
    if not delete:
        inOld = True
        for widget in root.winfo_children():
            widget.destroy()
            
        operation_frame = tk.Frame(root, bg=db.bg_color(None, True))
        operation_frame.pack(fill="x", expand=False, padx=5, pady=5)
        home = tk.PhotoImage(file="images/Home.png")
        home = home.subsample(15)
        home_button =tk.Button(operation_frame, image=home, command=lambda: homepage( ), background=db.bg_color(None, True), foreground=db.bg_color(None, True), borderwidth=0, activebackground=db.bg_color(None, True))
        home_button.image = home
        home_button.pack(padx=10, pady=10, side="left", anchor="nw")
        
        
        notes_frame = tk.Frame(root, bg=db.bg_color(None, True))
        notes_frame.pack(fill="both", expand=True, padx=5, pady=5)
    
        row = 0
        column = 0
        files = [item[0] for item in db.get_filename()]

        for note_name in files:
            note_button = tk.Button(notes_frame, text=note_name, width=10, font=("Arial", 15), command=lambda n=note_name: delete_note(n,True), background="Red", foreground="white")
            note_button.grid(row=row, column=column, padx=5, pady=5)
            column += 1
            if column >= 4:
                column = 0
                row += 1

homepage()

root.mainloop()