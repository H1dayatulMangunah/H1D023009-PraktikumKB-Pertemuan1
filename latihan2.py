import random
import statistics

# Daftar mahasiswa dan nilai
mahasiswa = {
    "Hida": [],
    "Ida": [],
    "Citra": [],
    "Abi": [],
    "Aji": []
}

# Mengisi nilai secara acak
for nama in mahasiswa:
    nilai = [random.randint(40, 100) for _ in range(5)]  # 5 mata kuliah
    mahasiswa[nama] = nilai

# Fungsi menghitung rata-rata dan predikat
def hitung_predikat(nilai):
    rata2 = statistics.mean(nilai)
    if rata2 >= 90:
        return "A"
    elif rata2 >= 80:
        return "B"
    elif rata2 >= 70:
        return "C"
    else:
        return "D"

# Menampilkan hasil
print("Hasil Penilaian Mahasiswa:\n")
for nama, nilai in mahasiswa.items():
    predikat = hitung_predikat(nilai)
    print(f"Nama    : {nama}")
    print(f"Nilai   : {nilai}")
    print(f"Rata2   : {statistics.mean(nilai):.2f}")
    print(f"Predikat: {predikat}")
    print("-" * 30)