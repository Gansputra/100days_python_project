print("INI ADALAH PROGRAM PEMBUAT PASSWORD NGUWAWOR!!")
import random
import os
list_huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_simbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

huruf = int(input("Mau Pakai berapa huruf? : "))
angka = int(input("Mau Pakai berapa angka? : "))
simbol = int(input("Mau Pakai berapa simbol? : "))
os.system("cls")
j_huruf = 0
j_angka = 0
j_simbol = 0
password = ""
for a in range(1, huruf+1):
    j_huruf += 1
    password += random.choice(list_huruf)
for b in range(1, angka+1):
    j_angka += 1
    password += random.choice(list_angka)
for c in range(1, simbol+1):
    j_simbol += 1
    password += random.choice(list_simbol)

print(f"Huruf = {j_huruf}")
print(f"Angka = {j_angka}")
print(f"Simbol = {j_simbol}")
password_teracak = ''.join(random.sample(password, len(password)))
print(f"Password Anda : {password_teracak}")