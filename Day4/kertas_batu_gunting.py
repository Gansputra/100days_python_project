ascii_tangan = [("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""),("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""), ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")]

import time
import random
import os

Selesai = False
hasil = ""
user_ascii = 0
komputer_ascii = 0
list_pilihan = ["Gunting","Batu","Kertas"]
skor = [0,0]

while not Selesai:
    print(" |                 SKOR TERKINI                  |")
    print(" |     SKOR PEMAIN      |      SKOR KOMPUTER     |")
    print(f" |          {skor[0]}           |           {skor[1]}            |")
    pilihan_user = input("Masukkan Pilihan (Gunting,Batu,Kertas) :").lower()
    pilihan_komputer = random.choice(list_pilihan)
    if (pilihan_user == "gunting"):
        if (pilihan_komputer == "Gunting"):
            hasil = "Seri!"
            komputer_ascii = 2
        elif (pilihan_komputer == "Batu"):
            hasil = "Kalah!"
            komputer_ascii = 0
            skor[1] += 1
        else:
            hasil = "Menang!"
            komputer_ascii = 1
            skor[0] += 1
        user_ascii = 2
    elif (pilihan_user == "batu"):
        if (pilihan_komputer == "Gunting"):
            hasil = "Menang!"
            komputer_ascii = 2
            skor[0] += 1
        elif (pilihan_komputer == "Batu"):
            hasil = "Seri!"
            komputer_ascii = 0
        else:
            hasil = "Kalah!"
            komputer_ascii = 1
            skor[1] += 1
        user_ascii = 0
    elif (pilihan_user == "kertas"):
        if (pilihan_komputer == "Gunting"):
            hasil = "Kalah!"
            komputer_ascii = 2
            skor[1] += 1
        elif (pilihan_komputer == "Batu"):
            hasil = "Menang!"
            komputer_ascii = 0
            skor[0] += 1
        else:
            hasil = "Seri!"
            komputer_ascii = 1
        user_ascii = 1
    print(f"Pilihan Anda : \n{ascii_tangan[user_ascii]}")
    time.sleep(1)
    print(f"Pilihan Komputer : \n{ascii_tangan[komputer_ascii]}")
    time.sleep(1)
    print(f"Hasil = {hasil}")
    time.sleep(2)
    os.system('cls')
    if (skor[0] == 3 or skor[1] == 3):
        if (skor[0] > skor[1]):
            print(f"Selamat Anda Menang Melawan Komputer")
            Selesai = True
        else:
            print(f"YAhhh!, Kamu kalah sama Komputer! (Cupu banget sih!)")
            Selesai = True
    else:
        #lanjutt
        Selesai = False