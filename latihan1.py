import random
from datetime import datetime

# Struktur Data
scoreboard = []

def generate_question():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)

    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def main():
    print("Selamat datang di Kuis Matematika Sederhana!")
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
    print(f"Nama: {name}")
    print(f"Skor: {skor}/5")
    print(f"Waktu: {timestamp}")

if __name__ == "__main__":
    main()

