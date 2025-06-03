import easyocr
import sqlite3
from datetime import datetime

conn = sqlite3.connect('Tel_numbers.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tel_numbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tel_numbers TEXT,
    created_at TEXT
)
""")


def text_recognition(file_path):
    reader = easyocr.Reader(['ru'])
    result = reader.readtext(file_path)
cd/ro
    return result


def main():
    file_path = input('Enter a file path: ')
    x = text_recognition(file_path=file_path)
    tel_numbers = x[0][1]
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Natija: {tel_numbers}')


    # Вставка в таблицу
    cursor.execute("""
    INSERT INTO tel_numbers (tel_numbers, created_at) VALUES (?, ?)
    """, (tel_numbers, created_at)
    )
    conn.commit()
    conn.close()
    print("✅ Данные успешно сохранены в базе tel_numbers.db.")

if __name__ == "__main__":
    main()