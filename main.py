from db_connect import DbConnect
from menu import Menu
import generator


connection = DbConnect.initialize('connection.txt')

connection.database_login()

connection.create_table()

start = Menu()
start.start_menu(connection)
