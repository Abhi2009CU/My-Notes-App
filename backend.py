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


# def get_all_data(filename):
#         conn = sqlite3.connect('Notes.db')
#         c = conn.cursor()
#         c.execute("SELECT filename FROM Notes WHERE filename = ?", (filename,))
#         print(c.fetchall())
#         c.execute("SELECT text FROM Notes WHERE filename = ?", (filename,))
#         print(c.fetchall())
#         conn.commit()
#         conn.close()
        
#get filename and text, without any parameters
def get_filename():
        conn = sqlite3.connect('Notes.db')
        c = conn.cursor()
        c.execute("SELECT filename FROM Notes")
        filename = c.fetchall()
        conn.commit()
        conn.close()
        return filename
