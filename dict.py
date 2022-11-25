import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="postgres",
   password="XXXXX"
)
#comment comment comment
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionary2;")
    cur.execute("COMMIT;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows#comment comment comment
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary2 (word, translation) VALUES ('{word}', '{translation}');")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary2 WHERE id = '{ID}';")
    cur.execute("COMMIT;")
    cur.close()
    conn.close()#comment comment comment
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")#comment comment comment
    cur.close()
    conn.close()

def insert_word(conn, word, translation):#comment comment comment
    print(word, translation)

while True: ## REPL - Read Execute Program Loop
    cmd = input("HELLO\nUse the following list of commands\nAdd = Add word and translation\nDelete = Input id to delete row\nQuit = Exit program\nCommand: ").lower()
    if cmd == "list":#comment comment comment
        print(read_dict(conn))
    elif cmd == "add":
        word = input("  Word: ")
        translation = input("  Translation: ")
        add_word(conn, word, translation)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()


##### ADDED FOR COMMIT number two"