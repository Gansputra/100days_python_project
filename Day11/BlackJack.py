import random, os

logo = """
 ________  ___       ________  ________  ___  __               ___  ________  ________  ___  __           
|\   __  \|\  \     |\   __  \|\   ____\|\  \|\  \            |\  \|\   __  \|\   ____\|\  \|\  \         
\ \  \|\ /\ \  \    \ \  \|\  \ \  \___|\ \  \/  /|_          \ \  \ \  \|\  \ \  \___|\ \  \/  /|_       
 \ \   __  \ \  \    \ \   __  \ \  \    \ \   ___  \       __ \ \  \ \   __  \ \  \    \ \   ___  \      
  \ \  \|\  \ \  \____\ \  \ \  \ \  \____\ \  \\ \  \     |\  \\_\  \ \  \ \  \ \  \____\ \  \\ \  \     
   \ \_______\ \_______\ \__\ \__\ \_______\ \__\\ \__\    \ \________\ \__\ \__\ \_______\ \__\\ \__\    
    \|_______|\|_______|\|__|\|__|\|_______|\|__| \|__|     \|________|\|__|\|__|\|_______|\|__| \|__|
"""
print(logo)

list_kartu = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

def tambah_kartu():
    return random.choice(list_kartu)

def hitungTotalKartu(kartu):
    jumlah_kartu = sum(kartu)
    if 11 in kartu and jumlah_kartu > 21:
        kartu.remove(11)
        kartu.append(1)
    return jumlah_kartu

def mulai_game(saldoPemain):
    kartu_user = [tambah_kartu(), tambah_kartu()]
    kartu_bandar = [tambah_kartu(), tambah_kartu()]

    taruhan = int(input("Masukkan Taruhan : "))
    if taruhan < 10:
        print("Minimal Taruhan = 10")
        return saldoPemain
    elif saldoPemain < taruhan:
        print(f"Duit Anda Tidak Cukup! Kurang {taruhan - saldoPemain}")
        return saldoPemain

    game_on = True
    while game_on:
        os.system("cls")
        jumlahKartuUser = hitungTotalKartu(kartu_user)

        print(f"Taruhan = {taruhan}")
        print(f"Kartu Anda = {kartu_user} | Jumlah Kartu Anda : {jumlahKartuUser}\nKartu Bandar = [{kartu_bandar[0]}, ?]")
        
        ulang_tanya_tambah = True
        while ulang_tanya_tambah:
            if jumlahKartuUser == 21:
                print("ANDA MENANG!, BLACKJACK")
                saldoPemain += taruhan
                return saldoPemain
            elif jumlahKartuUser > 21:
                print("Anda Kalah! Jumlah Kartu Anda lebih dari 21 ")
                saldoPemain -= taruhan
                return saldoPemain
            tanya_tambah = input("Apakah Anda Mau Tambah Kartu? (Y/n) : ").lower()
            if tanya_tambah == "y":
                kartu_user.append(tambah_kartu())
                break
            elif tanya_tambah == "n":
                while hitungTotalKartu(kartu_bandar) < 18:
                    kartu_bandar.append(tambah_kartu())
                jumlahKartuBandar = hitungTotalKartu(kartu_bandar)
                print(f"Kartu Anda : {kartu_user} | Total kartu = {jumlahKartuUser}\nKartu Komputer = {kartu_bandar} | Total Kartu = {jumlahKartuBandar}")
                if jumlahKartuBandar == jumlahKartuUser:
                    print("Serii Coi!")
                    return saldoPemain
                elif jumlahKartuBandar == 21:
                    print("Anda Kalah!, Kartu Bandar BlackJack!")
                    saldoPemain -= taruhan
                    return saldoPemain
                elif jumlahKartuBandar > 21:
                    print("Anda Menang!, Jumlah Kartu Bandar Melebihi 21!")
                    saldoPemain += taruhan
                    return saldoPemain
                elif jumlahKartuBandar < jumlahKartuUser:
                    print("Anda Menang! Jumlah Kartu Anda lebih Besar dari Jumlah Kartu Bandar!")
                    saldoPemain += taruhan
                    return saldoPemain
                else:
                    print("Anda Kalah!, Jumlah Kartu Anda lebih Kecil dari Jumlah Kartu Bandar!")
                    saldoPemain -= taruhan
                    return saldoPemain
            else:
                print("Input Tidak Valid!")

    return saldoPemain


saldoPemain = 100
while True:
    print(f"\nSaldo Anda : {saldoPemain}")
    if saldoPemain == 0:
        print("Saldo Anda Habis !, Rungkat Pakcik!\nTerimakasih dah mau main!")
        break
    else:
        tanya_main = input("Main BlackJack? (Y/n) : ").lower()
        if tanya_main == "y":
            saldoPemain = mulai_game(saldoPemain)
        elif tanya_main == "n":
            print("Terimakasih dah mau main!")
            break
        else:
            print("Input Tidak Valid!")
