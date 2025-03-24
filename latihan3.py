import random
import statistics
from datetime import datetime

# === PROGRAM 1: Kuis Matematika ===
scoreboard = []

def generate_question():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def kuis_matematika():
    print("\nSelamat datang di Kuis Matematika Sederhana!")
    name = input("Masukkan nama Anda: ")
    skor = 0

    for i in range(5):
        question, answer = generate_question()
        print(f"Soal {i+1}: {question} = ?")
        try:
            user_answer = int(input("Jawaban Anda: "))
            if user_answer == answer:
                print("Benar!\n")
                skor += 1
            else:
                print(f"Salah! Jawaban yang benar: {answer}\n")
        except ValueError:
            print("Input tidak valid. Skor tidak bertambah.\n")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    scoreboard.append({"nama": name, "skor": skor, "waktu": timestamp})

    print("\n=== Skor Anda ===")
    print(f"Nama : {name}")
    print(f"Skor : {skor}/5")
    print(f"Waktu: {timestamp}")


# === PROGRAM 2: Penilaian Mahasiswa ===
def penilaian_mahasiswa():
    mahasiswa = {
        "Hida": [],
        "Ida": [],
        "Citra": [],
        "Abi": [],
        "Aji": []
    }

    for nama in mahasiswa:
        nilai = [random.randint(40, 100) for _ in range(5)]
        mahasiswa[nama] = nilai

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

    print("\nHasil Penilaian Mahasiswa:\n")
    for nama, nilai in mahasiswa.items():
        predikat = hitung_predikat(nilai)
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
        print(f"Rata2   : {statistics.mean(nilai):.2f}")
        print(f"Predikat: {predikat}")
        print("-" * 30)


# === MENU UTAMA ===
def main():
    while True:
        print("\n=== Menu Program ===")
        print("1. Kuis Matematika")
        print("2. Penilaian Mahasiswa")
        print("3. Keluar")

        pilihan = input("Pilih program (1/2/3): ")
        if pilihan == "1":
            kuis_matematika()
        elif pilihan == "2":
            penilaian_mahasiswa()
        elif pilihan == "3":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
