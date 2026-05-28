# Quiz uygulamasını başlatan fonksiyon
def quiz_başlat():

    # Sorular, seçenekler ve doğru cevaplar liste içinde sözlük yapısıyla tutulur
    sorular = [
        {
        "soru": "Python'da ekrana yazı yazdırmak için hangisi kullanılır?",
        "secenekler": ["A) input", "B) print", "C) int", "D) str"],
        "cevap": "B"
        },
        {
        "soru": "Python'da kullanıcıdan veri almak için hangi komut kullanılır?",
        "secenekler": ["A) input", "B) print", "C) float", "D) len"],
        "cevap": "A"
        },
        {
        "soru": "Python'da birden fazla veriyi sıralı şekilde tutmak için hangi yapı kullanılır?",
        "secenekler": ["A) if", "B) for", "C) list", "D) print"],
        "cevap": "C"
        }
    ]

    # Kullanıcının doğru ve yanlış cevap sayılarını tutar
    dogru = 0
    yanlış = 0

    # Sorular listesindeki her soruyu sırayla ekrana getirir
    for soru in sorular:
        print(soru["soru"])

        # Sorunun seçeneklerini alt alta yazdırır
        for secenek in soru["secenekler"]:
            print(secenek)
    
        # Kullanıcıdan cevap alır
        cevap_alma = input("\nCevabınız: ")
        
        # Kullanıcının geçerli bir şık girip girmediğini kontrol eder
        if cevap_alma not in ["a", "A", "b", "B", "c", "C", "d", "D",]:
            print("\nBöyle şıkkımız yok A , B, C ve D şıkları vardır. Bunların arasında işaretleyiniz. ")
            return
        
        # Kullanıcının küçük harf girmesi durumunda cevabı büyük harfe çevirir
        cevap_alma = cevap_alma.upper()

        # Kullanıcının cevabı doğru cevapla aynıysa doğru sayısını artırır
        if cevap_alma == soru["cevap"]:
            print("\nDoğru cevap!")
            dogru += 1

        # Cevap yanlışsa doğru cevabı gösterir ve yanlış sayısını artırır
        else:
            print(f"\nYanlış cevap. Doğru cevap: {soru['cevap']}")
            yanlış += 1

    # Quiz bittikten sonra sonuçları gösterir
    sonuc_göster(dogru, yanlış, len(sorular))


# Quiz sonunda doğru, yanlış, toplam soru ve puan bilgisini gösterir
def sonuc_göster(dogru, yanlış, toplam_soru):

    # Puanı 100 üzerinden hesaplar
    puan = dogru * 100 / toplam_soru

    print("\n========== SONUÇ ==========")
    print(f"Toplam soru : {toplam_soru}")
    print(f"Doğru       : {dogru}")
    print(f"Yanlış      : {yanlış}")
    print(f"Puan        : {puan:.2f}")
    

# Programın sürekli çalışmasını sağlayan ana menü döngüsü
while True:
    print('''========== MİNİ QUIZ UYGULAMASI ==========

1. Quize başla
2. Çıkış
''')
    
    # Kullanıcıdan menü seçimi alır
    secim = input("Seçim: ")

    # Kullanıcının rakam girip girmediğini kontrol eder
    if not secim.isdigit():
        print("Harf değil rakam giriniz.")
        continue

    # Kullanıcının sadece 1 veya 2 seçmesini sağlar
    if secim not in ["1", "2"]:
        print("Hatalı seçim numarası 1 ile 2 arasından seçim yapınız.")
        continue

    # Kullanıcı 2 seçerse uygulamadan çıkılır
    if (secim == "2"):
        print("Uygulamadan çıkış yapılıyor.")
        break

    # Kullanıcı 1 seçerse quiz başlatılır
    elif (secim == "1"):
        quiz_başlat()