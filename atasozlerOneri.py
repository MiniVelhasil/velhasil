    #Atasözleri text dosaysı açılacak 
    #3. sütundaki kelimelerle paragraftan seçilen kelimeler karşılaştırılacak
    #paragraftaki kelimeler listelenecek
    #stopwords temizlenecek
    #kökleri bulanacak
#ATASÖZÜ ÖNERİ SİSTEMİ
class AtasozleriOneri():

    def atasozleriListesi(self):
        anahtarKelimeler =[]
        atasozleri = open("data/atasozleritest.txt", "r", encoding="utf8")
        for line in atasozleri:
            self.atasozu.append(line.split(":")[0])
            self.atasozuAnlami.append(line.split(":")[1])
            self.atasozuListesi.append(line.split(":")[2].split(" "))
    
    def stopwordTemizle(self, text):
        return 
    
    def paragrafKarsilastir(self,text):
        i = 0
        for atasoz in self.atasozuListesi: 
            sonuc = list(set(text) & set(atasoz))
            #print(atasoz)
            if len(sonuc)>3:
                
                print("Bu metin için önerdiğmiz atasözü : ", self.atasozu[i])
                print("Atasözünün anlamı : ", self.atasozuAnlami[i])
            i+=1
    def __init__(self,):
        self.atasozu =[]
        self.atasozuAnlami=[]
        self.atasozuListesi  =[]
        self.atasozleriListesi()
        
