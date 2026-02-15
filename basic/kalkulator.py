def hitung(angka1, operator, angka2):
    if operator == "+":
        return angka1 + angka2
    elif operator == "-":
        return angka1 - angka2
    elif operator == "*":
        return angka1 * angka2
    elif operator == "/":
        if angka2 != 0:
            return angka1 / angka2
        else:
            return "Error: Tidak bisa dibagi 0"
    else:
        return "Operator tidak valid"


def main():
    print("=== Kalkulator Sederhana ===")

    while True:
        angka1 = input("Masukkan angka pertama (atau q untuk keluar): ")

        if angka1.lower() == "q":
            print("Program selesai.")
            break

        try:
            angka1 = float(angka1)
            operator = input("Masukkan operator (+, -, *, /): ")
            angka2 = float(input("Masukkan angka kedua: "))

            hasil = hitung(angka1, operator, angka2)
            print("Hasil:", hasil)

        except ValueError:
            print("Input harus berupa angka!")

        print("-" * 30)


if __name__ == "__main__":
    main()
