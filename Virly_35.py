def ganjil_genap():
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap.")
    else:
        print(f"{angka} adalah bilangan ganjil.")

    while True:
     angka = int(input("Masukkan angka: "))
     if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap.")
     else:
        print(f"{angka} adalah bilangan ganjil.")

def bilangan_prima():
    angka = int(input("Masukkan angka: "))
    if angka < 2:
        print(f"{angka} bukan bilangan prima.")
    else:
        for i in range(2, int(angka ** 0.5) + 1):
            if angka % i == 0:
                print(f"{angka} bukan bilangan prima.")
                break
        else:
            print(f"{angka} adalah bilangan prima.")

    while True:
        angka = int(input("Masukkan angka: "))
        if angka < 2:
            print(f"{angka} bukan bilangan prima.")
        else:
            for i in range(2, int(angka ** 0.5) + 1):
                if angka % i == 0:
                    print(f"{angka} bukan bilangan prima.")
                    break
            else:
                print(f"{angka} adalah bilangan prima.")
