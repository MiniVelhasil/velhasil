    #ATASÖZÜ ÖNERİ SİSTEMİ

import Utils
class AtasozleriOneri():

    def atasozleriListesi(self):


        for line in self.atasozleri:
            self.atasozu.append(line.split(":")[0])
            self.atasozuAnlami.append(line.split(":")[1])
            self.atasozuListesi.append(line.split(":")[2].split(", "))

    def atasozuBul(self,text):
        i = 0
        ytext= []
        text = text.split(" ")
        with open ("data/stopwords.txt", encoding="UTF-8") as f:
            stopwords = f.read ()
        for kelime in text:
            kelime = Utils.utils.removeNewLine (kelime)
            kelime = kelime.replace(" ","")
            #kelime = Utils.utils.removeNewLine(kelime)
            kelime = Utils.utils.toLowercase(Utils.utils.removePunction(Utils.utils.removePunctionEnd(kelime)))
            if not (kelime in stopwords):
                ytext.append(kelime)
        #print(ytext)
        for atasoz in self.atasozuListesi:
            sonuc = list(set(ytext) & set(atasoz))
            #print(atasoz)

            if len(sonuc)>=5:
                self.atasozuOnerileri.append(str(len(sonuc))+ " : " + self.atasozu[i]+" : "+self.atasozuAnlami[i]) #print (sonuc)
                #print (sonuc)
               #print("Atasözünün anlamı : ", self.atasozuAnlami[i])

            i+=1
        return self.atasozuOnerileri
    def __init__(self,):
        self.atasozleri = open ("data/atasozleri.txt", "r", encoding="utf8")
        self.atasozu =[]
        self.atasozuAnlami=[]
        self.atasozuListesi  =[]
        self.atasozuOnerileri=[]
        self.atasozleriListesi()
        
