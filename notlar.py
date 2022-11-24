import sqlite3 as sql
"""
Bu içerik youtube Mühendisin Bloğu kanalının Python Sqlite video serisi ile hazırlanmıştır.
SQLiteStudio programı ile de oluşturulan veritabanında yapılan işlemler gözlemlenmiştir.
"""

# conn = sql.connect('ders.db')
#
# # cursor sayesinde SQL komutlarımızı python içinde çalıştırabileceğiz.
# cursor = conn.cursor()

# # tablo yoksa oluşturduk
# cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(
#                 name text,
#                 lastname text,
#                 age integer
#                 )""")

# cursor.execute("""DROP TABLE STUDENTS """)  # tabloyu sildik

# # tabloya tekli veri ekleme
# add_command = """INSERT INTO STUDENTS VALUES {}"""
# data1 = ("Kemal","Sunal",60)
# cursor.execute(add_command.format(data1))

# # tabloya çoklu veri ekleme
# add_command = """INSERT INTO STUDENTS VALUES {}"""
# datas = [('Selim', 'Çakır', 27), ('Deniz', 'Toprak', 39), ('Nil', 'Karaibrahimgil', 42)]
# for data in datas:
#     cursor.execute(add_command.format(data))

# # tabloya çoklu veri ekleme alternatif
# add_command = """INSERT INTO STUDENTS VALUES {}"""
# datas = [('Ahmet','Çakır',77), ('Murat','Koç',27), ('Tarık','Akan',58), ('Mehmet', 'Çolak',64)]
# add_command_multiple = """INSERT INTO STUDENTS VALUES (?,?,?) """
# cursor.executemany(add_command_multiple, datas)
#
# conn.commit()
# conn.close()

# # Ekleme işleminin fonksiyonelleştirilmiş hali
# def insert(name, lastname, age):
#     conn = sql.connect('ders.db')
#     cursor = conn.cursor()
#
#     add_command = """INSERT INTO STUDENTS VALUES {}"""
#     data = (name, lastname, age)
#
#     cursor.execute(add_command.format(data))
#     conn.commit()
#     conn.close()
#
# insert("Muhammed", "Balcı", 23)


# # Bilgi Güncelleme
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
# cursor.execute(
#     """UPDATE STUDENTS SET lastname = 'Rüzgar' WHERE name = 'Nil' """)
# conn.commit()
# conn.close()
# Ancak bu şekilde yaparsak tüm nillerin soyismini rüzgar yapar.

# # Spesifik olarak istediğimiz kişiyi güncellemek istiyorsak
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
# cursor.execute(
#     """UPDATE STUDENTS SET lastname = 'Karaibrahimgil' WHERE name = 'Nil' AND lastname='Rüzgar'""")
# conn.commit()
# conn.close()

# # veya istediğimiz kişiye db de bulunduğu sıradan da ulaşabiliriz. SQLiteStudio ile baktığımızda Deniz Toprak 5. sırada
# # yani rowid si 5
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
# cursor.execute(
#     """UPDATE STUDENTS SET lastname = 'Bulut' WHERE rowid = 5""")
# conn.commit()
# conn.close()

# # şimdi de yaşı 30 dan büyük olanların yaşını 1 artıralım
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
# cursor.execute(
#     """UPDATE STUDENTS SET age = age +1 WHERE age > 30""")
# conn.commit()
# conn.close()


# # Tablodan eleman Silme işlemi
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
# cursor.execute(
#     """DELETE FROM STUDENTS WHERE lastname = 'Demir' OR lastname = 'Akan'""")
# conn.commit()
# conn.close()

# # # Yaşa Göre Tablodan eleman Silme işlemi Fonksiyonel
# def delete_age(age):
#     conn = sql.connect('ders.db')
#     cursor = conn.cursor()
#     execute_command = """DELETE FROM STUDENTS WHERE age = {}"""
#     cursor.execute(execute_command.format(age))
#     conn.commit()
#     conn.close()
# delete_age(20)

# # # İsme Göre Tablodan eleman Silme işlemi Fonksiyonel
# def delete_name(name):
#     conn = sql.connect('ders.db')
#     cursor = conn.cursor()
#     execute_command = """DELETE FROM STUDENTS WHERE name = '{}'"""
#     cursor.execute(execute_command.format(name))
#     conn.commit()
#     conn.close()
# delete_name('Murat')


# # Şimdi gelelim db'de ki verileri okumaya
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
# # cursor.execute("SELECT name, lastname from STUDENTS """)  # sadece isim soyisim sütunlarını aldık
# cursor.execute("SELECT * from STUDENTS """)  # tüm sütunları aldık
# list_all = cursor.fetchall()
# for student in list_all:
#     print(student)
# conn.commit()
# conn.close()

# # fetchall() fn'ı tüm elemanları alırken fetchone sadece sıradakini alır.
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
# cursor.execute("SELECT * from STUDENTS """)
# first_student = cursor.fetchone()
# second_student = cursor.fetchone()
# print(first_student)
# print(second_student)
# conn.commit()
# conn.close()

# # fetchmany ise istenen adette alır
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
#
# cursor.execute("SELECT * from STUDENTS """)
# multiple_students = cursor.fetchmany(3)
# print(multiple_students)
# conn.commit()
# conn.close()


# # Şimdi de sıralama işlemlerine bakalım
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
#
# # cursor.execute("SELECT * from STUDENTS ORDER BY age""")  # tüm sütunları aldık ama yaşa göre sıraladık
# # sıralama işlemi default olarak ASC yani küçükten büyüğedir. Eğer büyükten küçüğe istiyorsak sonuna DESC ekleriz.
# cursor.execute("SELECT * from STUDENTS ORDER BY age DESC""")
# list_all = cursor.fetchall()
# for student in list_all:
#     print(student)
# conn.commit()
# conn.close()


# # tablonun kendisini silme işlemi
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
#
# cursor.execute("DROP TABLE STUDENTS """)
#
# conn.commit()
# conn.close()

# # şimdi primary key e sahip bir tablo oluşturalım.
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
#
# cursor.execute("CREATE TABLE CALISKANLAR("
#                "id integer PRIMARY KEY,"
#                "ad text,"
#                "soyad text,"
#                "maas integer) """)
#
# conn.commit()
# conn.close()


# # şimdi bu tabloya verileri ekleyelim
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
#
# datas = [('Ahmet','Yılmaz',2000), ('Mehmet', 'Deniz', 2500),
#          ('Selin', 'Doğan', 3000), ('Ali', 'Demir', 1500)]
# add_command = """INSERT INTO CALISKANLAR (ad,soyad,maas) VALUES (?,?,?)"""
# cursor.executemany(add_command,datas)
#
# conn.commit()
# conn.close()

# # Şimdi IN ifadesini görelim. IN ifadesinde yapacağımız örnekte eğer verdiğimiz isimler tabloda varsa yazdıracağız.
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
#
# cursor.execute("SELECT * from CALISKANLAR WHERE ad IN ('Demet','Kemal','Ahmet','Selin')""")
# list_all = cursor.fetchall()
# for student in list_all:
#     print(student)
# conn.commit()
# conn.close()


# # Şimdi de between ifadesini görelim. Örneğin maaşı 1500 ile 2500 arası olanları yazdıralım.
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
#
# cursor.execute("SELECT * from CALISKANLAR WHERE maas BETWEEN 1500 and 2500""")
# list_all = cursor.fetchall()
# for student in list_all:
#     print(student)
# conn.commit()
# conn.close()


# # Like ifadesinde de benzerlik buluyoruz. Mesela adı ah ile başlayanları yazdıralım.
# conn = sql.connect('ders.db')
# cursor = conn.cursor()
#
# # cursor.execute("SELECT * from CALISKANLAR WHERE ad LIKE 'Ah%'""")  # ahmet'i yazdırır
# # cursor.execute("SELECT * from CALISKANLAR WHERE ad LIKE '%et'""")  # mehmet ve ahmet et ile bittiği için 2 sini yazdırır
# # cursor.execute("SELECT * from CALISKANLAR WHERE ad LIKE '%hm%'""")  # ahmet ve mehmet in ortasında hm olduğundan onları yazar
# cursor.execute("SELECT * from CALISKANLAR WHERE ad LIKE 'm___e_'""")  #1. harf m 5. harf e olanları yazdırıyoruz (Mehmet)
# list_all = cursor.fetchall()
# for student in list_all:
#     print(student)
# conn.commit()
# conn.close()