import psycopg2
connection = psycopg2.connect(
   host="localhost",
   database="dict",
   user="postgres",
   password="XXXXX"
)

def read_dict(connection):
    cur = connection.cursor()
    cur.execute("SELECT * FROM dictionary2;")
    cur.execute("COMMIT;")
    rows = cur.fetchall()
    cur.close()
    connection.close()
    return rows
def add_word(connection, word, translation):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO dictionary2 (word, translation) VALUES ('{word}', '{translation}');")
    cur.execute("COMMIT;")
    cur.close()
    connection.close()
def delete_word(connection, ID):
    cur = connection.cursor()
    cur.execute(f"DELETE FROM dictionary2 WHERE id = '{ID}';")
    cur.execute("COMMIT;")
    cur.close()
    connection.close()
def save_dict(connection):
    cur = connection.cursor()
    cur.execute("COMMIT;")
    cur.close()
    connection.close()

def insert_word(connection, word, translation):
    print(word, translation)

while True: ## REPL - Read Execute Program Loop
    cmd = input("HELLO\nUse the following list of commands\nAdd = Add word and translation\nDelete = Input id to delete row\nQuit = Exit program\nCommand: ").lower()
    if cmd == "list":
        print(read_dict(connection))
    elif cmd == "add":
        word = input("  Word: ")
        translation = input("  Translation: ")
        add_word(connection, word, translation)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(connection, ID)
    elif cmd == "quit":
        save_dict(connection)
        exit()


##### ADDED FOR COMMIT number two"