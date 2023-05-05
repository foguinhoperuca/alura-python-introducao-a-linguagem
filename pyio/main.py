import sys
import traceback
from random import randrange

from contacts import CONTACTS, class_01, class_02, class_03, class_04, ContactDaoCsv, ContactDaoPickle, ContactDaoJson, Contact


if __name__ == "__main__":
    # class_01()
    # class_02()
    # class_03()
    # class_04()

    try:
        # Constant
        contacts = CONTACTS
        for contact in contacts:
            print(f'Contact from CONSTANT is: {contact}')

        # CSV
        print('............')
        dao_csv = ContactDaoCsv()
        contacts_csv = dao_csv.get_all(filename='./pyio/data/contacts.csv', encoding='latin_1')
        for contact in contacts_csv:
            print(f'Contact from CSV ORIGINAL is: {contact}')

        contacts.append(Contact(id=randrange(16, 100), name='CSV added', email='csv.pyio@alura.com.br'))
        dao_csv.save(contacts, './pyio/data/contacts_write.csv')
        print('************')
        contacts_csv_saved = dao_csv.get_all(filename='./pyio/data/contacts_write.csv', encoding='latin_1')
        for contact in contacts_csv_saved:
            print(f'Contact from CSV SAVED is: {contact}')

        # Pickle
        print('------------')
        dao_pickle = ContactDaoPickle()
        contacts.append(Contact(id=randrange(101, 200), name='The first of Pickle', email='pickle.pyio@alura.com.br'))
        dao_pickle.save(contacts, './pyio/data/contacts_write.pickle')
        contacts_pickle = dao_pickle.get_all('./pyio/data/contacts_write.pickle')
        for contact in contacts_pickle:
            print(f'Contact from PICKLE is: {contact}')

        # JSON
        print('============')
        dao_json = ContactDaoJson()
        contacts.append(Contact(id=randrange(201, 300), name='The last of JSON', email='json.pyio@alura.com.br'))
        dao_json.save(contacts, filename='./pyio/data/contacts_write.json')
        contacts_json = dao_json.get_all('./pyio/data/contacts_write.json')
        for contact in contacts_json:
            print(f'Contact from JSON is: {contact}')

    except Exception as ex:
        print('*************************************')
        print('Got some exception!!')
        print(f'EXCEPTION: {ex} ; ARG: {ex.args}')
        print('*************************************')
        traceback.print_exc()

    sys.exit(0)
