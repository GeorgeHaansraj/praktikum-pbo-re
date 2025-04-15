from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name:
            raise ValueError("Nama hewan tidak boleh kosong.")
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age <= 0:
            raise ValueError("Usia hewan harus lebih dari 0.")
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Guk guk!"

class Cat(Animal):
    def make_sound(self):
        return "Meong!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

def zoo_management():
    daftar_hewan = []
    while True:
        try:
            print("\nMenu Kebun Binatang:")
            print("1. Tambah Hewan")
            print("2. Tampilkan Semua Hewan")
            print("3. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == '1':
                jenis = input("Masukkan jenis hewan (dog/cat/cow): ").lower()
                nama = input("Masukkan nama hewan: ")
                usia = int(input("Masukkan usia hewan: "))

                if jenis == 'dog':
                    hewan = Dog(nama, usia)
                elif jenis == 'cat':
                    hewan = Cat(nama, usia)
                elif jenis == 'cow':
                    hewan = Cow(nama, usia)
                else:
                    raise ValueError("Jenis hewan tidak dikenal.")

                daftar_hewan.append(hewan)
                print(f"Hewan {jenis} bernama {nama} berhasil ditambahkan.")

            elif pilihan == '2':
                if not daftar_hewan:
                    print("Tidak ada hewan dalam daftar.")
                else:
                    print("\nDaftar Hewan:")
                    for h in daftar_hewan:
                        print(f"{h.get_name()} ({h.get_age()} tahun) - Suara: {h.make_sound()}")

            elif pilihan == '3':
                print("Keluar dari sistem kebun binatang.")
                break
            else:
                print("Pilihan tidak valid.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

zoo_management()