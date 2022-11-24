from projeVeritabani import *

def print_menu():
    print("""
    1) Giriş Yap
    2) Kaydol
    3) Kapat
    """)

def login_menu(user):
    print(f"""
    {user[1]} {user[2]} {user[3]}
    1) Bir kullanıcı arama
    2) Tüm kullanıcıları yazdır
    3) Hesabımı sil
    4) Çıkış yap
    """)

create_table()

while True:
    print_menu()
    secim = input("Seçim:")
    if secim == '1':
        username = input("Kullanıcı adı: ")
        password = input("Password: ")
        search = search_username(username)
        if search is None:
            print("Böyle bir kullanıcı yok")
            continue
        elif password == search[4]:
            while True:
                print(login_menu(search))
                secim2 = input("Secim: ")
                if secim2 == '1':
                    u = input("Kullanıcı adı: ")
                    birisi = search_username(u)
                    if birisi is None:
                        print("Kullanıcı bulunamadı")
                        continue
                    print(f"{birisi[1]} {birisi[2]}, {birisi[3]}")
                elif secim2 == '2':
                    print_all()
                elif secim2 == '3':
                    delete_account(username)
                    break
                elif secim2 == '4':
                    break



    elif secim == '2':
        name = input("Adınız: ")
        lastname = input("Soyadınız: ")
        username = input("Kullanıcı adınız: ")
        password = input("Şifreniz: ")
        search = search_username(username)
        if search is not None:
            print("Bu kullanıcı mevcut")
            continue
        else:
            insert_table(name,lastname,username,password)
            print("Kayıt başarılı")
            continue
    elif secim == '3':
        pass
    else:
        exit()