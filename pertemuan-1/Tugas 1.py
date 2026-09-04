suku_pertama = 12
beda_kursi = 4
baris_tujuan = 10

jumlah_kursi_ke_n = suku_pertama + (baris_tujuan - 1)*beda_kursi

print("PROGRAM PENENTUAN JUMLAH KURSI AULA (ARITMATIKA)")
print("Data yang diketahui:")
print(f"- Kursi baris pertama (a) : {suku_pertama}")
print(f"- Beda penambahan (b) : {beda_kursi}")
print(f"- Baris yang di cari (n) : {baris_tujuan}")
print("Proses Perhitungan:")
print(f"U_{baris_tujuan} = {suku_pertama} + ({baris_tujuan} - 1) * {beda_kursi}")
print(f"U_{baris_tujuan} = {suku_pertama} + (9*{beda_kursi})")
print(f"U_{baris_tujuan} ={suku_pertama} + 36")
print(f"HASIL AKHIR: jumlah kursi pada baris ke-{baris_tujuan} adalah {jumlah_kursi_ke_n} kursi")