from db_connect import DbConnect

connection = DbConnect.initialize('connection.txt')

connection.database_login()

connection.init_data()

print(connection.get_all_projects())
