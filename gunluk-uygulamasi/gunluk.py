# Tarih ve saat işlemleri için datetime modülü kullanılır
import datetime


# Kullanıcının günlük yazısını tarih bilgisiyle birlikte dosyaya kaydeder
def günlük_ekle():
    günlük_ekleme = input("Bugünkü günlük yazınızı giriniz: ")
    
    # Güncel tarihi yıl-ay-gün formatında alır
    tarih_belirleme = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Günlük yazısını gunluk.txt dosyasına ekleme modunda kaydeder
    with open("gunluk.txt" ,"a", encoding="utf-8") as dosya:
        dosya.write(f"{tarih_belirleme} - {günlük_ekleme}\n")

        # Eklenen günlüğü ekrana yazdırır
        print(f"\n{tarih_belirleme} - {günlük_ekleme}")
        print("\nGünlük başarılı şekilde oluşturuldu.")


# Dosyaya kaydedilmiş tüm günlükleri ekrana listeler
def günlük_listele():
    try:
        # Günlük dosyasını okuma modunda açar
        with open("gunluk.txt", "r", encoding="utf-8") as dosya:
            günlük = dosya.readlines()

            # Dosyada hiç günlük yoksa kullanıcıya bilgi verir
            if len(günlük) == 0:
                print("Henüz kayıtlı günlük yok.")
                return

            print("========== GÜNLÜKLER ==========")

            # Günlükleri sıra numarası ile ekrana yazdırır
            for sira, günlükler in enumerate(günlük, start=1):
                print(f"{sira}. {günlükler.strip()}")

    # Dosya yoksa hata vermeden kullanıcıya mesaj gösterir
    except FileNotFoundError:
        print("Hiçbir günlük yok.")


# Kullanıcının girdiği kelimeyi günlükler içinde arar
def günlük_ara():
    try: 
        # Günlük dosyasındaki tüm satırları okur
        with open("gunluk.txt", "r", encoding="utf-8") as dosya:
            günlük = dosya.readlines()

        # Dosya boşsa arama işlemini durdurur
        if len(günlük) == 0:
            print("Henüz kayıtlı günlük yok.")
            return
        
        arama = input("Aramak istediğiniz kelimeyi giriniz: ")

        # Aranan kelimenin bulunup bulunmadığını kontrol etmek için kullanılır
        bulundu = False

        print("========== ARAMA SONUCU ==========")

        # Günlüklerin içinde aranan kelime var mı diye kontrol eder
        for sira,günlükler in enumerate(günlük, start=1):
            if arama.lower() in günlükler.lower():
                print(f"{sira}. {günlükler.strip()}")
                bulundu = True

        if bulundu == False:
            print("Aradığınız kelimeye ait günlük bulunamadı.")

    # Dosya bulunamazsa kullanıcıya bilgi verir
    except FileNotFoundError:
        print("Henüz günlük kaydı yok.")


# Kullanıcının seçtiği günlüğü dosyadan siler
def günlük_sil():
    try:
        # Günlük dosyasındaki tüm kayıtları liste olarak okur
        with open("gunluk.txt", "r", encoding="utf-8") as dosya:
            günlük = dosya.readlines()

        # Silinecek günlük yoksa işlemi durdurur
        if len(günlük) == 0:
            print("Henüz kayıtlı günlük yok.")
            return
        
        print("========== GÜNLÜKLER ==========")

        # Günlükleri numaralı şekilde ekrana yazdırır
        for sira, günlükler in enumerate(günlük, start=1):
            print(f"{sira}. {günlükler.strip()}")

        secim = input("\nSilmek istediğiniz günlük numarasını giriniz: ")

        # Kullanıcının sayı girip girmediğini kontrol eder
        if not secim.isdigit():
            print("Lütfen harf değil, sayı giriniz.")
            return
        
        secim = int(secim)

        # Girilen numaranın geçerli olup olmadığını kontrol eder
        if secim < 1 or secim > len(günlük):
            print("Geçersiz not numarası girdiniz.")
            return
        
        # Seçilen günlüğü listeden siler
        silinecek_günlük = günlük.pop(secim - 1)

        # Güncellenmiş günlük listesini dosyaya tekrar yazar
        with open("gunluk.txt", "w", encoding="utf-8") as dosya:
            dosya.writelines(günlük)

        print(f"\nSilinen günlük: {silinecek_günlük.strip()}")
        print("Günlük başarıyla silindi.")

    # Dosya yoksa kullanıcıya bilgi verir
    except FileNotFoundError:
        print("Henüz kayıtlı günlük yok.")


# Programın sürekli çalışmasını sağlayan ana menü döngüsü
while True:
    print('''
========== Günlük Uygulaması ==========
          
1. Günlük Ekle
2. Günlük Listele
3. Günlük Ara
4. Günlük Sil
5. Çıkış
''')
    
    secim = input("Seçim: ")

    # Menü seçiminin rakam olup olmadığını kontrol eder
    if not secim.isdigit():
        print("Harf değil rakam giriniz.")
        continue

    # Kullanıcının 1 ile 5 arasında seçim yapmasını sağlar
    if secim not in ["1", "2", "3", "4", "5"]:
        print("1 ile 5 arasında rakam giriniz.")
        continue

    # Programdan çıkış yapar
    if (secim == "5"):
        print("Uygulamadan çıkış yapılıyor...")
        break

    # Günlük ekleme fonksiyonunu çalıştırır
    elif (secim == "1"):
        günlük_ekle()

    # Günlük listeleme fonksiyonunu çalıştırır
    elif (secim == "2"):
        günlük_listele()

    # Günlük arama fonksiyonunu çalıştırır
    elif (secim == "3"):
        günlük_ara()

    # Günlük silme fonksiyonunu çalıştırır
    elif (secim == "4"):
        günlük_sil()