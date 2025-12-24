import sys


def main() -> None:
    try:
        consumption = float(input("Aylik tuketim (kWh): "))
        energy_unit = float(input("Enerji birim fiyati (TL/kWh): "))
        distribution_unit = float(input("Dagitim bedeli (TL/kWh): "))
        tax_percent = float(input("Vergi orani (%): "))
    except ValueError:
        print("Lutfen sayisal deger girin.")
        return

    energy_cost = consumption * energy_unit
    distribution_cost = consumption * distribution_unit
    subtotal = energy_cost + distribution_cost
    tax = subtotal * (tax_percent / 100)
    total = subtotal + tax

    print("\n--- Fatura Ozeti ---")
    print(f"Enerji tutari     : {energy_cost:.2f} TL")
    print(f"Dagitim tutari    : {distribution_cost:.2f} TL")
    print(f"Vergi tutari      : {tax:.2f} TL")
    print(f"Toplam fatura     : {total:.2f} TL")


if __name__ == "__main__":
    main()
