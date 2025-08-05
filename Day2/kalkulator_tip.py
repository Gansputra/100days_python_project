import locale

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

print("Selamat datang di kalkulator tip!")
total_belanja = float(input("Masukkan total belanja Anda: "))
persentase_tip = float(input("Masukkan persentase tip yang diinginkan (dalam %): "))
tip = total_belanja * (persentase_tip / 100)
total_bayar = total_belanja + tip
banyakOrang = int(input("Masukkan jumlah orang yang membayar: "))
total_per_orang = total_bayar / banyakOrang
print("Total yang harus dibayar per orang adalah:", locale.currency(total_per_orang, grouping=True))