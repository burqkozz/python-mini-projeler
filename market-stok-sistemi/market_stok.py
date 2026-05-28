# Ürünleri saklamak için boş bir liste oluşturulur
ürünler=[]


# Kullanıcıdan ürün adı, fiyat ve stok bilgisi alıp listeye ekler
def urun_ekle():
    ürün = input("Ürünün adını giriniz: ")
    fiyat = input("Ürünün fiyatı nedir: ")
    stok = input("Kaç adet aldınız: ")

    # Ürün bilgileri sözlük yapısında tutulur
    urun= {
        "Ürün" : ürün,
        "Fiyatı" : fiyat,
        "Stok" : stok 
    }

    # Oluşturulan ürün sözlüğü ürünler listesine eklenir
    ürünler.append(urun)
    print("\nÜrün listeye eklendi. ")


# Listedeki tüm ürünleri ekrana yazdırır
def urun_listele():
    if len(ürünler) == 0:
        print("\nHenüz kayıtlı ürün yok.")
        return
    
    # Ürünleri sıra numarası ile birlikte listeler
    for sira,urun in enumerate(ürünler, start=1):
        print("========== MARKET LİSTESİ ==========")
        print(f"\n{sira}. Ürün Adı : {urun['Ürün']}")
        print(f"   Fiyatı   : {urun['Fiyatı']}")
        print(f"   Stok     : {urun['Stok']}")
    

# Kullanıcının girdiği ürün adına göre listede arama yapar
def urun_ara():
    if len(ürünler) == 0:
        print("Henüz listede ürün yok.")
        return
    
    arama=input("Aramak istediğiniz ürün adını giriniz: ")

    # Ürünün bulunup bulunmadığını kontrol etmek için kullanılır
    bulundu = False

    # Listedeki ürünleri tek tek kontrol eder
    for urun in ürünler:
        if arama.lower() in urun["Ürün"].lower():
            print("\n========== ARAMA SONUCU ==========")
            print(f"Ürün : {urun['Ürün']}")
            print(f"Fiyatı : {urun['Fiyatı']}")
            print(f"Stok : {urun['Stok']}")
            print("\n----------------------------------")
            
            bulundu = True

    # Ürün bulunamazsa kullanıcıya bilgi verir
    if bulundu == False :
        print("Aradığınız ürün bulunamadı.")


# Seçilen ürünün stok miktarını artırır
def urun_artır():
    if len(ürünler) == 0:
        print("Henüz listede ürün yok.")
        return
    
    eklenecek_ürün=input("Eklenecek olan ürünün adını giriniz: ")

    bulundu = False

    # Artırılacak ürünü listede arar
    for urun in ürünler:
        if eklenecek_ürün.lower() in urun["Ürün"].lower():

            # Kullanıcıdan eklenecek stok miktarını alır
            ekleme = int(input("Kaç adet daha ekliyceksiniz: "))

            # Eski stok ile yeni eklenen miktarı toplar
            toplam_ekleme= ekleme + int(urun["Stok"])

            # Ürünün birim fiyatını bulur
            fıyatını_bulma = int(urun["Fiyatı"]) / int(urun["Stok"])

            # Eklenen ürün miktarına göre toplam fiyatı günceller
            güncel_fiyat = (fıyatını_bulma * ekleme) + int(urun["Fiyatı"])
            print(f"\n{urun['Ürün']} ürününün stoğu güncellendi.")

            # Ürünün stok ve fiyat bilgisini günceller
            urun["Stok"] = toplam_ekleme
            urun["Fiyatı"] = güncel_fiyat

            print(f"Güncel stok sayısı: {urun['Stok']}")
            print(f"Güncel fiyatı: {urun['Fiyatı']:.2f}")

            bulundu = True

    if bulundu == False:
        print("\nAradığınız ürün bulunamadı. ")


# Seçilen ürünün stok miktarını azaltır
def urun_azalt():
    if len(ürünler) == 0:
        print("Henüz listede ürün yok.")
        return
    
    azaltılacak_ürün=input("\nStok azaltılacak ürün adını giriniz: ")
    bulundu = False

    # Azaltılacak ürünü listede arar
    for urun in ürünler:
        if azaltılacak_ürün.lower() in urun["Ürün"].lower():
            
            azaltma_miktarı = input("Kaç adet ürünü çıkarcaksınız: ")

            # Stoktan fazla ürün azaltılmasını engeller
            if int(azaltma_miktarı) > int(urun["Stok"]):
                print("\nStok miktarından fazla ürün azaltamazsınız.")
                
            else:
                # Ürünün birim fiyatını hesaplar
                fiyatını_bulma = int(urun["Fiyatı"]) / int(urun["Stok"])

                # Yeni stok miktarını hesaplar
                ürün_azaltma = int(urun["Stok"]) - int(azaltma_miktarı)

                # Yeni stok miktarına göre toplam fiyatı hesaplar
                ürün_azaltma_fiyatını_bulma = (ürün_azaltma * fiyatını_bulma) 

                # Ürün bilgilerini günceller
                urun["Stok"] = ürün_azaltma
                urun["Fiyatı"] = ürün_azaltma_fiyatını_bulma

                print(f"Güncel stok sayısı: {urun['Stok']}")
                print(f"Güncel fiyatı: {urun['Fiyatı']:.2f}")

                bulundu = True

    if bulundu == False:
        print("\nAradığınız ürün bulunamadı.")


# Kullanıcının seçtiği ürünü listeden siler
def urun_sil():
    if len(ürünler) == 0:
        print("Henüz listede ürün yok.")
        return
    
    silme = input("Silmek istediğiniz ürünün adını giriniz: ")

    bulundu = False

    # Silinecek ürünü listede arar
    for urun in ürünler:
        if silme.lower() in urun["Ürün"].lower():
            if silme == urun["Ürün"]:

                # Ürün bulunduysa listeden siler
                ürünler.remove(urun)
                print(f"{urun['Ürün']} adlı ürün başarılı şekilde silinde.")

                bulundu = True

    if bulundu == False:
        print("Aradığınız ürün bulunamadı.")


# Programın sürekli çalışmasını sağlayan ana menü döngüsü
while True:
    print('''
========== MARKET STOK LİSTESİ ==========
          
1. Ürün Ekle
2. Ürün Listele
3. Ürün Ara
4. Stok Artır
5. Stok Azalt
6. Ürün Sil
7. Çıkış
          
=========================================
''')
    
    # Kullanıcıdan menü seçimi alınır
    secim = input("Seçim: ")

    # Kullanıcının harf yerine rakam girip girmediğini kontrol eder
    if not secim.isdigit():
        print("Harf değil rakam olucak.")
        continue

    # Kullanıcının 1 ile 7 arasında seçim yapmasını kontrol eder
    if secim not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Hatalı seçim yaptınız 1 ile 7 arasında secim yapınız.")
        continue

    # Kullanıcı 7 seçerse çıkış mesajı verir
    if (secim == "7"):
        print("Çıkış yapılıyor...")
        break

    # Ürün ekleme fonksiyonunu çalıştırır
    elif (secim == "1"):
        urun_ekle()

    # Ürün listeleme fonksiyonunu çalıştırır
    elif (secim == "2"):
        urun_listele()

    # Ürün arama fonksiyonunu çalıştırır
    elif (secim == "3"):
        urun_ara()

    # Stok artırma fonksiyonunu çalıştırır
    elif (secim == "4"):
        urun_artır()

    # Stok azaltma fonksiyonunu çalıştırır
    elif (secim == "5"):
        urun_azalt()

    # Ürün silme fonksiyonunu çalıştırır
    elif (secim == "6"):
        urun_sil()