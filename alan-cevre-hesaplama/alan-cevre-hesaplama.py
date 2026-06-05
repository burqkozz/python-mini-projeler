# Matematiksel işlemler için math modülü kullanılır
# pi, sqrt, sin, cos, radians gibi işlemler bu modülden alınır
import math


# Kullanıcıdan pozitif sayı almak için kullanılan yardımcı fonksiyon
# Harf, özel karakter, 0 veya negatif sayı girilirse tekrar giriş ister
def pozitif_sayi_al(mesaj):
    while True:
        deger = input(mesaj)

        if not deger.isdigit() or int(deger) <= 0:
            print("\nLütfen pozitif sayı giriniz.")
            continue

        return int(deger)


# Üçgen ile ilgili alan, çevre, Heron, trigonometrik ve dik üçgen hesaplamalarını yapar
def ucgen_alanı():
    while True:
        # Üçgen hesaplama menüsü
        print('''
========== Üçgen Alanı ve Çevre Hesaplama ==========
1. Temel Formül
2. Heron Formülü 
3. Trigonometrik Alan Formülü 
4. Dik Üçgenin Alanı
5. Bir Önceki Sayfaya Dönme 
-----------------------------------------------------
''')
        alan_turu = input("Hangi üçgenin alanını ve çevresini hesaplayacaksınız: ")

        # Menü seçiminin sayı olup olmadığını kontrol eder
        if not alan_turu.isdigit():
            print("\nHarf değil pozitif rakam giriniz.")
            continue
        
        # Kullanıcının geçerli menü seçimi yapmasını sağlar
        if alan_turu not in ["1", "2", "3", "4", "5"]:
            print("\nYanlış üçgen seçimi. Lütfen 1 ile 5 arasında seçim yapınız.")
            continue

        # Üçgen menüsünden ana menüye döner
        if alan_turu == "5":
            print("Üçgen menüsünden bir önceki sayfaya dönülüyor.")
            break

        # Temel üçgen alan formülü: taban * yükseklik / 2
        elif alan_turu == "1":
            taban = pozitif_sayi_al("\nÜçgenin taban uzunluğunu giriniz: ")
            yükseklik = pozitif_sayi_al("Üçgenin yüksekliğini giriniz: ")

            temel_alan_hesaplama = (taban * yükseklik) / 2
            print(f"\nTemel formüle göre üçgenin alanı: {temel_alan_hesaplama:.2f}")

        # Heron formülü ile üçgen alanı ve çevresi hesaplama bölümü
        elif alan_turu == "2":
            while True:
                print('''
========== Heron Formülü Alan ve Çevre Hesaplama ==========
1. Alanı Hesaplama
2. Çevresini Hesaplama
3. Bir Önceki Sayfaya Dönme 
''')
                sec = input("Seçim: ")

                if not sec.isdigit():
                    print("Harf değil pozitif sayı giriniz.")
                    continue

                if sec not in ["1", "2", "3"]:
                    print("Yanlış seçim. Lütfen 1 ile 3 arasından seçim yapınız.")
                    continue

                # Heron menüsünden üçgen menüsüne döner
                if sec == "3":
                    print("Heron menüsünden bir önceki sayfaya dönülüyor.")
                    break

                # Üçgenin üç kenarını kullanıcıdan alır
                kenar1 = pozitif_sayi_al("1. Kenarı giriniz: ")
                kenar2 = pozitif_sayi_al("2. Kenarı giriniz: ")
                kenar3 = pozitif_sayi_al("3. Kenarı giriniz: ")

                # Girilen kenarların üçgen oluşturup oluşturmadığını kontrol eder
                if kenar1 + kenar2 <= kenar3 or kenar1 + kenar3 <= kenar2 or kenar2 + kenar3 <= kenar1:
                    print("\nBu kenarlar bir üçgen oluşturmaz.")
                    continue

                # Heron formülü ile alan hesaplar
                if sec == "1":
                    heron_ucgenin_yarı_cevre = (kenar1 + kenar2 + kenar3) / 2
                    heron_ucgenin_alanı = math.sqrt(
                        heron_ucgenin_yarı_cevre *
                        (heron_ucgenin_yarı_cevre - kenar1) *
                        (heron_ucgenin_yarı_cevre - kenar2) *
                        (heron_ucgenin_yarı_cevre - kenar3)
                    )
                    
                    print(f"\nHeron formülü üçgenin yarı çevresi: {heron_ucgenin_yarı_cevre:.2f}")
                    print(f"Heron formülü üçgenin alanı: {heron_ucgenin_alanı:.2f}")

                # Üç kenarı verilen üçgenin çevresini hesaplar
                elif sec == "2":
                    heron_cevre_hesaplama = kenar1 + kenar2 + kenar3
                    print(f"\nHeron formülü üçgenin çevresi: {heron_cevre_hesaplama:.2f}")

        # Trigonometrik formül ile alan ve çevre hesaplama bölümü
        elif alan_turu == "3":
            while True:
                print('''
========== Trigonometrik Formül Alan ve Çevre Hesaplama ==========
1. Alan
2. Çevre bulma ama 3. kenarı bilinmeyen şekilde
3. Çevre bulma
4. Bir Önceki Sayfaya Dönme 
''')
                sec = input("Seçim: ")

                if not sec.isdigit():
                    print("Sayı giriniz.")
                    continue
                
                if sec not in ["1", "2", "3", "4"]:
                    print("Yanlış seçim. Lütfen 1 ile 4 arasında seçim yapınız.")
                    continue

                # Trigonometrik formül menüsünden üçgen menüsüne döner
                if sec == "4":
                    print("Trigonometrik formül menüsünden bir önceki sayfaya dönülüyor.")
                    break

                # İki kenar ve aradaki açı ile üçgen alanı hesaplar
                if sec == "1":
                    kenar1 = pozitif_sayi_al("1. Kenarı giriniz: ")
                    kenar2 = pozitif_sayi_al("2. Kenarı giriniz: ")

                    alfa = input("Alfa derecesini giriniz: ")

                    if not alfa.isdigit() or int(alfa) <= 0:
                        print("Pozitif sayı giriniz.")
                        continue

                    # Sadece belirli açı değerlerini kabul eder
                    if alfa not in ["30", "45", "60", "90"]:
                        print("Alfa değerini 30, 45, 60 veya 90 derece olarak giriniz.")
                        continue

                    alfa = int(alfa)

                    # math.sin derece değil radyan istediği için derece radyana çevrilir
                    alfa_radyan = math.radians(alfa)

                    trigonometri_üçgen_alanı = 0.5 * kenar1 * kenar2 * math.sin(alfa_radyan)

                    print(f"\nTrigonometri üçgenin alanı: {trigonometri_üçgen_alanı:.2f}")

                # İki kenar ve aradaki açı biliniyorsa üçüncü kenarı bulup çevre hesaplar
                elif sec == "2":
                    kenar1 = pozitif_sayi_al("1. Kenarı giriniz: ")
                    kenar2 = pozitif_sayi_al("2. Kenarı giriniz: ")

                    alfa = input("Alfa derecesini giriniz: ")

                    if not alfa.isdigit() or int(alfa) <= 0:
                        print("Pozitif sayı giriniz.")
                        continue

                    if alfa not in ["30", "45", "60", "90"]:
                        print("Alfa değerini 30, 45, 60 veya 90 derece olarak giriniz.")
                        continue

                    alfa = int(alfa)
                    alfa_radyan = math.radians(alfa)

                    # Kosinüs teoremi ile üçüncü kenar hesaplanır
                    diger_kenar = math.sqrt(
                        kenar1 ** 2 + kenar2 ** 2 - 2 * kenar1 * kenar2 * math.cos(alfa_radyan)
                    )

                    trigonometri_üçgen_cevre = kenar1 + kenar2 + diger_kenar
                    print(f"\nTrigonometri üçgenin çevresi: {trigonometri_üçgen_cevre:.2f}")

                # Üç kenar biliniyorsa çevre hesaplar
                elif sec == "3":
                    kenar1 = pozitif_sayi_al("1. Kenarı giriniz: ")
                    kenar2 = pozitif_sayi_al("2. Kenarı giriniz: ")
                    kenar3 = pozitif_sayi_al("3. Kenarı giriniz: ")

                    # Girilen kenarların üçgen oluşturup oluşturmadığını kontrol eder
                    if kenar1 + kenar2 <= kenar3 or kenar1 + kenar3 <= kenar2 or kenar2 + kenar3 <= kenar1:
                        print("\nBu kenarlar bir üçgen oluşturmaz.")
                        continue

                    trigonometri_üçgen_cevre = kenar1 + kenar2 + kenar3
                    print(f"\nTrigonometri üçgenin çevresi: {trigonometri_üçgen_cevre:.2f}")

        # Dik üçgen alanı, çevresi ve hipotenüs hesaplama bölümü
        elif alan_turu == "4":
            while True:
                print('''
========== Dik Üçgen Alan, Pisagor ve Çevre Hesaplama ==========
1. Alanı
2. Çevresi
3. Pisagor
4. Bir Önceki Sayfaya Dönme 
''')
                sec = input("Seçim: ")

                if not sec.isdigit():
                    print("Harf değil sayı giriniz.")
                    continue

                if sec not in ["1", "2", "3", "4"]:
                    print("Yanlış numara seçimi. Lütfen 1 ile 4 arasında seçiniz.")
                    continue

                # Dik üçgen menüsünden üçgen menüsüne döner
                if sec == "4":
                    print("Dik üçgen menüsünden bir önceki sayfaya dönülüyor.")
                    break

                kenar1 = pozitif_sayi_al("1. Kenarı giriniz: ")
                kenar2 = pozitif_sayi_al("2. Kenarı giriniz: ")

                # Dik üçgende alan: dik kenarların çarpımı / 2
                if sec == "1":
                    dik_üçgen_alan = (kenar1 * kenar2) / 2
                    print(f"\nDik üçgenin alanı: {dik_üçgen_alan:.2f}")

                # Dik üçgende hipotenüs bulunup çevreye eklenir
                elif sec == "2":
                    kenar3 = math.sqrt(kenar1 ** 2 + kenar2 ** 2)
                    dik_üçgen_cevre = kenar1 + kenar2 + kenar3
                    print(f"\nDik üçgenin çevresi: {dik_üçgen_cevre:.2f}")

                # Pisagor teoremi ile hipotenüs hesaplanır
                elif sec == "3":
                    pisagor_bulma = math.sqrt(kenar1 ** 2 + kenar2 ** 2)
                    print(f"\nDik üçgenin hipotenüsü: {pisagor_bulma:.2f}")


# Kare alanı ve çevresini hesaplar
def kare_alanı():
    while True:
        print('''
========== Kare Alanı ve Çevresini Hesaplama ==========
1. Alan Hesaplama
2. Çevre Hesaplama
3. Bir Önceki Sayfaya Dönme 
''')
        
        sec = input("Seçim: ")

        if not sec.isdigit():
            print("\nHarf değil pozitif sayı giriniz.")
            continue

        if sec not in ["1", "2", "3"]:
            print("\nYanlış seçim. 1 ile 3 arasında seçim yapınız.")
            continue

        # Kare menüsünden ana menüye döner
        if sec == "3":
            print("\nBir önceki sayfaya yönlendiriliyorsunuz.")
            break

        kenar1 = pozitif_sayi_al("1. Kenar uzunluğunu giriniz: ")
        kenar2 = pozitif_sayi_al("2. Kenar uzunluğunu giriniz: ")

        # Karede tüm kenarlar eşit olmalıdır
        if kenar1 != kenar2:
            print("\nKarenin kenarları birbirine eşit olmalıdır.")
            continue

        # Karenin alanını hesaplar
        if sec == "1":
            kare_alan = kenar1 * kenar2
            print(f"\nKarenin alanı: {kare_alan:.2f}")

        # Karenin çevresini hesaplar
        elif sec == "2":
            kare_cevre = kenar1 * 4
            print(f"\nKarenin çevresi: {kare_cevre:.2f}")


# Dikdörtgen alanı ve çevresini hesaplar
def dikdörtgen_alanı():
    while True:
        print('''
========== Dikdörtgen Alanı ve Çevresi Hesaplama ==========
1. Alanı Hesaplama
2. Çevresini Hesaplama
3. Bir Önceki Sayfaya Dönme
''')
        sec = input("Seçim: ")

        if not sec.isdigit():
            print("Harf veya özel karakterle seçim yapılamaz. Lütfen pozitif sayı giriniz.")
            continue

        if sec not in ["1", "2", "3"]:
            print("Yanlış seçim numarası girdiniz. Lütfen 1 ile 3 arasında seçim yapınız.")
            continue

        # Dikdörtgen menüsünden ana menüye döner
        if sec == "3":
            print("\nBir önceki sayfaya yönlendiriliyorsunuz.")
            break

        kenar1 = pozitif_sayi_al("1. Kenar uzunluğunu giriniz: ")
        kenar2 = pozitif_sayi_al("2. Kenar uzunluğunu giriniz: ")

        # Dikdörtgenin kenarları eşit olursa kare olur
        if kenar1 == kenar2:
            print("\nDikdörtgenin kenarları birbirine eşit olmamalıdır.")
            continue

        # Dikdörtgen alanını hesaplar
        if sec == "1":
            dikdörtgen_alan = kenar1 * kenar2
            print(f"\nDikdörtgenin alanı: {dikdörtgen_alan:.2f}")

        # Dikdörtgen çevresini hesaplar
        elif sec == "2":
            dikdörtgen_cevre = (kenar1 * 2) + (kenar2 * 2)
            print(f"\nDikdörtgen çevresi: {dikdörtgen_cevre:.2f}")


# Daire, yarım daire, çeyrek daire ve daire halkası hesaplamalarını yapar
def daire_alan():
    while True:
        print('''
========== Daire Alanı ve Çevresi Hesaplama ==========
1. Tam Daire
2. Yarım Daire
3. Çeyrek Daire
4. Daire Halkası
5. Bir Önceki Sayfaya Dön
''')
        sec = input("Seçim: ")

        if not sec.isdigit():
            print("Harf veya özel karakterle seçim yapılamaz. Lütfen pozitif sayı giriniz.")
            continue

        if sec not in ["1", "2", "3", "4", "5"]:
            print("Yanlış numaralı seçim. Lütfen 1 ile 5 arasında seçim yapınız.")
            continue

        # Daire menüsünden ana menüye döner
        if sec == "5":
            print("\nBir önceki sayfaya yönlendiriliyorsunuz.")
            break

        while True:
            print('''
1. Alan
2. Çevre
3. Bir Önceki Sayfaya Dön
''')
            secim = input("Seçim: ")

            if not secim.isdigit():
                print("\nHarf veya özel karakterle seçim yapılamaz. Lütfen pozitif sayı giriniz.")
                continue

            if secim not in ["1", "2", "3"]:
                print("\nYanlış numaralı seçim. Lütfen 1 ile 3 arasında seçim yapınız.")
                continue

            # Alt daire menüsünden üst daire menüsüne döner
            if secim == "3":
                print("\nBir önceki sayfaya yönlendiriliyorsunuz.")
                break

            # Tam, yarım veya çeyrek daire işlemleri
            if sec in ["1", "2", "3"]:
                yarı_çapı = pozitif_sayi_al("Dairenin yarıçapını giriniz: ")

                # Tam daire hesaplama
                if sec == "1":
                    if secim == "1":
                        daire_alanı = math.pi * (yarı_çapı ** 2)
                        print(f"\nDairenin alanı: {daire_alanı:.2f}")

                    elif secim == "2":
                        daire_çevre = 2 * math.pi * yarı_çapı
                        print(f"\nDairenin çevresi: {daire_çevre:.2f}")

                # Yarım daire hesaplama
                elif sec == "2":
                    if secim == "1":
                        yarım_daire_alanı = (math.pi * (yarı_çapı ** 2)) / 2
                        print(f"\nYarım dairenin alanı: {yarım_daire_alanı:.2f}")

                    elif secim == "2":
                        yarım_daire_çevresi = (math.pi * yarı_çapı) + (2 * yarı_çapı)
                        print(f"\nYarım dairenin çevresi: {yarım_daire_çevresi:.2f}")

                # Çeyrek daire hesaplama
                elif sec == "3":
                    if secim == "1":
                        çeyrek_daire_alanı = (math.pi * (yarı_çapı ** 2)) / 4
                        print(f"\nÇeyrek dairenin alanı: {çeyrek_daire_alanı:.2f}")

                    elif secim == "2":
                        çeyrek_daire_çevresi = ((math.pi * yarı_çapı) / 2) + (2 * yarı_çapı)
                        print(f"\nÇeyrek dairenin çevresi: {çeyrek_daire_çevresi:.2f}")

            # Daire halkası hesaplama
            elif sec == "4":
                dış_yarı_çapı = pozitif_sayi_al("\nDış yarıçapını giriniz: ")
                iç_yarı_çapı = pozitif_sayi_al("İç yarıçapını giriniz: ")

                # Dış yarıçap iç yarıçaptan büyük olmalıdır
                if dış_yarı_çapı <= iç_yarı_çapı:
                    print("\nDış yarıçap, iç yarıçaptan büyük olmalıdır.")
                    continue

                # Daire halkası alanını hesaplar
                if secim == "1":
                    daire_halkası_alan = math.pi * ((dış_yarı_çapı ** 2) - (iç_yarı_çapı ** 2))
                    print(f"\nDaire halkasının alanı: {daire_halkası_alan:.2f}")

                # Daire halkası çevresini hesaplar
                elif secim == "2":
                    daire_halkası_çevre = 2 * math.pi * (dış_yarı_çapı + iç_yarı_çapı)
                    print(f"\nDaire halkası çevresi: {daire_halkası_çevre:.2f}")


# Yamuk türlerine göre alan ve çevre hesaplamaları yapar
def yamuk_alan_cevre():
    while True:
        print('''
========== Yamuk Alanı ve Çevresi Hesaplama ==========
1. Sıradan Yamuk
2. İkizkenar Yamuk
3. Dik Yamuk
4. Bir Önceki Sayfaya Dön
''')
        
        sec = input("Seçim: ")

        if not sec.isdigit():
            print("\nHarf veya özel karakterle seçim yapılamaz. Lütfen pozitif sayı giriniz.")
            continue

        if sec not in ["1", "2", "3", "4"]:
            print("\nYanlış numaralı seçim. Lütfen 1 ile 4 arasında seçim yapınız.")
            continue

        # Yamuk menüsünden ana menüye döner
        if sec == "4":
            print("\nBir önceki sayfaya yönlendiriliyorsunuz.")
            break

        while True:
            print('''
1. Alan
2. Çevre
3. Bir Önceki Sayfaya Dön
''')
            secim = input("Seçim: ")

            if not secim.isdigit():
                print("\nHarf veya özel karakterle seçim yapılamaz. Lütfen pozitif sayı giriniz.")
                continue

            if secim not in ["1", "2", "3"]:
                print("\nYanlış numaralı seçim. Lütfen 1 ile 3 arasında seçim yapınız.")
                continue

            # Alt yamuk menüsünden üst yamuk menüsüne döner
            if secim == "3":
                print("\nBir önceki sayfaya yönlendiriliyorsunuz.")
                break

            # Yamuk alanı hesaplama
            if secim == "1":
                alt_taban = pozitif_sayi_al("Alt taban uzunluğunu giriniz: ")
                üst_taban = pozitif_sayi_al("Üst taban uzunluğunu giriniz: ")
                yükseklik = pozitif_sayi_al("Yamuğun yüksekliğini giriniz: ")

                # Yamukta alt ve üst taban aynı olmamalıdır
                if alt_taban == üst_taban:
                    print("\nYamukta alt taban ve üst taban aynı olmamalıdır.")
                    continue

                yamuk_alan = ((alt_taban + üst_taban) / 2) * yükseklik

                if sec == "1":
                    print(f"\nSıradan yamuk alanı: {yamuk_alan:.2f}")

                elif sec == "2":
                    print(f"\nİkizkenar yamuk alanı: {yamuk_alan:.2f}")

                elif sec == "3":
                    print(f"\nDik yamuk alanı: {yamuk_alan:.2f}")

            # Yamuk çevresi hesaplama
            elif secim == "2":
                alt_taban = pozitif_sayi_al("Alt taban uzunluğunu giriniz: ")
                üst_taban = pozitif_sayi_al("Üst taban uzunluğunu giriniz: ")

                if alt_taban == üst_taban:
                    print("\nYamukta alt taban ve üst taban aynı olmamalıdır.")
                    continue

                # Sıradan yamuk çevresi
                if sec == "1":
                    sağ_kenar = pozitif_sayi_al("Yamuğun sağ kenar uzunluğunu giriniz: ")
                    sol_kenar = pozitif_sayi_al("Yamuğun sol kenar uzunluğunu giriniz: ")

                    # Yan kenarlar eşitse bu sıradan yamuk değil, ikizkenar yamuktur
                    if sağ_kenar == sol_kenar:
                        print("\nBu yamuk sıradan değil, ikizkenar yamuktur.")
                        continue

                    sıradan_yamuk_cevre = alt_taban + üst_taban + sağ_kenar + sol_kenar
                    print(f"\nSıradan yamuk çevresi: {sıradan_yamuk_cevre:.2f}")

                # İkizkenar yamuk çevresi
                elif sec == "2":
                    sağ_kenar = pozitif_sayi_al("Yamuğun sağ kenar uzunluğunu giriniz: ")
                    sol_kenar = pozitif_sayi_al("Yamuğun sol kenar uzunluğunu giriniz: ")

                    # İkizkenar yamukta yan kenarlar eşit olmalıdır
                    if sağ_kenar != sol_kenar:
                        print("\nİkizkenar yamukta yan kenarlar birbirine eşit olmak zorundadır.")
                        continue

                    ikizkenar_yamuk_cevre = alt_taban + üst_taban + sağ_kenar + sol_kenar
                    print(f"\nİkizkenar yamuk çevresi: {ikizkenar_yamuk_cevre:.2f}")

                # Dik yamuk çevresi
                elif sec == "3":
                    yükseklik = pozitif_sayi_al("Dik kenar / yükseklik uzunluğunu giriniz: ")

                    # Pisagor ile eğik kenar hesaplanır
                    eğik_kenar = math.sqrt((alt_taban - üst_taban) ** 2 + yükseklik ** 2)

                    dik_yamuk_cevre = alt_taban + üst_taban + yükseklik + eğik_kenar

                    print(f"\nDik yamuk çevresi: {dik_yamuk_cevre:.2f}")


# Programın sürekli çalışmasını sağlayan ana menü döngüsü
while True:
    print('''
========== Alan ve Çevre Hesaplama ==========
1. Üçgen Alanı
2. Kare Alanı
3. Dikdörtgen Alanı
4. Daire Alanı
5. Yamuk Alanı
6. Çıkış       
---------------------------------------------
''')
    
    secim = input("Seçim: ")

    # Kullanıcının harf yerine rakam girmesini kontrol eder
    if not secim.isdigit():
        print("Harf değil pozitif rakam giriniz.")
        continue

    # Kullanıcının geçerli menü seçeneği girip girmediğini kontrol eder
    if secim not in ["1", "2", "3", "4", "5", "6"]:
        print("Yanlış seçim. Lütfen 1 ile 6 arasında seçim yapınız.")
        continue

    # Ana menüden uygulamadan çıkış yapar
    if secim == "6":
        print("Uygulamadan çıkış yapılıyor...")
        break

    # Üçgen hesaplama menüsünü açar
    elif secim == "1":
        ucgen_alanı()

    # Kare hesaplama menüsünü açar
    elif secim == "2":
        kare_alanı()

    # Dikdörtgen hesaplama menüsünü açar
    elif secim == "3":
        dikdörtgen_alanı()

    # Daire hesaplama menüsünü açar
    elif secim == "4":
        daire_alan()

    # Yamuk hesaplama menüsünü açar
    elif secim == "5":
        yamuk_alan_cevre()