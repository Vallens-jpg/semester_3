# Struktur data linier

#List
buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
print(buah)

#Tuple
buah_buahan = ("apel", "jeruk", "mangga")
#buah_buahan.append("pisang") # akan error karena tuple immnutable
print(buah_buahan)

#Set
buah_buahan_1 = {"apel", "jeruk", "mangga"}
buah_buahan_1.add("pisang")
print(buah_buahan_1)

#Dict
elektronik = {
    "kipas angin" : 30,
    "TV": 40,
    "rice cooker": 120
}
print(elektronik)

elektronik["heater"] = 20
elektronik["TV"] = 20
print(elektronik)

teks = "hello"
teks = "world"
print(teks)
print(teks[0])

mahasiswa = {"nama": "Budi", "umur": 20}
print(mahasiswa["umur"])

#Input
nilai_a = int(input("Masukkan nilai anda: "))
nilai_b = int(input("Masukkan nilai anda: "))

hasil = nilai_a + nilai_b
print(hasil)
print(hasil // 2)


