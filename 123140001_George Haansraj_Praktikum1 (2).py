import math

def hitung_akar_kuadrat():
    while True:
        try:
            angka = input("Masukkan angka: ")
            angka = float(angka)
            if angka < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
            elif angka == 0:
                raise ValueError("Akar kuadrat dari nol tidak diperbolehkan.")
            else:
                akar = math.sqrt(angka)
                print(f"Akar kuadrat dari {angka} adalah {akar}")
                break
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Input tidak valid. Harap masukkan angka yang valid.")
            
hitung_akar_kuadrat()