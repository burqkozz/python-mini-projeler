# Kullanıcıdan görev bilgisi alır ve görevi BEKLEMEDE durumuyla dosyaya kaydeder
def görev_ekle():
    görev_belirleme= input("Görev giriniz: ")

    # Yeni eklenen görevlerin başlangıç durumu
    durum = "BEKLEMEDE"

    # Görevi gorevler.txt dosyasına ekleme modunda kaydeder
    with open("gorevler.txt", "a", encoding="utf-8") as task:
        task.write(f"[{durum}] {görev_belirleme}\n")

        # Eklenen görevi kullanıcıya gösterir
        print(f"\n[{durum}] {görev_belirleme}")
        print(f"Görev başarıyla eklendi.")


# Dosyadaki tüm görevleri ekrana listeler
def görev_listele():
    try:
        # Görevlerin kayıtlı olduğu dosyayı okur
        with open("gorevler.txt", "r", encoding="utf-8") as task:
            görev = task.readlines()

        # Dosya boşsa kullanıcıya bilgi verir
        if len(görev) == 0:
            print("Henüz kayıtlı görev yok.")
            return

        print("========== GÖREV LİSTESİ ==========")

        # Görevleri sıra numarası ile birlikte ekrana yazdırır
        for sira, görevler in enumerate(görev, start=1):
            print(f"{sira}.  {görevler.strip()}")

    # Dosya bulunamazsa hata vermeden mesaj gösterir
    except FileNotFoundError:
        print("Hiçbir görev yok.")


# Kullanıcının girdiği kelimeye göre görev araması yapar
def görev_ara():
    try:
        # Dosyadaki görevleri okur
        with open("gorevler.txt", "r", encoding="utf-8") as task:
            görev = task.readlines()

        # Görev listesi boşsa arama yapılmaz
        if len(görev) == 0:
            print("Görev listesinde hiçbir görev yok.")
            return

        görev_arama = input("Aramak istediğiniz görevi giriniz: ")

        # Aranan görevin bulunup bulunmadığını kontrol etmek için kullanılır
        bulundu = False

        print("========== ARAMA SONUCU ==========")

        # Görevler içinde aranan kelimeyi kontrol eder
        for sira, görevler in enumerate(görev, start=1):
            if görev_arama.lower() in görevler.lower():
                print(f"{sira} {görevler.strip()}")

                bulundu = True

        # Aranan görev bulunamazsa mesaj verir
        if bulundu == False:
                print("Öyle bir görev yok.")

    except FileNotFoundError:
        print("Hiçbir görev yok.")




# Seçilen görevin durumunu TAMAMLANDI olarak değiştirir
def görev_tamamlandı_yapma():
    try:
        # Dosyadaki tüm görevleri okur
        with open("gorevler.txt", "r", encoding="utf-8") as task:
            görevler = task.readlines()

        # Görev yoksa işlem yapılmaz
        if len(görevler) == 0:
            print("Henüz kayıtlı görev yok.")
            return

        print("========== GÖREV LİSTESİ ==========")

        # Görevleri numaralı şekilde listeler
        for sira, görev in enumerate(görevler, start=1):
            print(f"{sira}. {görev.strip()}")

        görev_numarası = input("Tamamlandı yapmak istediğiniz görevin numarasını giriniz: ")

        # Kullanıcının harf yerine rakam girmesini kontrol eder
        if not görev_numarası.isdigit():
            print("Harf değil rakam giriniz.")
            return

        görev_numarası = int(görev_numarası)

        # Girilen görev numarasının geçerli olup olmadığını kontrol eder
        if görev_numarası < 1 or görev_numarası > len(görevler):
            print("Geçersiz görev numarası girdiniz.")
            return

        # Liste indexleri 0'dan başladığı için 1 çıkarılır
        index = görev_numarası - 1

        # Görev zaten tamamlandıysa tekrar işlem yapılmaz
        if "[TAMAMLANDI]" in görevler[index]:
            print("Bu görev zaten tamamlanmış.")
            return

        # Görevin mevcut durumunu TAMAMLANDI olarak değiştirir
        görevler[index] = görevler[index].replace("[beklemede]", "[TAMAMLANDI]")
        görevler[index] = görevler[index].replace("[BEKLEMEDE]", "[TAMAMLANDI]")
        görevler[index] = görevler[index].replace("[yapılıyor]", "[TAMAMLANDI]")
        görevler[index] = görevler[index].replace("[YAPILIYOR]", "[TAMAMLANDI]")

        # Güncellenmiş görev listesini tekrar dosyaya yazar
        with open("gorevler.txt", "w", encoding="utf-8") as task:
            task.writelines(görevler)

        print("\nGörev tamamlandı olarak işaretlendi.")

    except FileNotFoundError:
        print("Hiçbir görev yok.")


# Seçilen görevin durumunu YAPILIYOR olarak değiştirir
def görev_yapılıyor_yapma():
    try:
        # Dosyadaki görevleri okur
        with open("gorevler.txt", "r", encoding="utf-8") as task:
            görevler = task.readlines()

        # Görev yoksa işlem yapılmaz
        if len(görevler) == 0:
            print("Henüz kayıtlı görev yok.")
            return
        
        print("========== GÖREV LİSTESİ ==========")

        # Görevleri numaralı şekilde listeler
        for sira, görev in enumerate(görevler, start=1):
            print(f"{sira}. {görev.strip()}")

        görev_numarası = input("Yapılıyor yapmak istediğiniz görevin numarasını giriniz: ")

        # Kullanıcının sayı girip girmediğini kontrol eder
        if not görev_numarası.isdigit():
            print("Harf değil rakam giriniz.")
            return
        
        görev_numarası = int(görev_numarası)

        # Girilen numaranın görev listesi içinde olup olmadığını kontrol eder
        if görev_numarası < 1 or görev_numarası > len(görevler):
            print("Geçersiz görev numarası girdiniz.")
            return
        
        index = görev_numarası - 1
        
        # Görev zaten yapılıyor durumundaysa tekrar işlem yapılmaz
        if "[YAPILIYOR]" in görevler[index]:
            print("Bu görev zaten yapılıyor.")
            return
        
        # Tamamlanmış görevlerin tekrar yapılıyor yapılmasını engeller
        if "[TAMAMLANDI]" in görevler[index]:
            print("Tamamlanmış görev tekrar yapılıyor yapılamaz.")
            return
        
        # BEKLEMEDE olan görevi YAPILIYOR durumuna çevirir
        görevler[index] = görevler[index].replace("[BEKLEMEDE]", "[YAPILIYOR]")

        # Güncellenmiş görevleri dosyaya tekrar yazar
        with open("gorevler.txt", "w", encoding="utf-8") as task:
            task.writelines(görevler)

        print("\nGörev yapılıyor olarak işaretlendi.")

    except FileNotFoundError:
        print("Henüz görev yok.")


# Seçilen görevin metnini düzenler, durum bilgisini korur
def görev_düzenlenme():
    try:
        # Dosyadaki görevleri okur
        with open("gorevler.txt", "r", encoding="utf-8") as task:
            görevler = task.readlines()

        # Görev listesi boşsa işlem yapılmaz
        if len(görevler) == 0:
            print("Henüz kayıtlı görev yok.")
            return

        # Görevleri numaralı şekilde listeler
        for sira, görev in enumerate(görevler, start=1):
            print(f"{sira}. {görev.strip()}")

        numara_alma = input("Düzenlemek istediğiniz görevin numarasını giriniz: ")

        # Kullanıcının sayı girip girmediğini kontrol eder
        if not numara_alma.isdigit():
            print("Harf değil rakam giriniz.")
            return
        
        numara_alma = int(numara_alma)

        # Girilen görev numarasının geçerli olup olmadığını kontrol eder
        if numara_alma < 1 or numara_alma > len(görevler):
            print("Hatalı görev numarasını girdiniz.")
            return
        
        index = numara_alma - 1

        # Görevin başındaki durum bilgisini alır
        # Örnek: [BEKLEMEDE], [YAPILIYOR], [TAMAMLANDI]
        durum = görevler[index].split("]") [0] + "]"

        yeni_görev_metni = input("Yeni görev metnini giriniz: ")

        # Durumu koruyarak sadece görev metnini değiştirir
        görevler[index] = (f"{durum} {yeni_görev_metni}\n")

        # Güncellenmiş görevleri dosyaya tekrar yazar
        with open("gorevler.txt", "w", encoding="utf-8") as task:
            task.writelines(görevler)

            print(f"{durum} {yeni_görev_metni}")
            print("Görev metni güncellendi")

    except FileNotFoundError:
        print("Henüz kayıtlı görev yok.")
 

# Seçilen görevi dosyadan siler
def görev_silme():
    try:
        # Dosyadaki görevleri okur
        with open("gorevler.txt", "r", encoding="utf-8") as task:
            görev = task.readlines()

        # Görev yoksa silme işlemi yapılmaz
        if len(görev) == 0:
            print("Henüz görev yok.")
            return
        
        print("========== GÖREVLER ==========")

        # Görevleri numaralı şekilde listeler
        for sira, görevler in enumerate(görev, start=1):
            print(f"{sira}. {görevler.strip()}")

        silinicek_olan_görev = input("Silmek istediğiniz görevin numarasını giriniz: ")

        # Kullanıcının sayı girip girmediğini kontrol eder
        if not silinicek_olan_görev.isdigit():
            print("Harf değil rakam giriniz.")

        silinicek_olan_görev = int(silinicek_olan_görev)

        # Girilen görev numarasının geçerli olup olmadığını kontrol eder
        if silinicek_olan_görev < 1 or silinicek_olan_görev > len(görevler):
            print("Geçersiz görev numarasını girdiniz.")
            return
        
        # Seçilen görevi listeden siler
        silinecek_görev = görev.pop(silinicek_olan_görev - 1)
        
        # Güncellenmiş görev listesini dosyaya tekrar yazar
        with open("gorevler.txt", "w", encoding="utf-8") as task:
            task.writelines(görev)

        print(f"\nSilinen görev: {silinecek_görev.strip()}")
        print("Silme işlemi başarılı.")

    except FileNotFoundError:
        print("Henüz görev yok.")


# Programın sürekli çalışmasını sağlayan ana menü döngüsü
while True:
    print('''
========== GÖREV TAKİP UYGULAMASI ==========

1. Görev ekle
2. Görevleri listele
3. Görev ara
4. Görevi yapılıyor yap
5. Görevi tamamlandı yap
6. Görev sil
7. Görev metni düzenleme
8. Çıkış
''')
    
    # Kullanıcıdan menü seçimi alınır
    secim = input("Seçim: ")

    # Harf girilmesini engeller
    if not secim.isdigit():
        print("Harf değil rakam giriniz.")
        continue

    # Kullanıcının geçerli menü seçeneği girip girmediğini kontrol eder
    if secim not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("1 ile 8 arasında seçim yapınız.")
        continue

    # Kullanıcı çıkış seçerse program sonlanır
    if (secim == "8"):
        print("Uygulamadan çıkı yapılıyor...")
        break

    # Görev ekleme fonksiyonunu çalıştırır
    elif (secim == "1"):
        görev_ekle()

    # Görev listeleme fonksiyonunu çalıştırır
    elif (secim == "2"):
        görev_listele()

    # Görev arama fonksiyonunu çalıştırır
    elif (secim == "3"):
        görev_ara()

    # Görevi yapılıyor yapma fonksiyonunu çalıştırır
    elif (secim == "4"):
        görev_yapılıyor_yapma()

    # Görevi tamamlandı yapma fonksiyonunu çalıştırır
    elif (secim == "5"):
        görev_tamamlandı_yapma()

    # Görev silme fonksiyonunu çalıştırır
    elif (secim == "6"):
        görev_silme()

    # Görev metni düzenleme fonksiyonunu çalıştırır
    elif (secim == "7"):
        görev_düzenlenme()