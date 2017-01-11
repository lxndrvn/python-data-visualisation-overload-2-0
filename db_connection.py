import psycopg2

def DbConnect():
    def __init__(self, db_name, username, host_name, password):
        self.db_name = db_name
        self.username = username
        self.host_name = host_name
        self.password = password
    
    @staticmethod
    def open_file(file_name):
            with open(file_name, "r") as f:
                data_line = f.readlines()
                return data_line[0].replace('\n', '')

    def connect_to_db(self):
        try:
            conn_str = DbConnect.open_file('connection.csv')
            conn = psycopg2.connect(conn_str)
            conn.autocommit = True
            print("Connection successful!")
            cursor = conn.cursor()
            cursor.execute("""SELECT name FROM base_data WHERE name='Y-find'""")
            return cursor.fetchall()
        
        except Exception as e:
            print("Something went wrong. Unable to connect to the database. Check your login details!")
            print(e)