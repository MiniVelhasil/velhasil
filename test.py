import velhasil
import atasozlerOneri

with open ('data/haber.txt', 'r', encoding="utf-8") as myfile:
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
    cumleConuc =[]
    for cumle in velhasil_.cumleler:
        print(cumle)
        cumleConuc.append(velhasil_.cumleBolucu(cumle))
    print(len(cumleConuc))
    print(cumleConuc)
    #print(velhasil_.cumleBolucu(velhasil_.cumleler[0]))
    #for count, i in enumerate(velhasil_.cumleler):
        #print (count,":",i)
    print ("**************************")
    # Metindeki ilk cümleyi yazım kontrolünden geçirip en doğru halini döndürür
    # print(velhasil_.yazimKontrolu(velhasil_.cumleler[0]))
    # Metindeki ilk cümleyi yazım kontrolünden geçirip en doğru halini döndürür
    print ("kelime önerileri " ,velhasil_.yazimDenetimi (text))
    print ("**************************")
    print (velhasil_.turkcesiniOner ("dekoder"))
    print ("**************************")
    # Metindeki ilk cümlenin ilk kelimesin ile ilgili yazım önerileri sunar
    print ("kelime önerileri " ,velhasil_.kelimeOneri ("yalnış"))
    print ("**************************")
    # Atasözü öneri sistemi
    atasozleri_ = atasozlerOneri.AtasozleriOneri ()
    oneriler = atasozleri_.atasozuBul (text)
    oneriler.sort(reverse=True)
    #benzerlik oranına göre sıralama yapıyoruz
    #print(len(oneriler)) #önerilen atasözü sayısını gösterir.
    #En benzer ilk 10 atasözü önerisini yazdırır
    for i in oneriler[0:10]:
        print(i)


if __name__ == '__main__':
    main ()

