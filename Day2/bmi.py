tinggi = input("Masukkan tinggi badan Anda (dalam cm): ")
berat = input("Masukkan berat badan Anda (dalam kg): ")
#rumus BMI
tinggi_m = float(tinggi) / 100
bmi = float(berat) / (tinggi_m ** 2)
rounded_bmi = round(bmi, 2)
print("Indeks Massa Tubuh (BMI) Anda adalah:", rounded_bmi)