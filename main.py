from db_connection import DbConnect

connection = DbConnect.get_db_connect('connection.txt')
connection.connect_to_db()
connection.run_query_from_file("base_data.sql")

sql_query = ""
answer = connection.query(sql_query)
print(answer)
