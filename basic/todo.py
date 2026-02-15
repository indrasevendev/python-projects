import json
import os

def tampilkan_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Tambah Task")
    print("2. Lihat Task")
    print("3. Hapus Task")
    print("4. Keluar")

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def main():
    tasks = load_tasks()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            task = input("Masukkan task baru: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task ditambahkan.")

        elif pilihan == "2":
            if not tasks:
                print("Belum ada task.")
            else:
                print("\nDaftar Task:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif pilihan == "3":
            if not tasks:
                print("Tidak ada task untuk dihapus.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                try:
                    index = int(input("Pilih nomor task yang dihapus: "))
                    tasks.pop(index - 1)
                    save_tasks(tasks)
                    print("Task dihapus.")
                except (ValueError, IndexError):
                    print("Input tidak valid.")

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
