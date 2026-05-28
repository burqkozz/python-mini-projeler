# Girilen 3 notun ortalamasını hesaplar
def not_ortalama_hesaplama(not1, not2, not3):
    ortalama = (not1 + not2 + not3) / 3
    return ortalama


# Hesaplanan ortalamaya göre geçme veya kalma durumunu belirler
def durum(ortalama):
    if (ortalama >= 50):
        return ("Ortalamadan geçtiniz.")
    else:
        return ("Ortalamadan kaldınız.")
    

# Programın çalışmasını sağlayan ana döngü
while True:
    print(''' 
========== NOTUN ORTALAMA HESAPLAMA ==========
          ''')

    # Kullanıcıdan 3 adet not bilgisi alınır
    not1 = int(input("1. Notunuzu Giriniz: "))
    not2 = int(input("2. Notunuzu Giriniz: "))
    not3 = int(input("3. Notunuzu Giriniz: "))

    # Girilen notlar fonksiyona gönderilir ve ortalama hesaplanır
    ortalama = not_ortalama_hesaplama(not1, not2, not3)

    # Hesaplanan ortalama ekrana yazdırılır
    print(f"Notun Ortalaması: {ortalama:.2f}")

    # Ortalama durum fonksiyonuna gönderilir ve geçme/kalma sonucu yazdırılır
    print(f"Ortalamanın Durumu: {durum(ortalama)}")

    # İşlem bittikten sonra döngü sonlandırılır
    break