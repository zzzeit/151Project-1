

FNAME = 0
LNAME = 1
SEX = 2
ID = 3
YRLVL = 4
CCODE = 5
PCODE = 6


class DataManager:
    def __init__(self, conn, curs):
        self.connection = conn
        self.cursor = curs

    def write_data(self, table_name, data):
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT OR IGNORE INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data))
        self.connection.commit()

    def load_data(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        return self.cursor.fetchall()