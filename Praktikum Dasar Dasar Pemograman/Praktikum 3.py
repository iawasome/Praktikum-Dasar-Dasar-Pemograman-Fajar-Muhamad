#1. Buatlah program python untuk menuliskan profil pribadi (nama, nim, kelas, no telp, alamat) menggunakan variabel dan di cetak (print)
Nama = "Fajar Muhamad"
Nim = "0110223078"
Kelas = "TI02"
No_telpon = "081319941507"
Alamat = '''Perumahan Villa Permata Mas 2 Blok AK no 20 RT 05/RW 01 Desa Cikuda, Kec. Gunung Putri, Kab. Bogor, Jawa Barat 16370'''

print(Nama)
print(Nim)
print(Kelas)
print(No_telpon)
print(Alamat)

#2. buat seperti no 1 tapi 1 nama teman kalian 
Nama2 = "Muhammad Andhika Thatha"
Nim2 = "0110223053"
Kelas2 = "TI02"
No_telpon2 = "085157634427"
Alamat2 = '''Jalan RH Panji, Kontrakan Griya Bunda Dewi 1 Rumah No.1  RT 03/RW 04 Kp. Masjid Desa Bojonggede Kec. Bojonggede Kab. Bogor,Jawa Barat 16922'''

print(Nama2)
print(Nim2)
print(Kelas2)
print(No_telpon2)
print(Alamat2)

#3. buat program python untuk mencari nilai berat badan ideal Rumus([tinggi badan (sentimeter) – 100] – [(tinggi badan (sentimeter) – 100) x 10 persen])
Tinggi_Badan = float(input("masukan nilai Tinggi_badan :"))
Rumus = (Tinggi_Badan - 100) - (Tinggi_Badan - 100) * 10/100

print("Berat Badan Ideal untuk pria dengan tinggi badan", Tinggi_Badan, "cm","adalah", Rumus, "kg")      

#4. buat program python untuk mencari nilai konversi dari celcius ke fahreinheit
C = float(input("masukan nilai celcius :"))
F = 9/5 * C - 32

print("Nilai konversi dari ",C,"C","ke fahrenheit adalah",F,"F")

#5. buat program python untuk mencari luas dan keliling tabung.
r = float(input("masukan nilai jari-jari :"))
t = float(input("masukan nilai tinggi :"))
P = 3.14
K = 2 * P * r
L = 2 * P * r * (r + t)

print("keliling dari tabung adalah", K,"cm")
print("Luas permukaan dari tabung adalah", L, "cm")