# Girilen sayının pozitif, negatif veya sıfır olduğunu kontrol eder
def pozitif(sayi):
    if sayi < 0:
        return "Sayı negatif"
    elif sayi == 0:
        return "Sayı sıfır"
    else:
        return "Sayı pozitif"


# Girilen sayının çift mi tek mi olduğunu kontrol eder
def çiftmi(sayi):
    if sayi % 2 == 0:
        return "Sayı çift"
    else:
        return "Sayı Tek"


# Kullanıcıdan kontrol edilecek sayıyı alır
result = int(input("Bir sayı giriniz: "))


# Sayının pozitif, negatif veya sıfır durumunu ekrana yazdırır
print(pozitif(result))

# Sayının çift/tek durumunu ekrana yazdırır
print(çiftmi(result))