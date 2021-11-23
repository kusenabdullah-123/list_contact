from module_contact import show_contact
from module_contact import add_contact
from module_contact import delete_contact
from module_contact import find_contact

list_menu = ['list contact', 'add contact',
             'delete contact', 'find contact', 'shutdown server']
list_contact = []

while True:
    print('====== Menu Contact ======')
    for i in range(0, len(list_menu)):
        print(f'{i+1}. {list_menu[i].capitalize()}')
    menu = int(input('Silahkan Pilih Menu :'))
    if(menu <= 0 or menu > len(list_menu)):
        print('Silahkan Pilih Menu Yang Tersedia ya..')
    else:
        if(menu == 1):
            show_contact(list_contact)
        elif(menu == 2):
            list_contact.append(add_contact())
        elif(menu == 3):

            delete_contact(list_contact)
        elif(menu == 4):
            find_contact(list_contact)
        elif (menu == 5):
            print('Comeback Soon')
            break
