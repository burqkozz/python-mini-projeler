# Kişileri saklamak için boş bir liste oluşturulur
kisiler = []


# Kullanıcıdan kişi bilgilerini alır ve listeye ekler
def kisi_ekle():
    ad = input("Adınızı giriniz: ")
    soyad = input("Soyadını giriniz: ")
    telefon = input("Telefon numaranızı giriniz: ")
    mail = input("Mailinizi giriniz: ")

    # Telefon numarasının sadece rakamlardan oluşup oluşmadığını kontrol eder
    if not telefon.isdigit():
        print("Telefon numarası harf içeremez.")
        return

    # Kişi bilgileri sözlük yapısında tutulur
    kisi = {
        "Adınız": ad,
        "Soyadınız": soyad,
        "Telefon numaranız": telefon,
        "E-posta adresiniz": mail
    }

    # Oluşturulan kişi sözlüğü kisiler listesine eklenir
    kisiler.append(kisi)
    print("Kişi eklendi.")


# Kayıtlı kişileri ekrana listeler
def kişileri_listele():
    if len(kisiler) == 0:
        print("Henüz kayıtlı kişi yok.")
    
    else:
        print("========== KİŞİ LİSTESİ ==========")

        # Kişileri sıra numarası ile birlikte listeler
        for sira, kisi in enumerate(kisiler, start=1):
            print(f"{sira}. Ad Soyad : {kisi['Adınız']} {kisi['Soyadınız']} ")
            print(f"   Telefon : {kisi['Telefon numaranız']}")
            print(f"   E-posta : {kisi['E-posta adresiniz']}")
            print("----------------------------------")


# Kullanıcının girdiği ad veya telefon numarasına göre kişi arar
def kişi_arama():
    arama = input("Aramak istediğiniz kişinin adını veya telefon numarasını giriniz: ")

    # Kişinin bulunup bulunmadığını kontrol etmek için kullanılır
    bulundu = False

    # Listedeki kişileri tek tek kontrol eder
    for kisi in kisiler:
        if arama.lower() in kisi["Adınız"].lower() or arama == kisi["Telefon numaranız"]:
            print("\n========== ARAMA SONUCU ==========\n")
            print(f"Ad Soyad : {kisi['Adınız']} {kisi['Soyadınız']} ")
            print(f"Telefon  : {kisi['Telefon numaranız']}")
            print(f"E-posta  : {kisi['E-posta adresiniz']}")
            print("----------------------------------")

            bulundu = True

    # Döngü bittikten sonra kişi bulunamadıysa mesaj verir
    if bulundu == False:
        print("Aradığınız kişi bulunamadı.")


# Kullanıcının girdiği telefon numarasına göre kişiyi siler
def kişi_silme():
    if len(kisiler) == 0:
        print("Henüz kayıtlı kişiler yok...")
        return
    
    sil = input("Silinecek olan kişinin telefon numarası: ")

    # Telefon numarasının rakam olup olmadığını kontrol eder
    if not sil.isdigit():
        print("Telefon numarası harf içeremez.")
        return

    bulundu = False

    # Listedeki kişileri tek tek kontrol eder
    for kisi in kisiler:
        if sil == kisi["Telefon numaranız"]:
            kisiler.remove(kisi)
            print(f"\n{kisi['Adınız']} {kisi['Soyadınız']} adlı kişi başarıyla silindi.\n")
            bulundu = True
            break

    # Kişi bulunamazsa kullanıcıya bilgi verir
    if bulundu == False:
        print(f"{sil} numaralı kişi listede yok.")


# Kayıtlı kişinin bilgilerini günceller
def kullanıcı_güncelleme():
    if len(kisiler) == 0:
        print("\nHenüz kayıtlı kişiler yok...\n")
        return

    soru = input("\nGüncellemek istediğiniz kişinin telefon numarasını giriniz: ")

    if not soru.isdigit():
        print("Telefon numarası harf içeremez.")
        return

    bulundu = False

    # Telefon numarasına göre kişi aranır
    for kisi in kisiler:
        if soru == kisi["Telefon numaranız"]:

            print(f"\nKişi bulundu: {kisi['Adınız']} {kisi['Soyadınız']}\n")
           
            while True:
                print('''\nNeyi güncellemek istiyorsunuz?

1. Ad
2. Soyad
3. Telefon numarası
4. E-posta
''')
                
                soru2 = input("Seçiniz: ")

                # Güncelleme seçim kontrolü
                if soru2 not in ["1", "2", "3", "4"]:
                    print("\nHatalı seçim yaptınız 1 ile 4 arasında seçim yapıcaksınız.")
                    continue

                # Ad bilgisini günceller
                if soru2 == "1":
                    yeni_ad = input("Yeni adı giriniz: ")
                    kisi["Adınız"] = yeni_ad
                    print(f"Adı güncellendi: {kisi['Adınız']}")
                    
                # Soyad bilgisini günceller
                elif soru2 == "2":
                    yeni_soyad = input("Yeni soyadı giriniz: ")
                    kisi["Soyadınız"] = yeni_soyad
                    print(f"Soyadı güncellendi: {kisi['Soyadınız']}")

                # Telefon numarasını günceller
                elif soru2 == "3":
                    yeni_telefon = input("Yeni telefon numarasını giriniz: ")

                    if not yeni_telefon.isdigit():
                        print("Telefon numarası harf içeremez.")
                        continue

                    kisi["Telefon numaranız"] = yeni_telefon
                    print(f"Telefon numaranız güncellendi: {kisi['Telefon numaranız']}")
                
                # E-posta adresini günceller
                elif soru2 == "4":
                    yeni_mail = input("Yeni mail adresini giriniz: ")
                    kisi["E-posta adresiniz"] = yeni_mail
                    print(f"Mail adresiniz güncellendi: {kisi['E-posta adresiniz']}")

                bulundu = True
                break

            break

    # Telefon numarasına ait kişi bulunamazsa mesaj verir
    if bulundu == False:
        print("\nBu telefon numarasına ait kişi bulunamadı.\n")


# Programın sürekli çalışmasını sağlayan ana menü döngüsü
while True:
    print('''
========== Telefon Rehberi ==========
1. Kişi Ekle
2. Kişileri Listele
3. Kişi Ara
4. Kişi Sil
5. Kişi Güncelle
6. Çıkış
=====================================
''')

    # Kullanıcıdan menü seçimi alınır
    secim = input("Seçim: ")

    # Harf girilmesini engeller
    if not secim.isdigit():
        print("Harf değil rakam olsun")
        continue

    # Kullanıcının 1 ile 6 arasında seçim yapmasını sağlar
    if secim not in ["1", "2", "3", "4", "5", "6"]:
        print("Hatalı seçim yaptınız. Lütfen 1 ile 6 arasında bir seçim yapınız.")
        continue

    # Kullanıcı 6 seçerse program kapanır
    if secim == "6":
        print("Uygulamadan Çıkış Yapılıyor...")
        break

    # Kişi ekleme fonksiyonunu çalıştırır
    elif secim == "1":
        kisi_ekle()

    # Kişileri listeleme fonksiyonunu çalıştırır
    elif secim == "2":
        kişileri_listele()
    
    # Kişi arama fonksiyonunu çalıştırır
    elif secim == "3":
        kişi_arama()

    # Kişi silme fonksiyonunu çalıştırır
    elif secim == "4":
        kişi_silme()

    # Kişi güncelleme fonksiyonunu çalıştırır
    elif secim == "5":
        kullanıcı_güncelleme()