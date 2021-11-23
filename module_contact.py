def show_contact(contacts):
    if(len(contacts) <= 0):
        print('========Contact========')
        print('404 Contact Not Found')
        print('====================')
    else:
        print('========Contact========')
        for no in range(0, len(contacts)):
            print('--------------------')
            print(f'{no+1}.')
            for key, value in contacts[no].items():
                print(f'{key}: {value} ')
            print('====================')


def add_contact():
    nama = input('Namanya Siapa? :')
    no = input('No nya dong? :')
    email = input('sekalian email nya ya :')
    return {
        'nama': nama,
        'No Telp': no,
        'email': email
    }


def delete_contact(contacts):

    if(len(contacts) <= 0):
        print('========Contact========')
        print('404 Contact Not Found')
        print('====================')
    else:
        no = int(
            input(f'Silahkan pilih No yang akan di hapus? [1-{len(contacts)}]'))
        if(no <= 0 or no > len(contacts)):
            print('pilih menu dengan benar ya sayang')
        else:
            print('--------------------')
            for key, value in contacts[no - 1].items():
                print(f'{key}: {value} ')
            print('====================')
            yakin_delete = input('Yakin Mau Menghapus No ini..?')
            if(yakin_delete.lower() == 'y'):
                del contacts[no-1]
                print('Contact Delete Successfuly')


def find_contact(contacts):
    dicari = input('Mau Cari Siapa?')
    ada = False
    for contact in contacts:
        nama = contact['nama']
        if(nama.find(dicari) != -1):
            ada = True
            print('--------------------')
            for key, value in contact.items():
                print(f'{key}: {value} ')
            print('====================')
    if(ada == False):
        print('========Contact========')
        print('404 Contact Not Found')
        print('====================')
