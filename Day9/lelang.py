from logo import logo
import os
import time
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

ulang = True
while ulang:
    print(logo)

    daftar_pelelang = {}

    def hitungHasil():
        if daftar_pelelang:
            pemenang = max(daftar_pelelang, key=daftar_pelelang.get)
            harga_tertinggi = daftar_pelelang[pemenang]
            print(f"\nPemenang Lelang adalah: {pemenang} dengan harga {locale.currency(harga_tertinggi, grouping=True)}")
        else:
            print("Tidak ada data pelelang.")

    def tambah_pelelang():
        nama_pelelang = input("Masukkan Nama Pelelang : ")
        pasang_harga = float(input("Masukkan Harga Lelang : Rp. "))
        daftar_pelelang[nama_pelelang] = pasang_harga
        print(f"Nama : {nama_pelelang}\nPasang Harga : {locale.currency(pasang_harga, grouping=True)}\nBerhasil ditambahkan!")
        
        tanya_user = input("Apakah ada yang mau lelang lagi? (Y/n): ").lower()
        time.sleep(1)
        os.system('cls')
        
        if tanya_user == "y":
            tambah_pelelang()
        elif tanya_user == "n":
            hitungHasil()
        else:
            print("Input tidak valid")
            tambah_pelelang()

    input("Tekan (Enter) Untuk memulai program!")
    tambah_pelelang()
    tanya_ulangi = input("Apakah Anda Mau Mengulangi Program? (Y/n) : ")
    if tanya_ulangi == "n":
        print("TERIMAKASIHH SUDAH MAU COBA PROGRAM INI, HORMAT SAYA ~Gansputra")
        ulang = False