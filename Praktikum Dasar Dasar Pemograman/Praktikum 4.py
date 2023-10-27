#1.Buatlah sebuah program python yang menghasilkan milai dari perbandingan 2 variabel
A = 25
B = 5
print(A==B)
print(A!=B)
print(A>B)
print(A<B)
print(A>=B)
print(A<=B)


#2.Buat program python menggunakan if, elif, else untuk konversi suhu
F = float(input("masukan nilai fahrenheit :"))
C = 5/9 * F - 32
print("Nilai konversi dari ",F,"F","ke Celcius adalah",C,"C")
if C<0:
    print("Suhu Dingin")
elif C>0:
    print("Suhu Panas")
else:
    print("Suhu Sangat Dingin atau Sangat Panas")

C = float(input("masukan nilai Celcius :"))
F = 9/5 * C + 32
print("Nilai konversi dari ",C,"C","ke Fahrenheit adalah",F,"F")
if F<32:
    print("Suhu Dingin")
elif F>32:
    print("Suhu Panas")
else:
    print("Suhu Sangat Dingin atau Sangat Panas")
    

#3.Buat program python untuk menampilkan status mahasiswa berdasarkan keaktifannya.
nama_mahasiswa = input("Masukkan nama mahasiswa: ")
keaktifan = input("Masukkan status keaktifan (aktif/tidak aktif/cuti): ")
#bedanya input() hanya mengembalikan string, sedangkan float(input()) mengembalikan nilai desimal yang sesuai dengan masukan pengguna 

if keaktifan == "aktif":
    status = "Mahasiswa aktif"
elif keaktifan == "tidak aktif":
    status = "Mahasiswa tidak aktif"
elif keaktifan == "cuti":
    status = "Mahasiswa sedang cuti"
else:
    status = "Status tidak valid"
#variabel status untuk menyimpan hasil yang sesuai dengan kondisi yang benar pertama kali.
#Setelah blok if, elif, atau else dievaluasi, kita mencetak status. Ini akan mencetak pesan yang sesuai dengan kondisi yang memenuhi, seperti yang diperoleh dari variabel status

print(f"Nama Mahasiswa: {nama_mahasiswa}")
print(f"Status Mahasiswa: {status}")


#4.Buat program python kalkulator sederhana
# Fungsi penjumlahan
def tambah(a, b):
    return a + b

# Fungsi pengurangan
def kurang(a, b):
    return a - b

# Fungsi perkalian
def kali(a, b):
    return a * b

# Fungsi pembagian
def bagi(a, b):
    if b == 0:
        return "Tidak bisa membagi dengan nol"
    return a / b

# Pilihan operasi
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Input pilihan
pilihan = input("Masukkan nomor operasi (1/2/3/4):")

# Input bilangan
bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

if pilihan == '1':
    print("Hasil:", tambah(bilangan1, bilangan2))
elif pilihan == '2':
    print("Hasil:", kurang(bilangan1, bilangan2))
elif pilihan == '3':
    print("Hasil:", kali(bilangan1, bilangan2))
elif pilihan == '4':
    print("Hasil:", bagi(bilangan1, bilangan2))
else:
    print("Pilihan tidak valid")


#dikumpulkan ke email : ridhobigboy@gmail.com