#MEMBUAT ARRAY KOSONG
DATA_NILAI= []
JUMLAH_KELAS = int (input("masukkan jumlah kelas : "))

for i in range (jumlah_kelas):
  print(f"\nmahasiswa ke- {i+1}")

  tugas= float(input("nilai tugas: "))
  uts = float(input("nilai uts :  "))
  uas = float (input ("nilai uas : "))
  #simpan kelas ke dalam array 2D
  kelas.append([tugas,uts,uas])

  #simpan kelas ke dalam array 3D
data_nilai.append(kelas)

print("\n===== DATA NILAI SEMUA KELAS =====")

for k in range (len/(data_nilai))
     print(f"nkelas ke- {kelas+1} ")
     for i in range (len(data_nilai[k])):
         print(f" Mahasiswa ke_{i+1}")
         print("   Tugas:", data_nilai[k][i][0])
         print("   UTS  :", data_nilai[k][i][1])
         print("   UAS  :", data_nilai[k][i][2])
       
  
