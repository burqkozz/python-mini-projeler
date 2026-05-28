# Öğrenci bilgilerini saklamak için boş bir liste oluşturulur
Öğrenciler = []


# Kullanıcıdan öğrenci bilgilerini alır ve listeye ekler
def Öğrenci_ekle():
    ad = input("Öğrenci Adını Giriniz: ")
    soyad = input("Öğrenci Soyadını Giriniz: ")
    sınıf = input("Öğrenci Sınıfını Giriniz: ")
    okulno = int(input("Öğrenci Numarasını Giriniz: "))

    # Öğrenci bilgileri sözlük yapısında tutulur
    öğrenci = {
        "Adınız": ad,
        "Soyadınız": soyad,
        "Sınıfınız": sınıf,
        "Okul Numaranız": okulno
    }

    # Oluşturulan öğrenci bilgisi listeye eklenir
    Öğrenciler.append(öğrenci)
    print("Öğrenci başarıyla eklendi.")


# Kayıtlı tüm öğrencileri ekrana listeler
def öğrencileri_listele():
    if len(Öğrenciler) == 0:
        print("Henüz kayıtlı öğrenci yok.")
    else:
        print("========= Öğrenci Listesi ========")

        # Öğrencileri sıra numarası ile birlikte listeler
        for sira, öğrenci in enumerate(Öğrenciler, start=1):
            print(f"{sira}. Öğrencinin Adı : {öğrenci['Adınız']}")
            print(f"   Soyadı         : {öğrenci['Soyadınız']}")
            print(f"   Sınıfı         : {öğrenci['Sınıfınız']}")
            print(f"   Numarası       : {öğrenci['Okul Numaranız']}")
            print("----------------------------------")


# Kullanıcının girdiği ada veya okul numarasına göre öğrenci arar
def öğrenci_arama():
    arama = input("Aramak istediğiniz öğrenci adını veya numarasını giriniz: ")

    # Başlangıçta öğrenci bulunmadı olarak kabul edilir
    bulundu = False

    # Listedeki öğrencileri tek tek kontrol eder
    for öğrenci in Öğrenciler:
        if arama.lower() in öğrenci["Adınız"].lower() or arama == str(öğrenci["Okul Numaranız"]):

            print("\n========== ARAMA SONUCU ==========")
            print(f"Öğrenci Adı : {öğrenci['Adınız']}")
            print(f"Soyadı      : {öğrenci['Soyadınız']}")
            print(f"Sınıfı      : {öğrenci['Sınıfınız']}")
            print(f"Numarası    : {öğrenci['Okul Numaranız']}")
            print("----------------------------------")

            bulundu = True

    # Döngü bittikten sonra öğrenci bulunamadıysa mesaj verir
    if bulundu == False:
        print("Aradığınız öğrenci bulunamadı.")


# Kullanıcının girdiği okul numarasına göre öğrenciyi siler
def öğrenci_silme():

    # Listede hiç öğrenci yoksa silme işlemi yapılamaz
    if len(Öğrenciler) == 0:
        print("Henüz kayıtlı öğrenci yok. Silme işlemi yapılamaz.")
        return

    silme = int(input("Silmek istediğiniz öğrencinin numarasını giriniz: "))

    # Başlangıçta öğrenci bulunmadı olarak kabul edilir
    delete = False

    # Listedeki öğrenciler tek tek kontrol edilir
    for öğrenci in Öğrenciler:
        if silme == öğrenci["Okul Numaranız"]:
            Öğrenciler.remove(öğrenci)

            print(f"{öğrenci['Adınız']} adlı öğrenci başarıyla silindi")

            delete = True
            break

    # Eğer öğrenci bulunamadıysa bilgi verir
    if delete == False:
        print("Silmek istediğiniz öğrenci bulunamadı.")


# Ana program döngüsü
while True:
    print('''
========== ÖĞRENCİ KAYIT SİSTEMİ ==========

1. Öğrenci ekle
2. Öğrencileri listele
3. Öğrenci ara
4. Öğrenci sil
5. Çıkış   

''')

    # Kullanıcıdan menü seçimi alınır
    secenek = input("Seçiminiz: ")

    # Harf girilmesini engeller
    if not secenek.isdigit():
        print("Lütfen harf değil, sayı giriniz.")
        continue

    # Sadece 1 ile 5 arasında seçim yapılmasını sağlar
    if secenek not in ["1", "2", "3", "4", "5"]:
        print("Hatalı seçim yaptınız. Lütfen 1 ile 5 arasında bir seçim yapınız.")
        continue

    # Kullanıcı 5 seçerse program kapanır
    if secenek == "5":
        print("Programdan çıkış yapılıyor...")
        break

    # Kullanıcı 1 seçerse öğrenci ekleme fonksiyonu çalışır
    elif secenek == "1":
        Öğrenci_ekle()

    # Kullanıcı 2 seçerse öğrenci listeleme fonksiyonu çalışır
    elif secenek == "2":
        öğrencileri_listele()

    # Kullanıcı 3 seçerse öğrenci arama fonksiyonu çalışır
    elif secenek == "3":
        öğrenci_arama()

    # Kullanıcı 4 seçerse öğrenci silme fonksiyonu çalışır
    elif secenek == "4":
        öğrenci_silme()