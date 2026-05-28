# Kullanıcının yazdığı notu notlar.txt dosyasına kaydeder
def not_ekle():
    notu=input("Notunuzu yazınız: ")

    # Dosyayı ekleme modunda açar ve yeni notu en alta ekler
    with open("notlar.txt", "a", encoding="utf-8" )as dosya:
        dosya.write(notu + "\n")

    print("\nNot başarıyla kaydedildi.")



# notlar.txt dosyasındaki tüm notları ekrana numaralı şekilde listeler
def not_listele():

    try:
        # Dosyadaki bütün notları satır satır okur
        with open("notlar.txt", "r", encoding="utf-8")as dosya:
            notlar = dosya.readlines()

        # Dosya boşsa kullanıcıya bilgi verir
        if len(notlar) == 0:
            print("Henüz kayıtlı not yok. ")
            return
    
        print("\n========== NOTLAR ==========")

        # Notları sıra numarası ile birlikte ekrana yazdırır
        for sira, notu in enumerate(notlar, start=1):
        
            print(f"{sira}. {notu.strip()}")

    # Eğer notlar.txt dosyası yoksa hata vermeden mesaj gösterir
    except FileNotFoundError:
        print("Henüz kayıtlı not yok.")


# Kullanıcının girdiği kelimeyi kayıtlı notların içinde arar
def not_ara():

    try:
        # Dosyadaki notları okur
        with open("notlar.txt", "r", encoding="utf-8")as dosya:
            notlar = dosya.readlines()

        arama = input("Aramak istediğiniz kelimeyi giriniz: ")

        # Aranan kelimenin bulunup bulunmadığını kontrol etmek için kullanılır
        bulundu = False

        # Her notun içinde aranan kelime var mı diye kontrol eder
        for notu in notlar:
            if arama.lower() in notu.lower():
                print("\n" + notu.strip())
                bulundu = True

        if bulundu == False:
            print("Aradığınız not bulunamadı.")

    # Eğer dosya yoksa kullanıcıya bilgi verir
    except FileNotFoundError:
        print("Henüz kayıtlı not yok.")


# Kullanıcının seçtiği notu dosyadan siler
def not_sil():
    try:
        # Dosyadaki tüm notları liste olarak okur
        with open("notlar.txt", "r", encoding="utf-8") as dosya:
            notlar = dosya.readlines()

        # Silinecek not yoksa işlemi durdurur
        if len(notlar) == 0:
            print("Henüz kayıtlı not yok. Silme işlemi yapılamaz.")
            return

        print("\n========== NOTLAR ==========")

        # Notları numaralı şekilde ekrana yazdırır
        for sira, notu in enumerate(notlar, start=1):
            print(f"{sira}. {notu.strip()}")

        secim = input("\nSilmek istediğiniz notun numarasını giriniz: ")

        # Kullanıcının harf yerine sayı girmesini kontrol eder
        if not secim.isdigit():
            print("Lütfen harf değil, sayı giriniz.")
            return

        secim = int(secim)

        # Girilen numaranın listedeki not numaraları arasında olup olmadığını kontrol eder
        if secim < 1 or secim > len(notlar):
            print("Geçersiz not numarası girdiniz.")
            return

        # Seçilen notu listeden siler
        silinen_not = notlar.pop(secim - 1)

        # Güncellenmiş not listesini dosyaya tekrar yazar
        with open("notlar.txt", "w", encoding="utf-8") as dosya:
            dosya.writelines(notlar)

        print(f"\nSilinen not: {silinen_not.strip()}")
        print("Not başarıyla silindi.")

    # Dosya bulunamazsa kullanıcıya bilgi verir
    except FileNotFoundError:
        print("Henüz kayıtlı not yok.")


# Programın sürekli çalışmasını sağlayan ana menü döngüsü
while True:
    print('''
========== NOT DEFTERİ ==========

1. Not ekle
2. Notları listele
3. Not ara
4. Not sil
5. Çıkış
''')
    
    secim=input("Seçim: ")

    # Menü seçiminin rakam olup olmadığını kontrol eder
    if not secim.isdigit():
        print("Yanlış girdiniz rakam formatında girmeniz gerekli.")
        continue 
    
    # Kullanıcının 1 ile 5 arasında seçim yapmasını sağlar
    if secim not in ["1", "2" ,"3", "4", "5"]:
        print("Lütfen 1 ile 5 arasında rakam giriniz.")
        continue

    # Programdan çıkış yapar
    if (secim == "5"):
        print("Uygulamadan çıkış yapılıyor...")
        break

    # Not ekleme fonksiyonunu çalıştırır
    elif (secim == "1"):
        not_ekle()

    # Not listeleme fonksiyonunu çalıştırır
    elif (secim == "2"):
        not_listele()

    # Not arama fonksiyonunu çalıştırır
    elif (secim == "3"):
        not_ara()

    # Not silme fonksiyonunu çalıştırır
    elif (secim == "4"):
        not_sil()