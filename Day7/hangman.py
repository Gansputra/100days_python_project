import random
import time
import os
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print("+----------------------------+")
print("+   SELAMAT DATANG DI GAME   +")
print("+           HANGMAN          +")
print("+----------------------------+")
print("\n2 detik Menuju Game!")
time.sleep(2)
os.system("cls")

nyawa = 7

list_tebakan = ["apel","mangga","pisang","alpukat"]
tebakan_terpilih = random.choice(list_tebakan)

placeholder = ""
for i in range(len(tebakan_terpilih)):
    placeholder += "_"
print(placeholder)
huruf_tertebak = []
selesai = False
while not selesai:
    tampilkan = ""
    print(f"Nyawa Tersisa {nyawa-1}")
    print(HANGMANPICS[-nyawa])
    tanya_user = input("Masukkan Huruf Tebakan : ")
    if tanya_user not in tebakan_terpilih:
        nyawa -= 1
    for x in tebakan_terpilih:
        if tanya_user == x:
            tampilkan += x
            huruf_tertebak.append(x)
        elif x in huruf_tertebak:
            tampilkan += x
        else:
            tampilkan += "_"
    print(tampilkan)
    if "_" not in tampilkan:
        os.system("cls")
        print(HANGMANPICS[-nyawa])
        print("Selamat Anda Menang!")
        selesai = True
    elif nyawa == 1:
        os.system("cls")
        print(HANGMANPICS[6])
        print("Anda Gagal!")
        print(f"Jawaban yang Benar adalah : {tebakan_terpilih}")
        selesai = True
