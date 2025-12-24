 
def main():
    distance = float(input("Gidilecek mesafe (km): "))
    consumption = float(input("100 km'de tuketim (litre): "))
    price = float(input("Yakit litre fiyati: "))
    cost = (distance / 100) * consumption * price
    print(f"Toplam yakit maliyeti: {cost:.2f}")


if __name__ == "__main__":
    main()
