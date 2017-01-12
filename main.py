from db_connect import DbConnect

connection = DbConnect.initialize('connection.txt')

connection.database_login()

connection.init_data()

connection.get_all_projects()

print(connection.client_importance())

draw_image(connection.client_importance())