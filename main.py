from db_connect import DbConnect
import generator

connection = DbConnect.initialize('connection.txt')

connection.database_login()

connection.create_table()

print(connection.client_importance())

generator.draw_image(connection.client_importance())