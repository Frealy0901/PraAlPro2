#gaji perjam dan kerja perjam yang diinginkan
gaji    = float(input("gaji perjam yang diinginkan : "))
kerja   = float(input("kerja perjam yang diinginkan : "))
#menghitung pendapatan
pendapatan= gaji *(5*kerja)
#menghitung gaji bersih
gaji_bersih = pendapatan - (pendapatan * 0.14)
#menghitung pembelian aksesoris
beli_aksesoris = gaji_bersih - (gaji_bersih * 0.1)
#membeli alat tulis
alat_tulis = beli_aksesoris -(gaji_bersih * 0.01)
#sedekah
sedehkahkan = alat_tulis - (alat_tulis * 0.25)
#untuk yatim
yatim = ((sedehkahkan * 0.30) // 1000 ) * 100
#untuk anak dhuafa
dhuafa = sedehkahkan * yatim

print("gaji yang yang didapatkan : ", pendapatan)
print("gaji kena pajak : ", gaji_bersih)
print("jumlah uang untuk pakaian : ", beli_aksesoris)
print("jumlah unang untuk alat tulis : ", alat_tulis)
print("uang untuk sedekah : ", sedehkahkan)
print("Sumbangan untuk anak yatim : ", yatim)
print("sedekah untuk dhuafah : ", dhuafa)

