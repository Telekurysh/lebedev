import sqlite3
import json


def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                        id INTEGER PRIMARY KEY,
                        created TEXT,
                        modified TEXT,
                        nativeId TEXT,
                        nativeName TEXT,
                        cardNumber TEXT,
                        cardDate TEXT,
                        studio TEXT,
                        crYearOfProduction TEXT,
                        director TEXT,
                        scriptAuthor TEXT,
                        composer TEXT,
                        cameraman TEXT,
                        artdirector TEXT,
                        producer TEXT,
                        mediaFormat TEXT,
                        numberOfSeries TEXT,
                        color TEXT,
                        categoryOfRights TEXT,
                        ageCategory TEXT,
                        annotation TEXT,
                        viewMovie TEXT,
                        countryOfProduction TEXT,
                        category TEXT,
                        approver TEXT,
                        approverFIO TEXT,
                        cadrFormat TEXT,
                        rentalRightsTransferred TEXT,
                        volumeOfMedia TEXT,
                        capacity TEXT,
                        startDateRent TEXT,
                        owner TEXT,
                        deleted TEXT,
                        doNotShowOnSite TEXT,
                        ageLimit TEXT
                    )''')


def insert_data(cursor, data):
    cursor.execute('''INSERT INTO movies (
                        created, modified, nativeId, nativeName, cardNumber,
                        cardDate, studio, crYearOfProduction, director,
                        scriptAuthor, composer, cameraman, artdirector, producer,
                        mediaFormat, numberOfSeries, color, categoryOfRights,
                        ageCategory, annotation, viewMovie, countryOfProduction,
                        category, approver, approverFIO, cadrFormat,
                        rentalRightsTransferred, volumeOfMedia, capacity,
                        startDateRent, owner, deleted, doNotShowOnSite, ageLimit
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   data)


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_to_sqlite(json_filename, db_filename):
    data = read_json(json_filename)

    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    create_table(cursor)

    for item in data:
        insert_data(cursor, (
            item.get('created', ''),
            item.get('modified', ''),
            item.get('nativeId', ''),
            item.get('nativeName', ''),
            item.get('data', {}).get('general', {}).get('cardNumber', ''),
            item.get('data', {}).get('general', {}).get('cardDate', ''),
            item.get('data', {}).get('general', {}).get('studio', ''),
            item.get('data', {}).get('general', {}).get('crYearOfProduction', ''),
            item.get('data', {}).get('general', {}).get('director', ''),
            item.get('data', {}).get('general', {}).get('scriptAuthor', ''),
            item.get('data', {}).get('general', {}).get('composer', ''),
            item.get('data', {}).get('general', {}).get('cameraman', ''),
            item.get('data', {}).get('general', {}).get('artdirector', ''),
            item.get('data', {}).get('general', {}).get('producer', ''),
            item.get('data', {}).get('general', {}).get('mediaFormat', ''),
            item.get('data', {}).get('general', {}).get('numberOfSeries', ''),
            item.get('data', {}).get('general', {}).get('color', ''),
            item.get('data', {}).get('general', {}).get('categoryOfRights', ''),
            item.get('data', {}).get('general', {}).get('ageCategory', ''),
            item.get('data', {}).get('general', {}).get('annotation', ''),
            item.get('data', {}).get('general', {}).get('viewMovie', ''),
            item.get('data', {}).get('general', {}).get('countryOfProduction', ''),
            item.get('data', {}).get('general', {}).get('category', ''),
            item.get('data', {}).get('general', {}).get('approver', ''),
            item.get('data', {}).get('general', {}).get('approverFIO', ''),
            item.get('data', {}).get('general', {}).get('cadrFormat', ''),
            item.get('data', {}).get('general', {}).get('rentalRightsTransferred', ''),
            item.get('data', {}).get('general', {}).get('volumeOfMedia', ''),
            item.get('data', {}).get('general', {}).get('capacity', ''),
            item.get('data', {}).get('general', {}).get('startDateRent', ''),
            item.get('data', {}).get('general', {}).get('owner', ''),
            item.get('data', {}).get('general', {}).get('deleted', ''),
            item.get('data', {}).get('general', {}).get('doNotShowOnSite', ''),
            item.get('data', {}).get('general', {}).get('ageLimit', '')
        ))

    conn.commit()
    conn.close()


save_to_sqlite('1.json', './../db.sqlite3')
