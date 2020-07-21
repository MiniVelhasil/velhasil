import velhasil
import atasozlerOneri

with open ('data/haber.txt', 'r', encoding="utf8") as myfile:
    text = myfile.read ()


def main():
    velhasil_ = velhasil.Velhasil (text)

    # Gönderilen metinle ilgili istatistik bilgisi döndürür
    print ("*************Metin İstatistikleri************")
    print ("Kelime sayisi :", velhasil_.kelimesayisi)
    print ("benzersiz kelime sayisi :", velhasil_.benzersizkelimesayisi)
    print ("Karakter sayisi :", velhasil_.karaktersayisi)
    print ("Benzersiz karakter sayisi :", velhasil_.benzersizkaraktersayisi)
    print ("Paragraf sayisi :", velhasil_.paragrafSayisi)
    print ("Cümle sayisi :", velhasil_.cumleSayisi)
    print ("Kelimeler :", velhasil_.benzersizkelimeler)
    print ("**************************")

    # Cümlenin bölünüp bölünmeyeceğini önerisini "true" veya "false" olarak bildirir
    # print(velhasil_.cumleBolucu(velhasil_.cumleler[0]))
    #for count, i in enumerate(velhasil_.cumleler):
        #print (count,":",i)

    # Metindeki ilk cümleyi yazım kontrolünden geçirip en doğru halini döndürür
    # print(velhasil_.yazimKontrolu(velhasil_.cumleler[0]))
    # Metindeki ilk cümleyi yazım kontrolünden geçirip en doğru halini döndürür
    print (velhasil_.yazimKontrolu ("ortyaa "))
    print (velhasil_.turkcesiniOner ("artaya"))

    # Metindeki ilk cümlenin ilk kelimesin ile ilgili yazım önerileri sunar
    print (velhasil_.kelimeOneri ("ortyaa"))

    # Atasözü öneri sistemi
    atasozleri_ = atasozlerOneri.AtasozleriOneri ()
    oneriler = atasozleri_.atasozuBul (text)
    oneriler.sort(reverse=True)
    #benzerlik oranına göre sıralama yapıyoruz
    print(len(oneriler))
    #En benzer ilk 5 atasözü önerisini yazdırır
    for i in oneriler[0:5]:
        print(i)


if __name__ == '__main__':
    main ()

"""metni gönderdik.
1. adım paragrafları bul.
2. Cümleleleri ayır
3. kelimelere ayır
4. kelimeleri yazım denetimi kontrol et
5. paragrafın sonu nokta gibi işaretle bitmiyorsa uyar
6. noktalama işaretlerinin önünde boşluk varsa uyarı ver
7. bir kaç yüzyıl gibi sık kullanılan hatalı kalıplar için istisnalar yazılabilir
8. Cümlenin tamamı ve ya ilk harfleri büyük harfse başlık olarak algılanmalı ve sonunda nokta olma hatası göz ardı edilmeli"""
