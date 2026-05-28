# Kitapları saklamak için boş bir liste oluşturuyoruz.
# Eklenen her kitap bu listenin içine eklenecek.
kitaplar = []


# Bu fonksiyon kullanıcıdan kitap bilgilerini alır
# ve kitaplar listesine yeni kitap ekler.
def kitap_ekle():
    ad = input("Kitabın Adını Giriniz: ")
    yazar = input("Kitabın Yazarı Kimdir: ")
    sayfa = input("Kitap Kaç Sayfa: ")

    if not sayfa.isdigit() or int(sayfa) <= 0:
        print("Harf ve sıfır değil pozitif sayı giriniz.")
        return

    sayfa = int(sayfa) 

    # Kitap bilgilerini sözlük yapısında tutuyoruz.
    # Her kitapta ad, yazar ve sayfa bilgisi olacak.
    kitap = {
        "ad": ad,
        "yazar": yazar,
        "sayfa": sayfa
    }

    # Oluşturulan kitap sözlüğünü kitaplar listesine ekliyoruz.
    kitaplar.append(kitap)

    print("Kitap başarıyla eklendi.")


# Bu fonksiyon eklenen bütün kitapları ekrana listeler.
def kitaplari_listele():

    # Eğer kitaplar listesinin uzunluğu 0 ise hiç kitap eklenmemiş demektir.
    if len(kitaplar) == 0:
        print("Henüz kayıtlı kitap yok.")

    else:
        print("\n========== KİTAP LİSTESİ ==========\n")

        # enumerate burada kitaplara sıra numarası vermek için kullanılır.
        # start=1 dediğimiz için sıralama 1'den başlar.
        for sira, kitap in enumerate(kitaplar, start=1):

            # Her kitabın bilgilerini alt alta yazdırıyoruz.
            print(f"{sira}. Kitap Adı : {kitap['ad']}")
            print(f"   Yazar     : {kitap['yazar']}")
            print(f"   Sayfa     : {kitap['sayfa']}")
            print("----------------------------------")


# Bu fonksiyon kullanıcının girdiği kitap adına göre kitap arar.
def kitap_ara():
    aranan = input("Aramak istediğiniz kitap adını giriniz: ")

    # Başta kitabın bulunmadığını kabul ediyoruz.
    # Kitap bulunursa bunu True yapacağız.
    bulundu = False

    # Kitaplar listesindeki bütün kitapları tek tek geziyoruz.
    for kitap in kitaplar:

        # lower() büyük-küçük harf farkını kaldırır.
        # Kullanıcı "suç" yazsa bile "Suç ve Ceza" kitabını bulabilir.
        if aranan.lower() in kitap["ad"].lower():

            print("\n========== ARAMA SONUCU ==========")
            print(f"Kitap Adı : {kitap['ad']}")
            print(f"Yazar     : {kitap['yazar']}")
            print(f"Sayfa     : {kitap['sayfa']}")
            print("----------------------------------")

            # Kitap bulunduğu için bulundu değişkenini True yapıyoruz.
            bulundu = True

    # Döngü bittikten sonra bulundu hala False ise kitap bulunamamış demektir.
    if bulundu == False:
        print("Aradığınız kitap bulunamadı.")


# Bu fonksiyon kitaplar listesinden kitap siler.
def kitap_sil():

    # Eğer listede hiç kitap yoksa silme işlemi yapılamaz.
    if len(kitaplar) == 0:
        print("Henüz kayıtlı kitap yok. Silme işlemi yapılamaz.")
        return

    silinecek_kitap = input("Silmek istediğiniz kitabın adını giriniz: ")

    # Başta silinecek kitabın bulunmadığını kabul ediyoruz.
    bulundu = False

    # Kitaplar listesindeki kitapları tek tek kontrol ediyoruz.
    for kitap in kitaplar:

        # Kullanıcının yazdığı kitap adı ile listedeki kitap adı aynı mı diye bakıyoruz.
        if silinecek_kitap.lower() == kitap["ad"].lower():

            # Kitap bulunduysa listeden siliyoruz.
            kitaplar.remove(kitap)

            print(f"{kitap['ad']} adlı kitap başarıyla silindi.")

            # Kitap bulunduğu için bulundu değişkenini True yapıyoruz.
            bulundu = True

            # Kitabı bulup sildiğimiz için döngüyü durduruyoruz.
            break

    # Döngü bittikten sonra bulundu hala False ise kitap listede yok demektir.
    if bulundu == False:
        print("Silmek istediğiniz kitap bulunamadı.")


# Ana program döngüsü.
# Program kullanıcı çıkış yapana kadar çalışmaya devam eder.
while True:

    # Kullanıcıya menü gösteriyoruz.
    print('''
========== KÜTÜPHANE SİSTEMİ ==========

1. Kitap ekle
2. Kitapları listele
3. Kitap ara
4. Kitap sil
5. Çıkış    
''')

    # Kullanıcıdan seçim alıyoruz.
    secim = input("Seçim: ")

    if not secim.isdigit():
        print("Harf değil rakam giriniz.")
        continue

    if secim not in ["1", "2", "3", "4", "5"]:
        print("Hatalı seçim yaptınız. Lütfen 1 ile 5 arasında bir seçim yapınız.")
        continue

    # Kullanıcı 5 seçerse programdan çıkılır.
    if secim == "5":
        print("Programdan çıkış yapılıyor...")
        break

    # Kullanıcı 1 seçerse kitap ekleme fonksiyonu çalışır.
    elif secim == "1":
        kitap_ekle()

    # Kullanıcı 2 seçerse kitap listeleme fonksiyonu çalışır.
    elif secim == "2":
        kitaplari_listele()

    # Kullanıcı 3 seçerse kitap arama fonksiyonu çalışır.
    elif secim == "3":
        kitap_ara()

    # Kullanıcı 4 seçerse kitap silme fonksiyonu çalışır.
    elif secim == "4":
        kitap_sil()