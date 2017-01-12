import psycopg2

class DbConnect:
    def __init__(self, db_name, username, host_name, password):
        self.db_name = db_name
        self.username = username
        self.host_name = host_name
        self.password = password
        self.conn_str = "dbname='" + self.db_name + "' user='" + self.username + "' host='localhost' password='" + self.password + "'"
        self.database = None

    # instantiate connection with login parameters
    @staticmethod
    def initialize(file_name):
            with open(file_name, "r") as f:
                data_line = f.readlines()
                db_name = data_line[0].replace("\n", "").split(":",1)[1]
                username = data_line[1].replace("\n", "").split(":",1)[1]
                host_name = data_line[2].replace("\n", "").split(":",1)[1]
                password = data_line[3].replace("\n", "").split(":",1)[1]
                create_connect = DbConnect(db_name, username, host_name, password)
                return create_connect

    # commits connection to database
    def database_login(self):
        try:
            self.database = psycopg2.connect(self.conn_str)
            self.database.autocommit = True
            print("Connection successful!")
        except Exception as e:
            print("Something went wrong. Unable to connect to the database. Check your login details!")
            print(e)

    def create_table(self):
        sql_script = open("base_data.sql", "r").read()
        cursor = self.run_sql_script(sql_script)

    def run_sql_script(self, query_str):
        cursor = self.database.cursor()
        cursor.execute(query_str)
        return cursor

    def client_importance(self):
        query_str = """SELECT count(id)*2+10, array_agg(substring(main_color from 2 for 3)), company_name FROM project GROUP BY company_name"""
        cursor = self.run_sql_script(query_str)
        return cursor.fetchall()