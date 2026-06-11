import json
import datetime


# Verilerin kaydedileceği JSON dosyasının adı
DOSYA_ADI = "butce.json"


# JSON dosyasındaki verileri okuyan fonksiyon
def verileri_yukle():
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            islemler = json.load(dosya)
            return islemler

    # Eğer dosya yoksa boş liste döndürür
    except FileNotFoundError:
        return []

    # Eğer JSON dosyası boş veya bozuksa program hata vermesin diye boş liste döndürür
    except json.JSONDecodeError:
        return []


# İşlem listesini JSON dosyasına kaydeden fonksiyon
def verileri_kaydet(islemler):
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(islemler, dosya, ensure_ascii=False, indent=4)


# Kullanıcının girdiği metinleri arama için düzenleyen fonksiyon
# Büyük/küçük harf ve Türkçe ı/i farkını azaltmak için kullanılır
def metin_duzenle(metin):
    return metin.strip().lower().replace("ı", "i")


# Kullanıcıdan gelir bilgilerini alıp JSON dosyasına kaydeden fonksiyon
def gelir_ekle():
    islemler = verileri_yukle()

    gelir_aciklamasi = input("Gelir açıklaması: ")
    gelir_miktari = input("Gelir miktarı: ")

    # Miktarın sayı olup olmadığını kontrol eder
    if not gelir_miktari.isdigit():
        print("Gelir miktarı pozitif sayı olmalıdır.")
        return

    gelir_miktari = int(gelir_miktari)

    # Miktarın sıfır veya negatif olmamasını kontrol eder
    if gelir_miktari <= 0:
        print("Gelir miktarı sıfır veya negatif olamaz.")
        return

    kategori = input("Kategori: ")

    # Bugünün tarihini otomatik alır
    tarih = datetime.datetime.now().strftime("%Y-%m-%d")

    # Gelir bilgilerini sözlük yapısında oluşturur
    gelir = {
        "tur": "Gelir",
        "aciklama": gelir_aciklamasi,
        "miktar": gelir_miktari,
        "kategori": kategori,
        "tarih": tarih
    }

    # Yeni geliri listeye ekler ve dosyaya kaydeder
    islemler.append(gelir)
    verileri_kaydet(islemler)

    print("Gelir başarıyla eklendi.")


# Kullanıcıdan gider bilgilerini alıp JSON dosyasına kaydeden fonksiyon
def gider_ekle():
    islemler = verileri_yukle()

    aciklama = input("Gider açıklaması: ")
    gider_miktari = input("Gider miktarı: ")

    # Miktarın sayı olup olmadığını kontrol eder
    if not gider_miktari.isdigit():
        print("Gider miktarı pozitif sayı olmalıdır.")
        return

    gider_miktari = int(gider_miktari)

    # Miktarın sıfır veya negatif olmamasını kontrol eder
    if gider_miktari <= 0:
        print("Gider miktarı sıfır veya negatif olamaz.")
        return

    kategori = input("Kategori: ")

    # Bugünün tarihini otomatik alır
    tarih = datetime.datetime.now().strftime("%Y-%m-%d")

    # Gider bilgilerini sözlük yapısında oluşturur
    gider = {
        "tur": "Gider",
        "aciklama": aciklama,
        "miktar": gider_miktari,
        "kategori": kategori,
        "tarih": tarih
    }

    # Yeni gideri listeye ekler ve dosyaya kaydeder
    islemler.append(gider)
    verileri_kaydet(islemler)

    print("\nGider başarıyla eklendi.")


# JSON dosyasındaki tüm gelir ve gider işlemlerini listeleyen fonksiyon
def islemleri_listele():
    islemler = verileri_yukle()

    if len(islemler) == 0:
        print("\nKayıtlı işlem bulunamadı.")
        return

    print("\n========== TÜM İŞLEMLER ==========")

    # enumerate ile işlemleri sıra numarası vererek listeler
    for sira, islem in enumerate(islemler, start=1):
        print(f"{sira}. {islem['tur']} - {islem['aciklama']} - {islem['miktar']} TL - {islem['kategori']} - {islem['tarih']}")


# Kullanıcının girdiği kategoriye göre gelir/gider işlemlerini arayan fonksiyon
def kategoriye_gore_ara():
    islemler = verileri_yukle()

    if len(islemler) == 0:
        print("Kayıtlı işlem bulunamadı.")
        return

    kategori_bilgi = input("Aranacak kategori: ")

    bulundu = False

    print("\n========== ARAMA SONUCU ==========")

    # Tüm işlemler içinde kategori eşleşmesi aranır
    for sira, islem in enumerate(islemler, start=1):
        if metin_duzenle(islem["kategori"]) == metin_duzenle(kategori_bilgi):
            print(f"{sira}. {islem['tur']} - {islem['aciklama']} - {islem['miktar']} TL - {islem['kategori']} - {islem['tarih']}")
            bulundu = True

    # Döngü bittikten sonra hiç sonuç bulunmadıysa mesaj verir
    if bulundu == False:
        print("Aradığınız kategori bulunamadı.")


# Sadece gelir türündeki işlemleri toplayan fonksiyon
def toplam_gelirleri_goster():
    islemler = verileri_yukle()

    if len(islemler) == 0:
        print("\nKayıtlı işlem yok.")
        return

    toplam_gelir = 0

    print("\n========== TOPLAM GELİR ==========")

    # Sadece türü Gelir olan işlemleri toplar
    for sira, islem in enumerate(islemler, start=1):
        if islem["tur"] == "Gelir":
            print(f"{sira}. {islem['tur']} - {islem['aciklama']} - {islem['miktar']} TL - {islem['kategori']} - {islem['tarih']}")
            toplam_gelir += islem["miktar"]

    print(f"\nToplam gelir: {toplam_gelir} TL")


# Sadece gider türündeki işlemleri toplayan fonksiyon
def toplam_giderleri_goster():
    islemler = verileri_yukle()

    if len(islemler) == 0:
        print("Kayıtlı işlem yok.")
        return

    toplam_gider = 0

    print("\n========== TOPLAM GİDER ==========")

    # Sadece türü Gider olan işlemleri toplar
    for sira, islem in enumerate(islemler, start=1):
        if islem["tur"] == "Gider":
            print(f"{sira}. {islem['tur']} - {islem['aciklama']} - {islem['miktar']} TL - {islem['kategori']} - {islem['tarih']}")
            toplam_gider += islem["miktar"]

    print(f"\nToplam gider: {toplam_gider} TL")


# Toplam gelirden toplam gideri çıkararak güncel bakiyeyi gösteren fonksiyon
def guncel_bakiye():
    islemler = verileri_yukle()

    if len(islemler) == 0:
        print("Kayıtlı işlem yok.")
        return

    toplam_gelir = 0
    toplam_gider = 0

    # Gelirleri ve giderleri ayrı ayrı toplar
    for islem in islemler:
        if islem["tur"] == "Gelir":
            toplam_gelir += islem["miktar"]

        elif islem["tur"] == "Gider":
            toplam_gider += islem["miktar"]

    bakiye = toplam_gelir - toplam_gider

    print("\n========== GÜNCEL BAKİYE ==========")
    print(f"Toplam gelir: {toplam_gelir} TL")
    print(f"Toplam gider: {toplam_gider} TL")
    print(f"Güncel bakiye: {bakiye} TL")


# Kullanıcının seçtiği işlemi listeden silen fonksiyon
def islem_sil():
    islemler = verileri_yukle()

    if len(islemler) == 0:
        print("Kayıtlı işlem yok.")
        return

    print("\n========== İŞLEM SİLME ==========")

    # Silinecek işlemi seçebilmek için önce tüm işlemleri listeler
    for sira, islem in enumerate(islemler, start=1):
        print(f"{sira}. {islem['tur']} - {islem['aciklama']} - {islem['miktar']} TL - {islem['kategori']} - {islem['tarih']}")

    silmek = input("\nHangi işlemi silmek istersiniz: ")

    # Kullanıcının sayı girip girmediğini kontrol eder
    if not silmek.isdigit():
        print("Harf veya özel karakterle seçim yapılamaz. Lütfen pozitif sayı giriniz.")
        return

    silmek = int(silmek)

    # Girilen numaranın listedeki işlem sayısı içinde olup olmadığını kontrol eder
    if silmek < 1 or silmek > len(islemler):
        print("Geçersiz işlem numarası seçtiniz.")
        return

    # Kullanıcı 1'den başlattığı için listede silerken 1 çıkarılır
    silinen_islem = islemler.pop(silmek - 1)

    # Güncel liste tekrar JSON dosyasına kaydedilir
    verileri_kaydet(islemler)

    print(f"{silinen_islem['aciklama']} işlemi başarıyla silindi.")


# Ana menü döngüsü
while True:
    print('''
========== BÜTÇE TAKİP UYGULAMASI ==========

1. Gelir ekle
2. Gider ekle
3. Tüm işlemleri listele
4. Kategoriye göre ara
5. Toplam gelirleri göster
6. Toplam giderleri göster
7. Güncel bakiyeyi göster
8. İşlem sil
9. Çıkış
''')

    secim = input("Seçim: ")

    # Seçimin sayı olup olmadığını kontrol eder
    if not secim.isdigit():
        print("\nHarf veya özel karakter olamaz. Lütfen sayı giriniz.")
        continue

    # Menüde olmayan bir sayı girilmesini engeller
    if secim not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("\nHatalı seçim numarası. 1 ile 9 arasında seçim yapınız.")
        continue

    if secim == "9":
        print("\nBütçe takip uygulamasından çıkış yapılıyor.")
        break

    elif secim == "1":
        gelir_ekle()

    elif secim == "2":
        gider_ekle()

    elif secim == "3":
        islemleri_listele()

    elif secim == "4":
        kategoriye_gore_ara()

    elif secim == "5":
        toplam_gelirleri_goster()

    elif secim == "6":
        toplam_giderleri_goster()

    elif secim == "7":
        guncel_bakiye()

    elif secim == "8":
        islem_sil()