list_huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

rule = """
1. PROJEK INI HANYA BARU BISA ENCODE/DECODE TEKS BIASA!
2. JANGAN INPUTKAN SIMBOL 
3. KALAU ANDA MENGINPUTKAN HURUF BESAR MAKA AKAN OTOMATIS JADI HURUF KECIL SEMUA 
"""


def encode(text, shift):
    teks = text
    shift = shift
    teks_terkode = ""
    for t in teks:
        if t == " ":
            teks_terkode += " "
        else: 
            posisi_text = list_huruf.index(t)
            updated_index = posisi_text + shift
            teks_terkode += list_huruf[updated_index]
    print(teks_terkode)

def decode(text, shift):
    teks = text
    shift = shift
    terdecode = ""
    for t in teks:
        if t == " ":
            terdecode += " "
        else:
            posisi_text = list_huruf.index(t)
            updated_index = posisi_text - shift
            terdecode += list_huruf[updated_index]
    print(terdecode)

print(logo)
print(rule)
ulangi = True
while ulangi:
    tanya_user = input("Mau pilih encode atau decode? : ")
    if tanya_user == 'encode':
        text_encode = input("Masukkan pesan yang akan di encode : ").lower()
        shift_encode = int(input("Mau maju(shift) berapa ?"))
        encode(text_encode, shift_encode)
    elif tanya_user == 'decode':
        text_decode = input("Masukkan pesan yang akan di decode : ").lower()
        shift_decode = int(input("Mau mundur(shift) berapa ?"))
        decode(text_decode, shift_decode)
    user_ulangi = input("Apakah Anda Ingin Mengulangi Program! (Y/n) : ").lower()
    if user_ulangi == "n":
        print("Terimakasih Telah Menggunakan Program Ini :) 'HAVE A GOOD DAY!' ")
        ulangi = False