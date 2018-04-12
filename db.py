# Import System modules

import sqlite3
import sys
import os.path 

#Importing custom modules

import classes

db_name = "info.db"
init_src = "tsumo.txt"
new_tsumo_file = "new_tsumo.txt"
keys_src = "keys"
all_tsumo = "all_tsumo.txt"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, db_name)

def create_tables():
    tsumo_lines = []
    keys_lines = [] 
    with open(init_src, "r") as f:
        tsumo_lines = f.readlines()

    with open(keys_src, "r") as f:
        keys_lines =  f.readlines()


    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    #Create the Tsumo table and poulate it with Tsumos

    c.execute('''CREATE table Tsumo 
                (ID integer primary key, tsumo text, meaning text)''')

    for line in tsumo_lines:
        c.execute('''INSERT INTO Tsumo(tsumo) values (?)''',(line[:-1],))

    #Create the keys table and populate it with Keys
    
    c.execute('''CREATE TABLE Keys
                (key text, value text)''')

    for line in keys_lines:
        if len(line) == 0:
            continue
        c.execute('''INSERT INTO Keys (key, value) values (?, ?)''', (line.split(": ")[0], line.split(": ")[1][:-1]))
        
    
    conn.commit()
    conn.close()

def get_tsumo(x):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''SELECT * FROM Tsumo WHERE ID = ?''', (x,))
    result = c.fetchone()
    conn.close()

    return classes.Tsumo(id = result[0], tsumo = result[1])

def get_tsumo_count():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT count(*) FROM Tsumo''')
    result = c.fetchone()
    return int(result[0])

def print_all_tsumo():
    
    conn =  sqlite3.connect(DB_PATH)
    c = conn.cursor()

    tsumo = []
    c.execute("""SELECT * FROM Tsumo""")
    
    with open(all_tsumo, "w") as f:
        for result in c.fetchall():
            f.write(result[1] + "\n")

    conn.close()


def new_tsumo():

    print_all_tsumo()

    new_lines = []
    new_tsumo = []
    with open(new_tsumo_file, "r") as f: 
        new_lines = f.readlines()

    for line in new_lines:
        if len(line) < 2:
            continue
        if line.find("|") == -1:
            new_tsumo.append([line[:-1], ""])
        else:
            new_tsumo.append(line[:-1].split("|"))
    
    print (new_tsumo)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    x = c.rowcount
    print(x)
    for tsumo in new_tsumo:
        c.execute('''INSERT INTO Tsumo(tsumo, meaning)
                SELECT ?, ?
                WHERE NOT EXISTS( SELECT 1
                FROM Tsumo
                WHERE tsumo ==  ?)''', (tsumo[0], tsumo[1], tsumo[0]))

    conn.commit()
    conn.close()
    y = c.rowcount
    print(y)

    if x ==y:
        print ("No new rows were added.")

    else:
        print(y-x, " rows were added.")
    
    with open(new_tsumo, "w") as f:
        f.write("")

def get_keys():
    
    keys = {}
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''SELECT key, value  FROM Keys''')
    results = c.fetchall()
    for result in results: 
        keys[result[0]] =  result[1]

    conn.commit()
    conn.close()

    return keys


def delete_table():
    print_all_tsumo()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''DROP TABLE Tsumo''')
    conn.commit()
    conn.close()

def clean_tsumo():
    print_all_tsumo()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(''' DELETE FROM Tsumo
                WHERE tsumo = ""''')

    conn.commit()
    conn.close()


# Running db methods

if __name__ == "__main__":
        
    if len(sys.argv) < 2:
        print("No option selected. Exitting.")

    elif sys.argv[1] == "create_tables":
        create_tables()

    elif sys.argv[1] ==  "new_tsumo":
        print("Adding new tsumo to the database.")
        new_tsumo()

    elif sys.argv[1] == "delete_table":
        print ("Dropping Tsumo database")
        delete_table()

    elif sys.argv[1] ==  "back_up":
        print("Back up selected. Backing up data...")
        print_all_tsumo()
    
    elif sys.argv[1] == "clean_tsumo":
        print("Cleaning blank tsumo from DB...")
        clean_tsumo()

    else:
        print("Unavailable option.")




