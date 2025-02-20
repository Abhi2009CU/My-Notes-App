#imports
import sqlite3
import os


#checks if database exists, if not creates it
if not os.path.exists('Notes.db'):
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE Notes
                (filename TEXT, text TEXT)''')
        conn.commit()
        conn.close()
        
if not os.path.exists('Settings.db'):
        conn = sqlite3.connect('Settings.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE Settings
                (setting TEXT, value TEXT)''')
        conn.commit()
        c.execute("INSERT INTO Settings (setting, value) VALUES (?, ?)", ("bg_color", "#2f3136"))
        conn.commit()
        conn.close()

#Creates new filename with text
def create_file(filename, text):
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute("INSERT INTO Notes (filename, text) VALUES (?, ?)", (filename, text))
        conn.commit()
        conn.close()

#Gets the text from the specified filename
def get_file_content(filename):
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute("SELECT text FROM Notes WHERE filename = ?", (filename,))
        text = c.fetchall()
        conn.commit()
        conn.close()
        return text

#Updates the text from the specified filename
def update_file(filename, text):
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute("UPDATE Notes SET text = ? WHERE filename = ?", (text, filename))
        conn.commit()
        conn.close()
        
def change_filename(old_filename, new_filename):
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute("UPDATE Notes SET filename = ? WHERE filename = ?", (new_filename, old_filename))
        conn.commit()
        conn.close()

#Deletes the specified filename
def delete_file(filename):
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute("DELETE FROM Notes WHERE filename = ?", (filename,))
        conn.commit()
        conn.close()

#Deletes all data from the database
def delete_ALL():
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute("DROP TABLE Notes")
        conn.commit()
        conn.close()

# Get all data from the database
def get_all_data():
        print('Function build in progress..')
        # conn = sqlite3.connect('Notes.db')
        # c = conn.cursor()
        # c.execute("SELECT * FROM Notes")
        # print(c.fetchall())
        # conn.commit()
        # conn.close()
        
#get filename and text, without any parameters
def get_filename():
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute("SELECT filename FROM Notes")
        filename = c.fetchall()
        conn.commit()
        conn.close()
        return filename



#Updates the text from the specified setting
def bg_color(bg_color, get):
        conn = sqlite3.connect('Settings.db')
        c = conn.cursor()
        if get:
                c.execute("SELECT value FROM Settings WHERE setting = ?", ('bg_color',))
                bg_color = c.fetchone()  # Use fetchone() to get a single result
                conn.close()
                return bg_color[0] if bg_color else None
        else:
                c.execute("UPDATE Settings SET value = ? WHERE setting = ?", (bg_color, "bg_color"))
                conn.commit()
                conn.close()