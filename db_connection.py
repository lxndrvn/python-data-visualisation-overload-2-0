import psycopg2

def DbConnect:
    def __init__(self, db_name, username, host_name, password):
        self.db_name = db_name
        self.username = username
        self.host_name = host_name
        self.password = password
        
    def connect_to_db(self):
        connect_details = psycopg2.connect(
            "dbname='" + self.db_name + "' user='" + self.username + "' host='localhost' password='"+ self.password +'")
        try:
            self.connect = psycopg2.connect(connect_details)
            self.conn.autocommit = True
            print("Connection successful!")
        except Exception as e:
            print("Something went wrong. Unable to connect to the database. Check your login details!")
            print(e)

    def run_sql(self):
        cur = self.conn.cursor()
        cur.execute("""SELECT name FROM base_data WHERE name='Y-find'""")
        text_content=list(cur)
        return text_content