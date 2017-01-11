import psycopg2

class DbConnect():
    def __init__(self, db_name, username, host_name, password):
        self.db_name = db_name
        self.username = username
        self.host_name = host_name
        self.password = password
        self.conn_str = "dbname='" + self.db_name + "' user='" + self.username + "' host='localhost' password='"+ self.password +"'"
        self.connection = None
    
    @staticmethod
    def get_db_connect(file_name):
            with open(file_name, "r") as f:
                data_line = f.readlines()
                db_name = data_line[0].replace("\n", "").split(":",1)[1]
                username = data_line[1].replace("\n", "").split(":",1)[1]
                host_name = data_line[2].replace("\n", "").split(":",1)[1]
                password = data_line[3].replace("\n", "").split(":",1)[1]
                db_connect = DbConnect(db_name, username, host_name, password)
                return db_connect

    def connect_to_db(self):
        try:
            self.connection = psycopg2.connect(self.conn_str)
            self.connection.autocommit = True
            print("Connection successful!")
        except Exception as e:
            print("Something went wrong. Unable to connect to the database. Check your login details!")
            print(e)

    def query(self, query_str):
        cursor = self.connection.cursor()
        cursor.execute(query_str)
        return cursor.fetchall()
    
