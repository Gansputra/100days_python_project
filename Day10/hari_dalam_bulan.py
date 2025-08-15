tanya_tahun = int(input("Masukkan Tahun : "))
tanya_bulan = int(input("Masukkan Bulan : "))
def cek_kabisat(tahun):
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def cek_hari(tahun, bulan):
    hari = 0
    if cek_kabisat(tahun=tahun):
        if bulan == 2:
            hari = 29
        elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
            hari = 30
        elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 10 or bulan == 12:
            hari = 31
        else:
            return False
    else:
        if bulan == 2:
            hari = 28
        elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
            hari = 30
        elif bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 10 or bulan == 12:
            hari = 31
        else:
            return False
    print(f"Pada Tahun {tahun} | Bulan {bulan} | Jumlah Hari = {hari}")

if cek_hari(tanya_tahun, tanya_bulan) == False:
    print("Bulan Tidak Valid!")