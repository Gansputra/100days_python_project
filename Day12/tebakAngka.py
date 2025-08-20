from logo import logo
import random, os, time

print(logo)
angka_tebakan = random.randrange(1, 101, 1)

def kesulitan():
    while True:
        tanya_kesulitan = input("Mau Coba Tingkat Kesulitan yang apa? (EASY,MEDIUM,HARD,HOKI) : ").lower()
        if tanya_kesulitan == "easy":
            return 10
        elif tanya_kesulitan == "medium":
            return 7
        elif tanya_kesulitan == "hard":
            return 5
        elif tanya_kesulitan == "hoki":
            return 1
        else:
            print("Input Tidak Valid!")
def mulai_game():
    kesempatan_menebak = kesulitan()
    time.sleep(1)
    os.system("cls")
    print(f"Kesempatan menebakmu : {kesempatan_menebak}")
    print("Okee!, Saya sedang memikirkan angka dari 1-100, Tebaklah!")
    while True:
        try:
            print(f"Kesempatan menebakmu : {kesempatan_menebak}")
            if kesempatan_menebak == 0:
                print("Kesempatanmu Untuk Menebak Sudah Habis! | Nice Try!")
                return
            tebakan = int(input("Masukkan Tebakan : "))
            if tebakan == angka_tebakan:
                print("Angka Tebakanmu Benar!")
                return
            elif tebakan > angka_tebakan:
                print("Angka Tebakanmu Ketinggian | Tebak Lagi!")
                kesempatan_menebak -= 1
            elif tebakan < angka_tebakan:
                print("Angka Tebakanmu Terlalu Rendah | Tebak Lagi!")
                kesempatan_menebak -= 1
        except ValueError:
            print("INPUT HARUS BERUPA ANGKA BRO!")
        
        
game_on = True
while game_on:
    tanya_main = input("Mau main game tebak angka?(Y/n) : ").lower()
    if tanya_main == 'y':
        mulai_game()
    elif tanya_main == 'n':
        print("Terimakasih Sudah Main Game ini! :)")
        game_on = False