from db_connection import DbConnect

my_connection = DbConnect.get_db_connect('connection.txt')
my_connection.connect_to_db()
answer = my_connection.query("""SELECT * FROM project""")
print(answer)

