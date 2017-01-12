import generator

class Menu:
    def start_menu(self, connection):
        while True:
            print('Welcome to Tag-clouds!')
            print('1. All Clients')
            print('2. Project Names')
            print('3. Manager Names')
            print('4. Project status')
            
            press_key = input('Please, select a cloud type or press Q to exit from the program: ')

            if press_key == 'q':
               exit()
            elif press_key == '1':
                generator.draw_image(connection.client_importance())
            elif press_key == '2':
                generator.draw_image(connection.based_on_budget())
            elif press_key == '3':
                generator.draw_image(connection.list_of_manager())
            elif press_key == '4':
                generator.draw_image(connection.project_status())
            else:
                return Menu.start_menu()

            