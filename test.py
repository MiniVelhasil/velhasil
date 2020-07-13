import velhasil
import atasozlerOneri

with open('testmetin.txt', 'r', encoding="utf8") as myfile:
    text = myfile.read()

def main():
    velhasil_ = velhasil.Velhasil(text)
    
    #Gönderilen metinle ilgili istatistik bilgisi döndürür
    print(velhasil_.kelimesayisi)
    print(velhasil_.paragrafSayisi)
    print(velhasil_.cumleSayisi)
    

    #Cümlenin bölünüp bölünmeyeceğini önerisini "true" veya "false" olarak bildirir
    print(velhasil_.cumleBolucu(velhasil_.cumleler[0]))
    
    #Daha doğru yazım denetimi için önce noktalam İşaretlerini metinden temizliyoruz
    print(velhasil_.noktalamaTemizleyicisi("Ahmet'in."))

    #Metindeki ilk cümleyi yazım kontrolünden geçirip en doğru halini döndürür
    print(velhasil_.yazimKontrolu(velhasil_.cumleler[0]))
    
    #Metindeki ilk cümlenin ilk kelimesin ile ilgili yazım önerileri sunar
    print(velhasil_.kelimeOneri(velhasil_.cumleler[0].split(" ")[0]))

    #Atasözü öneri sistemi
    atasozleri_ = atasozlerOneri.AtasozleriOneri()
    atasozleri_.paragrafKarsilastir(text.split(" "))

if __name__ == '__main__':
    main()
