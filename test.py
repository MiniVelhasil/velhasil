import velhasil
import atasozlerOneri

with open('testmetin.txt', 'r', encoding="utf8") as myfile:
    text = myfile.read()


def main():
    velhasil_ = velhasil.Velhasil(text)

    # Gönderilen metinle ilgili istatistik bilgisi döndürür
    print("*************Metin İstatistikleri************")
    print("Kelime sayisi :",velhasil_.kelimesayisi)
    print("benzersiz kelime sayisi :",velhasil_.benzersizkelimesayisi)
    print("Karakter sayisi :",velhasil_.karaktersayisi)
    print("Benzersiz karakter sayisi :",velhasil_.benzersizkaraktersayisi)
    print("Paragraf sayisi :",velhasil_.paragrafSayisi)
    print("Cümle sayisi :",velhasil_.cumleSayisi)
    print("Kelimeler :", velhasil_.benzersizkelimeler)
    print("**************************")

    # Cümlenin bölünüp bölünmeyeceğini önerisini "true" veya "false" olarak bildirir
    #print(velhasil_.cumleBolucu(velhasil_.cumleler[0]))
    print(velhasil_.cumleler[0])
    # Daha doğru yazım denetimi için önce noktalam İşaretlerini metinden temizliyoruz
    print(velhasil_.noktalamaTemizleyicisi("Ahmet'in."))

    # Metindeki ilk cümleyi yazım kontrolünden geçirip en doğru halini döndürür
    #print(velhasil_.yazimKontrolu(velhasil_.cumleler[0]))
    # Metindeki ilk cümleyi yazım kontrolünden geçirip en doğru halini döndürür
    print(velhasil_.yazimKontrolu("Mehmet'in"))

    # Metindeki ilk cümlenin ilk kelimesin ile ilgili yazım önerileri sunar
    print(velhasil_.kelimeOneri("Mehmet'in"))

    # Atasözü öneri sistemi
    atasozleri_ = atasozlerOneri.AtasozleriOneri()
    atasozleri_.atasozuBul(text.split(" "))


if __name__ == '__main__':
    main()

"""metni gönderdik.
1. adım paragrafları bul."""