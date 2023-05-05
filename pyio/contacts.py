# from time import sleep
from abc import ABC, abstractmethod
import csv
import pickle
import json
from random import randrange


def class_01():
    print('Python I/O!!')
    contact_file = open('./python_io/data/contacts.csv', encoding='latin_1')

    # content = contact_file.readlines()
    # for contact in content:
    #     print(contact, end='')

    single_line = contact_file.readline(10)
    print("----------------")
    print(single_line)


def class_02():
    wr_cntc = open('./pyio/data/contacts_write.csv', mode='a+', encoding='latin_1')
    for contact in CONTACTS:
        wr_cntc.write(contact)

    # txt = input('Informe um texto\n')
    # print(txt)

    wr_cntc.flush()
    print("Flushed file and waiting 100 seconds to quit program.")

    # wr_cntc.seek(28)
    # for line in wr_cntc:
    #     print(line)

    wr_cntc.seek(7)
    wr_cntc.write('xxx, xxx@xxx.com\n'.upper())
    wr_cntc.flush()
    # txt = input('Informe um texto:\n')
    # print(txt)
    
    wr_cntc.seek(256)
    for contact in wr_cntc:
        print(contact)


def class_03():
    try:
        print('Opening same file multiple times')
        contact_db = open('./pyio/data/tester.csv', encoding='latin_1', mode='a')
        for contact in CONTACTS:
            contact_db.write(contact)

        contact_db.flush()
    except FileNotFoundError:
        print('File not found!')
    except PermissionError:
        print('No permission!!')
    finally:
        print('closing file...')
        contact_db.close()

    try:
        with open('./pyio/data/contacts_write.csv', mode='a+') as f:
            f.write(f'XXX{randrange(0, 10)}, tester{randrange(0, 10)}@sorocaba.sp.gov.br\n')

        with open('./pyio/data/lalala.csv') as f2:
            content = f2.readlines()
            for contact in content:
                print(contact)
        
    except FileNotFoundError as ex:
        print('File not found exception!!')
        print(ex)
    except PermissionError as ex:
        print('Permission Error!!')
        print(ex)


def class_04():
    try:
        txt_byte01 = b'Este eh um texto em bytes'
        print(txt_byte01)

        txt_byte02_utf8 = bytes('Este é um texto em bytes UTF-8', 'utf-8')
        print(txt_byte02_utf8)

        txt_byte02_latin1 = bytes('Este é um texto em bytes LATIN-1', 'latin_1')
        print(txt_byte02_latin1)

        txt = 'Este é um Texto!!'
        txt_byte_error = bytes(f'{txt}', 'utf_8')
        print('-----------------------')
        print(txt_byte_error)
        print('-----------------------')

        with open('./pyio/data/contacts.csv') as f2:
            print(type(f2))
            content = f2.buffer.read()
            print(content)
            # breakpoint()

            # content_str = f2.readlines()
            # for contact in content_str:
            #     print(contact)

        with open('./pyio/data/contacts_write.csv', encoding='latin_1', mode='w') as contact_file_write:
            print(type(contact_file_write))
            text_byte = bytes('Este é u texto em bytes', 'latin_1')
            contact = bytes(f'{randrange(1, 100)}, Verônica, veronica@alura.com.br\n', 'latin_1')
            contact_file_write.buffer.write(contact)

    except FileNotFoundError as ex:
        print('File not found exception!!')
        print(ex)
    except PermissionError as ex:
        print('Permission Error!!')
        print(ex)
    except Exception as ex:
        print('Error with bytes')
        print(ex)


class ContactDao(ABC):
    @abstractmethod
    def get_all(self, filename: str, encoding: str) -> list:
        ...

    @abstractmethod
    def save(self, contacts: list, filename: str, encoding: str) -> None:
        ...


class ContactDaoCsv(ContactDao):
    def get_all(self, filename: str = './pyio/data/contacts_write.csv', encoding: str = 'latin_1') -> list:
        contacts = []
        with open(filename, encoding=encoding) as contact_file:
            reader = csv.reader(contact_file)
            for line in reader:
                id, name, email = line
                contacts.append(Contact(id, name, email))
                # contacts.append(Contact(id=line[0], name=line[1], email=line[2]))  # alternative

        return contacts

    def save(self, contacts: list, filename: str = './pyio/data/contacts_write.csv', encoding: str = 'latin_1') -> None:
        with open(filename, mode='w', encoding=encoding) as contacts_csv:
            for contact in contacts:
                contacts_csv.write(f'{contact}\n')


class ContactDaoPickle(ContactDao):
    def get_all(self, filename: str = './pyio/data/contacts_write.p', encoding: str = 'latin_1') -> list:
        with open(filename, mode='rb') as pickle_file:
            contacts = pickle.load(pickle_file)

        return contacts

    def save(self, contacts: list, filename: str = '.pyio/data/contacts_write.p', encoding: str = 'latin_1') -> None:
        with open(filename, mode='wb') as pickle_file:
            pickle.dump(contacts, pickle_file)


# TODO implement it!
class ContactDaoSql(ContactDao):
    pass


class ContactDaoJson(ContactDao):
    def get_all(self, filename: str = './pyio/data/contacts_write.json', encoding: str = 'latin_1') -> list:
        contacts = []
        with open(filename, mode='r', encoding=encoding) as json_file:
            contacts_json = json.load(json_file)
            for contact in contacts_json:
                contacts.append(Contact(**contact))
                # contacts.append(Contact(id=contact['_id'], name=contact['_name'], email=contact['_email']))  # alternative

        return contacts

    def save(self, contacts: list, filename: str = './pyio/data/contacts_write.json', encoding: str = 'latin_1') -> None:
        with open(filename, mode='w', encoding=encoding) as json_file:
            json.dump(contacts, json_file, default=ContactDaoJson._contact_to_json)
            # json.dump(contacts, json_file, default=lambda contact: {f"{k.replace('_', '')}": v for k, v in contact.__dict__.items()})  # alternative lambda

    @staticmethod
    def _contact_to_json(contact):
        c = dict()
        for k, v in contact.__dict__.items():
            c[k.replace('_', '')] = v

        return c


class Contact:
    """Read contact DB from csv and export data"""

    def __init__(self, id: int, name: str, email: str):
        self._id = id
        self._name = name
        self._email = email

    def __str__(self):
        return f'id: {self._id}, name: {self._name}, email: {self._email}'

    def __repr__(self):
        return f'{self._id=} {self._name=} {self._email}'
        
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @staticmethod
    def convert_contacts(contacts):
        pass


CONTACTS = [
    Contact(id=1, name='Guilherme', email='guilherme@guilherme.com.br'),
    Contact(id=2, name='Elias', email='elias@elias.com.br'),
    Contact(id=3, name='Gabriel', email='gabriel@gabriel.com.br'),
    Contact(id=4, name='Anderson', email='anderson@anderson.com.br'),
    Contact(id=5, name='Alex', email='alex@alex.com.br'),
    Contact(id=6, name='Vini', email='vini@vini.com.br'),
    Contact(id=7, name='Letícia', email='leticia@leticia.com.br'),
    Contact(id=8, name='Giulia', email='giulia@giulia.com.br'),
    Contact(id=9, name='Felipe', email='felipe@felipe.com.br'),
    Contact(id=10, name='Luísa', email='luisa@luisa'),
    Contact(id=11, name='Carol', email='carol@alura.com.br'),
    Contact(id=12, name='Ana', email='ana@alura.com.br'),
    Contact(id=13, name='Tais', email='tais@alura.com.br'),
    Contact(id=14, name='Felipe', email='felipe@alura.com.br'),
    Contact(id=15, name='João', email='joao@alura.com.br'),
]
