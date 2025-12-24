def maas_ve_vergi_hesapla():
    tur = input("Brutten nete mi netten brute mi? (B/N): ").strip().lower()
    maas = float(input("Maas tutari: "))
    vergi_orani = float(input("Vergi orani (0-1): "))
    if tur == "n":
        brut = maas / (1 - vergi_orani)
        vergi = brut - maas
        net = maas
    else:
        vergi = maas * vergi_orani
        net = maas - vergi
        brut = maas
    print(f"Brut: {brut:.2f}")
    print(f"Vergi: {vergi:.2f}")
    print(f"Net: {net:.2f}")


if __name__ == "__main__":
    maas_ve_vergi_hesapla()
