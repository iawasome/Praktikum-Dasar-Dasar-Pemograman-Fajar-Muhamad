#My_list = [1,2,3,4,5]
#My_list.append(6)
#Absensi.insert(1, "6")
#print(My_list)
#print(My_list[0])
#print(My_list[4])

#Absensi = ["fajar", "eko", "andhika", "kelvin", "syahrul"]
#Absensi.remove("eko")
#Absensi.pop(2)
#print(Absensi)
#print(Absensi[1])
#print(Absensi[3])

#Total = My_list + Absensi
#print(Total)

#cuaca = input ("Apakah Cuaca Pada Hari Ini? :")
#match cuaca:
    #case "panas":
        #print("kekampus naik motor")
    #case "hujan":
        #print("kekampus naik kereta")
    #case "badai":
        #print("tidak berangkat ke kampus")
    #case _:
        #print("berangkat kekampus")


#1. Buat variabel list dengan value :[namaKendaraan, JenisKendaraan, ccKendaraan, WarnaKendaraan, RodaKendaraan]
#tambahkan dari list tersebut dibelakang dengan value :
#[harga kendaraan, tipe kendaraan]
#tambahkan setelah jenis kendaraan dengan value [MerkKendaraan]

Kendaraan1 = ["Civic", "Mobil","1500 cc", "Hitam", "Roda 4"]
Kendaraan1.append("Rp.799.000.000",)
Kendaraan1.append("Sport Car")
Kendaraan1.insert(2, "Honda")
print(Kendaraan1)

#2. Buat program python dengan match case untuk menghitung luas bangun datar :
#jika pilih 1, maka menghitung luas persegi
#jika pilih 2, maka menghitung luas lingkaran
#jika pilih 3, maka menghitung luas segitiga

Keterangan = '''Selamat datang di aplikasi menghitung luas bangun datar, aplikasi ini dapat melakukan 3 operasi yaitu :
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga
Pilih Operasi :'''

Operasi = input(Keterangan)

match Operasi:
    case "1": 
        Sisi = int(input("Masukan nilai Sisi nya:"))
        Luas_Persegi= Sisi * Sisi
        print("Luas persegi yang sisi-sisinya", Sisi, "adalah", Luas_Persegi)
    case "2":
        P = 3.14
        r = int(input("Masukan Nilai Jari-jari:"))
        Luas_Lingkaran = P * r * r
        print("Luas lingkaran yang jari-jarinya",r, "adalah", Luas_Lingkaran)
    case "3":
        Tinggi = int(input("Masukan Nilai Tinggi:"))
        Alas = int(input("Masukan Nilai Alas:"))
        Luas_Segitiga= 1/2 * Alas * Tinggi
        print("Luas segitiga yang memiliki tinggi", Tinggi, "dan alas", Alas, "adalah", Luas_Segitiga)
    case _:
        print("Tidak ada operasi Yang di pilih")