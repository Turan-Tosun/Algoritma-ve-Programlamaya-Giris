def not_ortalamasi_hesapla():
    vize_orani = 0.4
    final_orani = 0.6

    try:
        vize = float(input("Vize notu (0-100): "))
        final = float(input("Final notu (0-100): "))
    except ValueError:
        print("Notlar icin sayisal deger girin.")
        return

    ortalama_100 = vize * vize_orani + final * final_orani
    ortalama_4luk = ortalama_100 / 25

    print(f"Ders ortalamaniz (100'luk): {ortalama_100:.2f}")
    print(f"Ders ortalamaniz (4'luk): {ortalama_4luk:.2f}")


if __name__ == "__main__":
    not_ortalamasi_hesapla()
