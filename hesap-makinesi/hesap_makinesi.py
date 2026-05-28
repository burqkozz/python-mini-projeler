# İki sayıyı toplar ve sonucu geri döndürür
def toplama(x,y):
    return (x+y)


# İki sayı arasında çıkarma işlemi yapar ve sonucu geri döndürür
def çıkarma(x,y):
    return (x-y)


# İki sayıyı çarpar ve sonucu geri döndürür
def çarpma(x,y):
    return (x*y)


# Birinci sayıyı ikinci sayıya böler ve sonucu geri döndürür
def bölme(x,y):
    return (x/y)





# Programın sürekli çalışmasını sağlayan ana döngü
while True:

        # Kullanıcıya hesap makinesi menüsünü gösterir
        print('''
=============== HESAP MAKİNESİ ===============
1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Çıkış
==============================================
''')
        
        # Kullanıcıdan yapmak istediği işlem numarasını alır
        çıktıı=input("Hangi işlemi yapmak istiyorusunuz: ") 

        # Kullanıcının harf yerine rakam girip girmediğini kontrol eder
        if not çıktıı.isdigit():
            print("Harf değil rakam giriniz.")
            continue

        # Kullanıcının 1 ile 5 arasında seçim yapmasını kontrol eder
        if çıktıı not in ["1", "2", "3", "4", "5"]:
            print("Yanlış seçim 1 le 5 arasında seçim yapınız.")
            continue

        # Kullanıcı 5 seçerse uygulamadan çıkılır
        if (çıktıı == "5"):
            print("Uygulamadan çıkış yapılıyor...")
            break

        # Kullanıcıdan birinci sayıyı alır
        result=input("1.sayıyı giriniz: ")

        # Birinci sayının rakam olup olmadığını kontrol eder
        if not result.isdigit():
            print("Harf değil pozitif sayı giriniz.")
            continue

        # Kullanıcıdan ikinci sayıyı alır
        result2=input("2. Sayıyı giriniz: ")

        # İkinci sayının rakam olup olmadığını kontrol eder
        if not result2.isdigit():
            print("Harf değil pozitif sayı giriniz.")
            continue
        
        # input ile alınan değerleri metinden sayıya çevirir
        result = int(result)
        result2 = int(result2)
        
        # Kullanıcı 1 seçerse toplama işlemi yapılır
        if (çıktıı == "1"):
            sonuc = toplama(result , result2)
            print(f"Toplamanın Sonucu: {sonuc}")

        # Kullanıcı 2 seçerse çıkarma işlemi yapılır
        elif (çıktıı == "2"):
            sonuc = çıkarma(result , result2)
            print(f"Çıkarmanın sonucu: {sonuc}")

        # Kullanıcı 3 seçerse çarpma işlemi yapılır
        elif (çıktıı == "3"):
            sonuc = çarpma(result , result2)
            print(f"Çarpmanın Sonucu: {sonuc}")

        # Kullanıcı 4 seçerse bölme işlemi yapılır
        elif (çıktıı == "4"):
            sonuc = bölme(result , result2)
            print(f"Bölümün Sonucu: {sonuc:.1f}")