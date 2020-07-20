    #Atasözleri text dosaysı açılacak 
    #3. sütundaki kelimelerle paragraftan seçilen kelimeler karşılaştırılacak
    #paragraftaki kelimeler listelenecek
    #stopwords temizlenecek
    #kökleri bulanacak
    #ATASÖZÜ ÖNERİ SİSTEMİ

import velhasil
import Utils
class AtasozleriOneri():

    def atasozleriListesi(self):
        anahtarKelimeler =[]
        atasozleri = open("data/bilgiler.txt", "r", encoding="utf8")
        for line in atasozleri:
            self.atasozu.append(line.split(":")[0])
            self.atasozuAnlami.append(line.split(":")[1])
            self.atasozuListesi.append(line.split(":")[2].split(", "))

    
    def stopwordTemizle(self, text):
        #Buna şimdilik gerek olmadığına kannat getirdim. Gerekirse eklenecek.
        return 
    
    def atasozuBul(self,text):
        i = 0
        ytext= []
        with open ("data/stopwords.txt", encoding="UTF-8") as f:
            stopwords = f.read ()
        for kelime in text:
            kelime = kelime.replace(" ","")
            kelime = Utils.utils.toLowercase(Utils.utils.removePunction(Utils.utils.removePunction(kelime)))
            if not (kelime in stopwords):
                ytext.append(kelime)
        print(ytext)
        for atasoz in self.atasozuListesi:
            sonuc = list(set(ytext) & set(atasoz))
            #print(atasoz)
            #print(sonuc)
            if len(sonuc)>5:
                print (sonuc)
                print(self.atasozu[i]+" : "+self.atasozuAnlami[i])
               #print("Atasözünün anlamı : ", self.atasozuAnlami[i])
            i+=1

    def __init__(self,):

        self.atasozu =[]
        self.atasozuAnlami=[]
        self.atasozuListesi  =[]
        self.atasozleriListesi()
        
