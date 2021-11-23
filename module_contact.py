def show_contact(contacts):
    if(len(contacts) <= 0):
        print('========Contact========')
        print('404 Contact Not Found')
        print('====================')
    else:
        print('========Contact========')
        for contact in contacts:
            print('--------------------')
            for key, value in contact.items():
                print(f'{key}: {value} ')
        print('====================')


def add_contact():
    nama = input('Namanya Siapa?')
    no = input('No nya dong?')
    email = input('sekalian email nya ya')
    return {
        'nama': nama,
        'no': no,
        'email': email
    }


def delete_contact():
    print('hello')


def find_contact():
    print('find')
