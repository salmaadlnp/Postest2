

import os
os.system ("cls")
from prettytable import PrettyTable

print("---------------------------------")
print("**********Login Program**********")
print("=================================")

barang = {
    "Product" : ['Micellar Water','Facial Wash','Toner','Serum','Moisturizer','Sunscreen'],
    "Harga" :  [30,50,150,130,160,60]
    }

table=PrettyTable()
judul = ["Product","Harga"]
table.field_names = judul

username = []
password = []

def buat_table():
    table.clear_rows()
    for i in range(len(barang.get("Product"))):
        table.add_row([barang.get("Product")[i], barang.get("Harga")[i]])

def program_user():
    while True:
        print("""
        ========================
        |       MENU USER      |
        |======================|
        | 1. Tampilkan Barang  |
        | 2. Beli Barang       |
        | 3. Exit              |
        ========================
        """)
        menu_user= input('\n masukan pilihan : ')
        
        if menu_user=='1':
            print()
            print("-"*25)
            buat_table()
            print(table)
            print("-"*25)
            print()
            continue
        elif menu_user == '2':
            menu2 ="y"
            while menu2 == "y":
                print("***** SELAMAT BERBELANJA *****")
                buat_table()
                print(table)
                while True :
                    nama_barang = input("masukan nama barang : ").upper()
                    try:
                        cari = barang.get("Product")
                        hasil_index = cari.index(nama_barang)
                        break 

                    except ValueError:
                        print("ERROR-> Masukan kembali nama barang anda")
        
                while True:
                    total = int(input("masukkan jumlah barang yang ingin dibeli: "))
                    if total > 0 :
                        totalharga = (barang.get("harga")[hasil_index]*total)
                        print("="*40, "\n")
                        print("\tBarang yang Ingin Dibeli\t")
                        print("barang: ",(barang.get("Product")[hasil_index]))
                        print("harga : ",(barang.get("harga")[hasil_index]))
                        print("total harga :",totalharga)
                        print("\n", "="*40)
                        break
                    else:
                        print("inputan tidak valid")
                        continue

                menu2 = input('Beli lagi ? [y/t] : ').lower()
                if menu2 == "t":
                    break

        elif menu_user == '3':
            break

        else :
            continue

def program_admin():
    while True :
        print("""
            =========================================
            | ----------  PILIHAN ADMIN  ---------- |
            |  1.Menambahkan barang dan harga       |
            |  2.Melihat barang dan harga           |
            |  3.Memperbarui nama barang            |
            |  4.Menghapus barang tertentu          |
            |  5.Logout Admin                       |
            =========================================
            """)
        print()

        # fungsi create
        menu = input("Masukan menu [1-5] : ")
        if menu == '1':
            menu1 ='y'
            print("Menambahkan barang dan harga ")
            while menu1 == 'y':
                print()
                print("-"*25)
                print()
                buat_table()
                print(table)
                print()
                print("-"*25)
                BarangBaru = input("Masukan nama barang : ").upper()
                #eror handling inputan berupa sring
                while True:
                    try:
                        HargaBaru =int(input("Masukan harga barang : "))
                        break
                    except ValueError :
                        print("Tidak valid, silahkan coba lagi")
                print()
                print("-"*25)
                print()
                barang.get("Product").append(BarangBaru)
                barang.get("harga").append(HargaBaru)
                print()
                buat_table()
                print(table)
                menu1 = input('Tambahkan Data Lagi ? [y/t] : ').lower()
                if menu1 == "t":
                    break
        # fungsi read
        elif menu == '2':
            menu2 = 'y'
            print("Melihat barang dan harga")
            while menu2 == 'y' :
                while True:
                    print("-"*25)
                    buat_table()
                    print(table)
                    print("-"*25)
                    print()
        # fungsi update
        elif menu == '3':
            menu3 = 'y'
            print("Memperbarui Nama Barang")
            while menu3 == 'y':
                while True:
                    print()
                    print("-"*25)
                    print()
                    buat_table()
                    print(table)
                    print()
                    nama_barang = input("masukan nama barang : ").upper()
                    try:
                        cari = barang.get("Product")
                        hasil_index = cari.index(nama_barang.upper())
                        break 

                    except ValueError:
                        print("Periksa kembali penulisan anda")

                a =input("masukan barang baru : ").upper()
                print()
                #eror handling inputan berupa sring
                while True:
                    try:
                        b = input("masukan harga barang baru :")
                        break
                    except ValueError :
                        print("Tidak valid, silahkan coba lagi")

                barang.get("Product")[hasil_index] = a
                barang.get("harga")[hasil_index]= b
                buat_table()
                print(table)
                
                menu3 = input('Update/ubah Data Lagi ?  [y/t]: ').lower()
                if menu3 == "t":
                        break
        # fungsi delete
        elif menu == '4':
            menu4 = 'y'
            print("Menghapus barang tertentu")
            while menu4 == 'y' :
                while True:
                    buat_table()
                    print(table)
                    print()
                    nama_barang = input("masukan nama barang : ").upper()
                    try:
                        cari = barang.get("Tidak valid, silahkan coba lagi")
                        hasil_index = cari.index(nama_barang)
                        break 

                    except ValueError:
                        print("Periksa kembali penulisan anda")

                a = barang.get("Product")
                c = a.index(nama_barang)
                a.pop(c)
                buat_table()
                print(table)

                menu4 = input('Delete Data Lagi ? [y/t]: ')
                if menu4 == "t":
                        break

        elif menu == '5':
            break
            
        else :
            print("input Not Found")
            continue
    
def admin():
    us_admin = "salma"
    pw_admin = "admin1"   

    i = 0  
    while i < 3 :
        print('='*24)
        print('halo admin, silahkan login\n')  
        us_admin =input("Username : ")
        pw_admin = input("Password : ")
        if us_admin == "salma" and pw_admin == "admin1":
            print()
            print("LOGIN SUKSESS")
            break
        else :
            print()
            print('LOGIN GAGAL')
            i+=1 
            continue 
    if i <3 :
        program_admin()
    elif i==3:
        exit

     
def login_user(username,password):

    print()
    print("SILAHKAN LOGIN")
    i = 0  
    while i < 3 :  
        us_user =input("Username : ")
        pw_user = input("Password : ")  
        if us_user == username and pw_user == password:
            print()
            print("LOGIN SUKSESS\n")
            break
        else :
            print()
            print('LOGIN GAGAL')
            i+=1 
            continue 
    if i < 3 :
        program_user()
    elif i==3:
        exit()       
   
menu ='y'
while menu== 'y':
    print('Login Sebagai : \n1.admin \n2.user')
    sebagai =input('\nmasukan opsi: ') 
    if sebagai == '1' or sebagai == 'admin':
        admin()
    elif sebagai == '2' or sebagai == 'user':
        
        while True:
            # try:
            # login_user(username,password)
            account = input("Sudah punya akun [y/t] : ").lower()
            if account == "t" :
                print('REGISTRASI AKUN TERLEBIH DAHULU')
                username = input("Username : ")
                password = input("Password : ")
                login_user(username,password)
                break
            elif account == "y":
                login_user(username,password)
                break
            else:
                continue
        
            
            # except:
            #     break


    else:
        print('eror')

    menu = input('ke menu login?[y/t] : ').lower()
    if menu == 't':
        break
    elif account == "y":
        login_user()
