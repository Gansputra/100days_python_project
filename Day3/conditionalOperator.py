#Game dengan Pengimplementasi Operator Kondisional dasar
#Operator Kondisional
import time
print("Selamat datang di game Tebak Pintu !")

#Memulai permainan
print("Anda memasuki ruangan misterius. Ada tiga pintu yang bisa Anda pilih.")
print("Pilih pintu: 1, 2, atau 3")
pintu = int(input("Masukkan nomor pintu yang Anda pilih: "))
if pintu == 1:
    print("Anda memilih pintu 1. Di dalamnya terdapat labirin")
    time.sleep(1)
    print("Anda harus mencari jalan keluar dari labirin tersebut.")
    time.sleep(1)
    langkah = input("Apakah Anda ingin menjelajahi labirin? (ya/tidak) ")
    if langkah == "ya":
        print("Anda berani menjelajahi labirin!")
        time.sleep(1)
        print("Di ujung labirin, Anda menemukan 3 pintu lagi.")
        time.sleep(1)
        print("Pilih pintu: 1, 2, atau 3")
        pintu_lanjutan = int(input("Masukkan nomor pintu yang Anda pilih: "))
        if pintu_lanjutan == 1:
            time.sleep(1)
            print("Anda memilih pintu 1. Di dalamnya terdapat harta karun!")
        elif pintu_lanjutan == 2:
            time.sleep(1)
            print("Anda memilih pintu 2. Di dalamnya terdapat jebakan!")        
        elif pintu_lanjutan == 3:
            time.sleep(1)
            print("Anda memilih pintu 3. Di dalamnya terdapat jalan keluar!")
            print("Selamat, Anda berhasil keluar dari labirin!")
    else:
        print("Anda memilih untuk tidak menjelajahi labirin.")
    
elif pintu == 2:
    print("Anda memilih pintu 2. Di dalamnya terdapat monster!")
    time.sleep(1)
    print("Anda harus melawan monster tersebut untuk keluar dari ruangan.")
    time.sleep(1)
    print("Anda berhasil mengalahkan monster dan muncul 3 pintu!")
    time.sleep(1)
    print("Pilih pintu: 1, 2, atau 3")
    time.sleep(1)
    pintu_lanjutan = int(input("Masukkan nomor pintu yang Anda pilih: "))
    if pintu_lanjutan == 1:
        print("Anda memilih pintu 1. Di dalamnya terdapat harta karun!, anda terlena dengan harta karun tersebut. Anda tidak bisa keluar dari ruangan!")
    elif pintu_lanjutan == 2:
        print("Anda memilih pintu 2. Di dalamnya terdapat jebakan! Anda tidak bisa keluar dari ruangan!")
        time.sleep(1)
        print("Anda terjebak dalam jebakan!")
    elif pintu_lanjutan == 3:
        print("Anda memilih pintu 3. Di dalamnya terdapat jalan keluar!")
        time.sleep(1)
        print("Selamat, Anda berhasil keluar dari ruangan misterius!")
    else:
        print("Pilihan tidak valid. Silakan pilih pintu 1, 2, atau 3.")
elif pintu == 3:
    time.sleep(1)
    print("Anda memilih pintu 3. Di dalamnya terdapat jalan keluar!")
    time.sleep(1)
    print("Selamat, Anda berhasil keluar dari ruangan misterius!")
else:
    print("Pilihan tidak valid. Silakan pilih pintu 1, 2, atau 3.")