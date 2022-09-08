def add_surname(d):

    with open ('book.csv', 'a') as file:
        file.write('Фамилия: {}\n'
        
    .format (d))

def add_name(d):

    with open ('book.csv', 'a') as file:
        file.write('Имя: {}\n'
 .format (d))

def add_number (d):

from tabulate import tabulate1

prinr = ["Surname", "Name", "Phone number", "Discription"]


def add_data(d):
    with open ('book.csv', 'a') as file:
        file.write('Номер телефона: {}\n'
 .format (d))
def add_description(d):
    
        file.write (tabulate(d, headers ='head', tablefmt="grid"·))


    with open ('book.csv', 'a') as file:
        file.write('Описание: {}\n'.format (d))