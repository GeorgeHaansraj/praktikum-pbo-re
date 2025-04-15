def todo_list():
    tugas = []
    while True:
        try:
            print("\nPilih aksi:")
            print("1. Tambah tugas")
            print("2. Hapus tugas")
            print("3. Tampilkan daftar tugas")
            print("4. Keluar")
            pilihan = input("Masukkan pilihan (1/2/3/4): ")

            if pilihan == '1':
                deskripsi = input("Masukkan tugas yang ingin ditambahkan: ").strip()
                if not deskripsi:
                    raise ValueError("Tugas tidak boleh kosong.")
                tugas.append(deskripsi)
                print("Tugas berhasil ditambahkan!")

            elif pilihan == '2':
                if not tugas:
                    print("Daftar tugas kosong.")
                    continue
                for i, t in enumerate(tugas, 1):
                    print(f"{i}. {t}")
                idx = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                if idx < 1 or idx > len(tugas):
                    raise IndexError(f"Tugas dengan nomor {idx} tidak ditemukan.")
                tugas.pop(idx - 1)
                print("Tugas berhasil dihapus!")

            elif pilihan == '3':
                print("Daftar Tugas:")
                if not tugas:
                    print("- Tidak ada tugas.")
                else:
                    for t in tugas:
                        print(f"- {t}")

            elif pilihan == '4':
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid.")

        except ValueError as e:
            print(f"Error: {e}")
        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            
todo_list()