import re
import csv


def get_contacts_list():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        # for contact in contacts_list:
        #     contact = {
        #         'lastname': contact[0],
        #         'firstname': contact[1],
        #         'surname': contact[2],
        #         'organization': contact[3],
        #         'position': contact[4],
        #         'phone': contact[5],
        #         'email': contact[6]
        #     }
        return contacts_list


def format_initials(contact):
    fields = contact[3:]
    names = ' '.join(contact[:3]).split()
    while len(names) != 3:
        names.append('')
    normal_contact = names + fields
    return normal_contact


def delete_duplicates(contacts_list):
    merged = {}
    for contact in contacts_list:
        name = f'{contact[0]} {contact[1]}'
        if name in merged:
            for i, field in enumerate(contact):
                if field == '':
                    continue
                merged[name][i] = field
        else:
            merged[name] = contact
    contacts_list = [field for field in merged.values()]
    return contacts_list


def format_phone(old_phone):
    phone_pattern = r'(\+?[7|8])\s*\(?(\d{3,3})\)?\s*\-?(\d{3,3})\-?(\d{2,2})\-?(\d{2,2})\s*\(?[доб.]*\s*(\d+)?\)?'
    if "доб." not in old_phone:
        new_phone_pattern = r'+7(\2)\3-\4-\5'
    else:
        new_phone_pattern = r'+7(\2)\3-\4-\5 доб.\6'
    normal_phone = re.sub(phone_pattern, new_phone_pattern, old_phone)
    print(normal_phone)
    return normal_phone


def fill_phonebook(correct_phonebook):
    with open("correct_phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(correct_phonebook)
        return


if __name__ == '__main__':
    contacts_list = get_contacts_list()
    for i, contact in enumerate(contacts_list):
        contacts_list[i] = format_initials(contact)
        contacts_list[i][5] = format_phone(contact[5])
    correct_phonebook = delete_duplicates(contacts_list)
    fill_phonebook(correct_phonebook)

