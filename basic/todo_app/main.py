from todo import TodoApp


def main():
    app = TodoApp()

    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Tambah Task")
        print("2. Lihat Task")
        print("3. Hapus Task")
        print("4. Toggle Status")
        print("5. Keluar")

        choice = input("Pilih menu (1-5): ")

        if choice == "1":
            title = input("Masukkan task: ")
            app.add_task(title)

        elif choice == "2":
            app.view_tasks()

        elif choice == "3":
            app.view_tasks()
            try:
                index = int(input("Pilih nomor task yang dihapus: "))
                app.delete_task(index)
            except ValueError:
                print("Masukkan angka yang valid.")

        elif choice == "4":
            app.view_tasks()
            try:
                index = int(input("Pilih nomor task yang diubah statusnya: "))
                app.toggle_task(index)
            except ValueError:
                print("Masukkan angka yang valid.")

        elif choice == "5":
            print("Keluar dari aplikasi.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
