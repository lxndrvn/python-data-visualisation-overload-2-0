import generator
from db_connect import DbConnect

class Menu:

    @staticmethod
    def start_menu():
        while True:
            print('Welcome to Tag-clouds!')
            print('1. All Clients')
            print('2. Project Names')
            press_key = input('Please, select a cloud type or press Q to exit from the program: ')

            if press_key == 'q':
               exit()
            elif press_key == '1':
                generator.draw_image(DbConnect.client_importance)
            else:
                return Menu.start_menu()