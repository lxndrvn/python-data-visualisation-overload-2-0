from db_connection import DbConnect

connection = DbConnect.get_db_connect('connection.txt')
connection.open_data_table("base_data.sql")
answer = connection.connect_to_db()
print(answer)

