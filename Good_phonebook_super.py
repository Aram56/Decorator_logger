from pprint import pprint
import csv
import re
from logger_1_1 import logger


with open("phonebook_raw.csv", encoding = "UTF8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: пункты 1-3 ДЗ
@logger
def names_on_place():
    for line_names in contacts_list[1:]: 
        line_3 = " ".join(line_names[:3])
        list_line_3 = line_3.split(" ")
        line_names[0] = list_line_3[0]
        line_names[1] = list_line_3[1]
        line_names[2] = list_line_3[2]
    # pprint(contacts_list)
@logger
def phone_number_perfect():
    pattern_phone = r"(\+7|8)+\s?\(?(\d{3})\)?\s?-?(...)\s?-?(..)\s?-?(..)(\s)?\(?(доб.)?\s?(\d+)?\)?"
    new_phone_sub = r"+7(\2)\3-\4-\5\6\7\8"
    for line_phone in contacts_list:
        line_phone[5] = re.sub(pattern_phone, new_phone_sub, line_phone[5])
        # print(line_phone[5])
    # pprint(contacts_list)

data_new = []

@logger
def one_in_one():
    for one_line in contacts_list:
        if one_line[:2] not in data_new:
            data_new.append(one_line[:2])

    for line in data_new:
        line += ['','','','','']
        
    for new_line in data_new:
        for line in contacts_list:
            if new_line[:2] == line[:2]:
                if new_line[2] != line[2]:
                    new_line[2] += line[2]
                if new_line[3] != line[3]:
                    new_line[3] += line[3]
                if new_line[4] != line[4]:
                    new_line[4] += line[4]
                if new_line[5] != line[5]:
                    new_line[5] += line[5]
                if new_line[6] != line[6]:
                    new_line[6] += line[6]

    pprint(f"'data_new 1' - {data_new}")

if __name__ == '__main__':
    names_on_place()
    phone_number_perfect()
    one_in_one()

    with open("phonebook.csv", "w", encoding = "UTF8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(data_new)