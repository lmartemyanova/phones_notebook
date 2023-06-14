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
    for contact in contacts_list:
        if contact[0] == contact[0] and contact[1] == contact[1]:
            for i, field in enumerate(contact):
                if field == '':
                    continue
                contact[i] = field
        else:
            contacts_list[contact] = contact
    # print(contacts_list)
    return contacts_list


def format_phone(old_phone):
    # phone_pattern = r'\+?[7|8]\s*\(?\d+\)?\s*\-?\d+\-?\d+\-?\d+\s*\(?[доб.]*\s*\d+\)?'
    phone_pattern = r'(\+?[7|8])\s*\(?(\d{3,3})\)?\s*\-?(\d{3,3})\-?(\d{2,2})\-?(\d{2,2})\s*\(?[доб.]*\s*(\d+)?\)?'
    phone = re.findall(phone_pattern, old_phone)
    if "доб." not in old_phone:
        new_phone_pattern = r'+7(\2)\3-\4-\5'
    else:
        new_phone_pattern = r'+7(\2)\3-\4-\5 доб.\6'
    normal_phone = re.sub(phone_pattern, new_phone_pattern, old_phone)
    # print(normal_phone)
    # email_pattern = r'[a-zA-Z0-9\.]+[^\s]@{1,1}[a-zA-Z0-9]+\.[a-zA-Z0-9]+'
    # email = re.findall(email_pattern, old_phone)
    # print(email)
    return normal_phone


def fill_phonebook(correct_phonebook):
    with open("correct_phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(correct_phonebook)
        return


if __name__ == '__main__':
    contacts_list = get_contacts_list()
    for i, contact in enumerate(contacts_list):
        contacts_list[i] = format_initials(contact)
        contacts_list[i][5] = format_phone(contact[5])
    correct_phonebook = delete_duplicates(contacts_list)
    # fill_phonebook(correct_phonebook)

