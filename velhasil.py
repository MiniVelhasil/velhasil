# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:30:58 2020

@author: halil
"""
import re
import listeler
import Utils
from SpellChecker.SimpleSpellChecker import SimpleSpellChecker
from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram
from SpellChecker.NGramSpellChecker import NGramSpellChecker
from NGram.NoSmoothing import NoSmoothing


class Velhasil ():

    nGram = NGram ("data/ngram.txt")

    def __init__(self, text=""):
        self.fsm = FsmMorphologicalAnalyzer ("data/turkish_dictionary.txt", "data/turkish_misspellings.txt",
                                             "data/turkish_finite_state_machine.xml")
        paragraflar = self.paragrafAyir (text)

        self.kelimeSayici (text)

        self.searchfile = open ("data/VERB_TS_Corpus_Frequency_List.txt", "r", encoding="utf8")
        self.simpleSpellChecker = SimpleSpellChecker (self.fsm)
        self.nGram.calculateNGramProbabilitiesSimple (NoSmoothing ())
        self.nGramSpellChecker = NGramSpellChecker (self.fsm, self.nGram)
        self.simpleSpellChecker = SimpleSpellChecker (self.fsm)
        self.cumleBulucu (paragraflar)
        self.turkceKelimeler = open ("data/kelimeler.txt", "r", encoding="utf8")

    # Metindeki paragrafları Ayırmak için kullandığımız fonksiyonumuz
    def paragrafAyir(self, text):
        paragraflar = text.split ("\n")
        self.paragrafSayisi = len (paragraflar)
        return paragraflar

    # Cümle sonu belirleme işleminde istisna olan kısaltmaları metin içinde bulup sonlarındaki noktalama işaretini kaldırıyoruz.
    def kisaltmaTemizle(self, text):
        kisaltList = listeler.kisaltList
        for kisaltma in kisaltList:
            text = text.replace (kisaltma, kisaltma + "*")
        return text

    # #Metindeki cümleleri ayırmak için kullandığımız fonksiyonumuz

    def cumleBulucu(self, paragraflar):
        sent2 = []
        for paraf in paragraflar:
            paraf = self.kisaltmaTemizle (paraf)
            sentence = re.compile (
                """(?<=['""a-zıüöşğç\""\]\)][\!\?\:\.\…\n\r\n\t])\s+(?=[""A-ZİÜÖŞĞÇ0-9\(\-\(\''\‘\““\""\[\+])""")

            sent = re.split (sentence, paraf)

            sent2.extend (sent)

        a = 0
        for i in sent2:
            i = i.replace ("*", '')
            sent2[a] = i
            a += 1
        self.cumleler = sent2
        self.cumleSayisi = len (self.cumleler)
        return self.cumleler

    # #Metin İçindeki Kelime Sayısını bulmak için kullandığımız fonksiyon
    def kelimeSayici(self, text):
        # İstatistik çıkarmak için satır boşluklarını ve çift başlukları siliyoruz.
        text = re.sub (r"\n", "  ", text)
        text = re.sub (r"  ", " ", text)
        # İstatistik çıkarmak için tüm metni küçük harfe dönüştürüyoruz.
        text = re.sub (r"I", "ı", text)
        text = Utils.utils.toLowercase (text)
        text = Utils.utils.removePunction (text)

        kelimeler = text.split (" ")
        self.kelimesayisi = len (kelimeler)
        self.karaktersayisi = len (text)
        self.benzersizkaraktersayisi = len (set (text))
        self.benzersizkelimesayisi = len (sorted (list (set (kelimeler))))
        self.benzersizkelimeler = sorted (list (set (kelimeler)))

        return None

    # Gönderilen kelime içindeki noktalama işaretlerini temizler
    def noktalamaTemizleyicisi(self, kelime):
        # kelime= re.sub(r'[^\w\s]','',kelime)
        regex = r"(?<!\d)[.,;:?)(](?!\d)"

        result = re.sub (regex, "", kelime, 0)
        return result

    # #Uzun cümlelerin bölünmeye uygun olup olmadığını anlamak için kullandığımız fonksiyonumuz
    # @zamanHesapla
    def cumleBolucu(self, text):
        kelimeler = text.split (" ")
        if len(kelimeler)>20:
            for baglac in listeler.baglaclar:
                if baglac in kelimeler:
                    index = kelimeler.index (baglac)
                    oncekiKelime = Utils.utils.removePunction (kelimeler[index - 1]).lower ()
                    for line in self.searchfile:
                        #print(re.search(r'\b' + oncekiKelime.lower() + '\b', line.split(" ")))
                        #print (str (line.split (" ")[1]))
                        #print (oncekiKelime)
                        result = re.findall ('\\b' + oncekiKelime + '\\b', str (line.split (" ")[1]))
                        #print(result)
                        if len(result)>0:
                            return 1
                    self.searchfile.seek(0)
        return 0

    def yazimDenetimi(self, text):
        '''
                    Metnin yazım kontrolünü yapar.
                    @param  string kelime : Metnin tamamı
                    @return list      : [0,1,2,3,4,5,6] biçiminde
                    0-> kelime doğru ;
                    1-> Kelime bir noktalama işareti Önündeki boşluk silinmeli
                    2-> kelime yanlış
                    3-> cümleden sonra (enter ile bitmiş) nokta koyulmalı.
                    4-> Noktalama işaretinden sonra boşluk bırakılmalı (merhana,dünya) uyarı verir (3,14) -doğru döndürür
                    5-> Noktadan sonra büyük harf gelmeli
                    6-> Kelime doğru ancak Türkçe kelime önerisi var
        '''
        sonuc = []
        kelimeler = []
        for paragraf in text.split ("\n"):
            sayi = len(paragraf.split (" "))
            for sayac, kelime in enumerate(paragraf.split (" ")):
                if sayac == sayi-1:
                    if kelime[-1]!=".":
                        gelen =3

                elif sayac == 0:
                    gelen = self.yazimDenetimiIslem (kelime, "")
                else:
                    gelen = self.yazimDenetimiIslem (kelime,paragraf.split (" ")[sayac-1])
                sonuc.append (gelen)
                # kelimeler.append(kelime)
        # print()
        return sonuc
    # Yazım kontrolü yapan metodlarımız
    def yazimDenetimiIslem(self, kelime,oncekiKelime=""):
        '''
            Kelimenin yazım kontrolünü yapar.
            @param  string kelime : kelimenin kendisi
            @return int      :
            0-> kelime doğru ;
            1-> Kelime bir noktalama işareti Önündeki boşluk silinmeli
            2-> kelime yanlış
            3-> cümleden sonra (enter ile bitmiş) nokta koyulmalı
            4-> Noktalama işaretinden sonra boşluk bırakılmalı (merhana,dünya) uyarı verecek (3,14) -doğru döndürecek
            5-> noktadan sonra büyük harf gelmeli
            6-> Kelime doğru ancak Türkçe kelime önerisi var
        '''

        #kelime kısaltma listesinde varsa doğrudur.
        if kelime in listeler.kisaltList:
            return 0

        noktalamaİsaretleri = [".", ",", "?", "!", "...", ":", "(", ")"]
        if  len(kelime)==1:
            if kelime in noktalamaİsaretleri:
                return 1 #Kelime Noktalama işaretidir. Burada yazım yanlışı var.


        if len(oncekiKelime)>=1:#kelimenin içindeki noktalama işaretlerine karışmıyoruz
            if oncekiKelime[-1] in [".", "?", "!", "...", ":"]:
                #print(sonrakiKelime)
                if not(kelime.istitle()):
                    return 5 #kelime büyük harfle başlamalı

        kelime = Utils.utils.removePunctionEnd(kelime)  #kelimenin başındaki ve sonundaki noktalama işaretlerini kaldırıypruz kelimenin içindeki noktalama işaretlerine karışmıyoruz

        #Kelimenin içinde noktalama işareti olup olmadığı kontrol ediliyor.
        #Eğer kelime içinde noktalama işareti varsa ve noktalama işaretinden önceki karakte sayı değilde uyarı verecek
        for i in noktalamaİsaretleri:
            if i in kelime:
                if not(kelime[kelime.index(i)-1].isnumeric()): #noktalama işaretinden önceki kelime numerik mi?
                    return 4

        if self.isCorrect(kelime):
            if len(self.turkcesiniOner(kelime))>0:
                return 6 #kelime doğru ancak türkçe önerileri var
            else:
                return 0 #Kelime doğrudur

        return 2 #Kelime yanlış yazılmıştır.



    def yazimKontrolu(self, cumle):
        # simpleSpellChecker = SimpleSpellChecker(self.fsm)

        return (self.simpleSpellChecker.spellCheck (Sentence (cumle)).toString ())

    def isCorrect(self,kelime: str) -> bool:
        fsmParses = self.fsm.morphologicalAnalysis (kelime)

        return fsmParses.size () != 0

    def NGramYazimKontrolu(self, cumle):

        return (self.nGramSpellChecker.spellCheck (Sentence (cumle)).toString ())

    # Yazım yanlışı yapılmış kelime için kelime önerileri sunar

    def kelimeOneri(self, kelime):

        return (self.simpleSpellChecker.candidateList (Word (kelime)))

    def turkcesiniOner(self, kelime):

        ilkKelime =[]
        kelime  = Utils.utils.toLowercase(kelime)
        kelime = Utils.utils.removePunction(kelime)

        for line in self.turkceKelimeler:
            aranan = str(line.split(":")[1])
            aranan = aranan.replace(" ","")
            if re.search (r'\b' + kelime + r'\b', aranan):
                ilkKelime.append(Utils.utils.removePunction(str(line.split (" ")[0])))

        self.turkceKelimeler.seek (0)
        return ilkKelime
