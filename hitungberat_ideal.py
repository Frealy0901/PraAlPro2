print("Underweight <18.5\nNormal 18.5-24.9\nOverweight 25-29.9\nObese 30-39.9\nExtreme Obesity > 40")
bmi = float(input('Berat badan yang diinginkan : '))
tinggi_bdn = float(input ('Tinggi Badan Anda : ',))
tinggi_bdn2 = tinggi_bdn / 100
berat_bdn = round(bmi * tinggi_bdn2 **2)
print("Untuk berat badan yang diinginkan, berat anda harus: ", berat_bdn, "kg")

    

