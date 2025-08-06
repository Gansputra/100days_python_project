list_skor = [90,92,99,100,80,85,86,88,75,65]
skor_tertinggi = list_skor[0]
skor_terendahh = list_skor[0]
for i in range(len(list_skor)):
    if skor_tertinggi < list_skor[i]:
        skor_tertinggi = list_skor[i]
    elif skor_terendahh > list_skor[i]:
        skor_terendahh = list_skor[i]

print(f"Skor Tertinggi = {skor_tertinggi}")
print(f"Skor Terendah = {skor_terendahh}")