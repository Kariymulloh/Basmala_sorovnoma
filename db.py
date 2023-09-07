import sqlite3

# Ma'lumotlar bazasini yaratish va bog'lanish
conn = sqlite3.connect("likelist.db")
cursor = conn.cursor()

# "like" jadvalni yaratish (agar mavjud bo'lmasa)
cursor.execute('''CREATE TABLE IF NOT EXISTS like (
                    id INTEGER PRIMARY KEY,
                    school INTEGER,
                    count INTEGER
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS user_list (
                    id INTEGER PRIMARY KEY,
                    number INTEGER
                )''')
# Ma'lumotlarni yozish
# schools = [("Maktab 1", 10), ("Maktab 2", 15), ("Maktab 3", 8)]

# cursor.executemany("INSERT INTO like (school, count) VALUES (?, ?)", schools)
# conn.commit()

# # Ma'lumotlarni o'qish
# cursor.execute("SELECT school, count FROM like")
# result = cursor.fetchall()

# for row in result:
#     school, count = row
#     print(f"School: {school}, Count: {count}")

# # Ma'lumotlar bazasini yopish
conn.close()
