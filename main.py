import json
import csv
import os


from loguru import logger


def export_notes(notes):
    """Tratar notas"""
    row_list = []
    for note in notes:
        # Crear un registro estandar y guardar en la salida
        # "Group", "Title", "Username", "Password", "URL", "Notes"
        row_list.append([
            "Root/notes",
            note['label'],
            '',
            note['text'],
            '',
            ''
        ])

    logger.info("{records} found", records=len(row_list))

    return row_list


def export_cards(param):
    """Tratar tarjetas"""
    logger.debug("Aún no :)")
    pass


def export_logins(logins):
    """Tratar logins"""
    row_list = []
    for login in logins:
        # Crear un registro estandar y guardar en la salida
        # "Group", "Title", "Username", "Password", "URL", "Notes"
        try:
            name = login['custName']
            if name == '':
                name = login['url']
        except KeyError:
            name = login['url']

        row_list.append([
            "Root/web",
            name,
            login['loginName'],
            login['pwd'],
            login['url'],
            login['note']
        ])

    logger.info("{records} found", records=len(row_list))

    return row_list


if __name__ == "__main__":
    file_name = input("Please enter fileName: ")

    if file_name == '':
        file_name = "misPasswords.json"
    elif file_name.endswith('.json') == False:
        file_name = file_name + ".json"

    file_contents = open(file_name, "r")
    json_data = json.load(file_contents)

    # Delete generated files
    try:
        os.remove("passwords.csv")
    except FileNotFoundError:
        pass

    row_list = export_notes(json_data['notes'])
    with open('passwords.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)

    export_cards(json_data['cards'])

    row_list = export_logins(json_data['logins'])
    with open('passwords.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
