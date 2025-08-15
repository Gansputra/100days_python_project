from logo_kalkulator import logo

print(logo)

# def tambah(angka1,angka2):
#     return angka1 + angka2
# def kurang(angka1,angka2):
#     return angka1 - angka2
# def bagi(angka1,angka2):
#     return angka1 / angka2
# def kali(angka1,angka2):
#     return angka1 * angka2
hasil_sementara = 0

def hitung(angka1, angka2, operasi):
    if operasi == "+":
        return angka1 + angka2
    elif operasi == "-":
        return angka1 - angka2
    elif operasi == "/":
        return angka1 / angka2
    elif operasi == "x":
        return angka1 * angka2
    else:
        print("Operasi Tidak Valid!")   

angka1 = float(input("Masukkan Angka pertama : "))
operasi = input("Masukkan Operasi( + atau - atau / atau x ) : ").lower()
angka2 = float(input("Masukkan Angka kedua : "))

hasil1 = hitung(angka1, angka2, operasi)
ulangi = True
while ulangi:
    tanya_user = input(f"Mau meneruskan kalkulasi dengan angka {hasil1} ? (Y/n) : ").lower()
    if tanya_user == "y":
        operasi = input("Masukkan Operasi( + atau - atau / atau x ) : ").lower()
        angka2 = float(input("Masukkan Angka kedua : "))
        hasil2 = hasil1
        hasil1 = hitung(hasil1, angka2, operasi)
        print(f"Hasil dari {hasil2} {operasi} {angka2} = {hasil1}")
    else:
        print("Dadah!, TERIMAKASIH SUDAH MAU COBA PROGRAM INI :)")
        ulangi = False


# if operasi == "+":
#     print(tambah(angka1,angka2))
# elif operasi == "-":
#     print(kurang(angka1,angka2))
# elif operasi == "/":
#     print(bagi(angka1,angka2))
# elif operasi == "x":
#     print(kali(angka1,angka2))
# else:
#     print("Operasi Tidak Valid!")