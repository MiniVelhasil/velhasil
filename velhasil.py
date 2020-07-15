# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:30:58 2020

@author: halil
"""
import re
import listeler
from SpellChecker.SimpleSpellChecker import SimpleSpellChecker
from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram
from SpellChecker.NGramSpellChecker import NGramSpellChecker
from NGram.NoSmoothing import NoSmoothing

import time


class Velhasil():
    fsm = FsmMorphologicalAnalyzer("data/turkish_dictionary.txt", "data/turkish_misspellings.txt",
                                   "data/turkish_finite_state_machine.xml")
    nGram = NGram("data/ngram.txt")

    def __init__(self, text):

        paragraflar = self.paragrafAyir(text)

        self.kelimeSayici(text)

        self.searchfile = open("data/VERB_TS_Corpus_Frequency_List.txt", "r", encoding="utf8")
        self.simpleSpellChecker = SimpleSpellChecker(self.fsm)
        self.nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        self.nGramSpellChecker = NGramSpellChecker(self.fsm, self.nGram)
        self.simpleSpellChecker = SimpleSpellChecker(self.fsm)
        self.cumleBulucu(paragraflar)

    # Metindeki paragrafları Ayırmak için kullandığımız fonksiyonumuz
    def paragrafAyir(self, text):
        paragraflar = text.split("\n")
        self.paragrafSayisi = len(paragraflar)
        return paragraflar

    # Cümle sonu belirleme işleminde istisna olan kısaltmaları metin içinde bulup sonlarındaki noktalama işaretini kaldırıyoruz.
    def kisaltmaTemizle(self, text):
        kisaltList = listeler.kisaltList
        for kisaltma in kisaltList:
            text = text.replace(kisaltma, kisaltma+"*")
        return text

    # #Metindeki cümleleri ayırmak için kullandığımız fonksiyonumuz

    def cumleBulucu(self, paragraflar):
        sent2 = []
        for paraf in paragraflar:
            paraf = self.kisaltmaTemizle(paraf)
            sentence = re.compile("""(?<=['""a-zıüöşğç\""\]\)][\!\?\:\.\…\n\r\n\t])\s+(?=[""A-ZİÜÖŞĞÇ0-9\(\-\(\''\‘\““\""\[\+])""")

            sent = re.split(sentence, paraf)

            sent2.extend(sent)

        a =0
        for i in sent2:
            i = i.replace("*",'')
            sent2[a]= i
            a+=1
        self.cumleler = sent2
        self.cumleSayisi = len(self.cumleler)
        return self.cumleler

    # #Metin İçindeki Kelime Sayısını bulmak için kullandığımız fonksiyon
    def kelimeSayici(self, text):
        #İstatistik çıkarmak için satır boşluklarını ve çift başlukları siliyoruz.
        text = re.sub(r"\n", "  ", text)
        text = re.sub(r"  ", " ", text)
        # İstatistik çıkarmak için tüm metni küçük harfe dönüştürüyoruz.
        text = re.sub(r"I", "ı", text)
        text = text.lower()
        text
        kelimeler= text.split(" ")
        self.kelimesayisi = len(kelimeler)
        self.karaktersayisi = len(text)
        self.benzersizkaraktersayisi = len(set(text))
        self.benzersizkelimesayisi = len(sorted(list(set(kelimeler))))
        self.benzersizkelimeler=sorted(list(set(kelimeler)))

        return None


    # Gönderilen kelime içindeki noktalama işaretlerini temizler
    def noktalamaTemizleyicisi(self, kelime):
        # kelime= re.sub(r'[^\w\s]','',kelime)
        regex = r"(?<!\d)[.,;:?)(](?!\d)"

        result = re.sub(regex, "", kelime, 0)
        return result

    # #Uzun cümlelerin bölünmeye uygun olup olmadığını anlamak için kullandığımız fonksiyonumuz
    # @zamanHesapla
    def cumleBolucu(self, text):
        text = text.split(" ")
        for baglac in listeler.baglaclar:

            if baglac in text:
                index = text.index(baglac)

                oncekiKelime = self.noktalamaTemizleyicisi(text[index - 1]).lower()
                for line in self.searchfile:
                    # print(re.search(r'\b' + oncekiKelime.lower() + '\b', line.split(" ")))
                    print(str(line.split(" ")[1]))
                    print(oncekiKelime)
                    if re.search(r'\b' + oncekiKelime + r'\b', str(line.split(" ")[1])):
                        return True
                    else:
                        return False

    # Yazım kontrolü yapan metodlarımız
    def yazimKontrolu(self, cumle):
        # simpleSpellChecker = SimpleSpellChecker(self.fsm)

        return (self.simpleSpellChecker.spellCheck(Sentence(cumle)).toString())

    def NGramYazimKontrolu(self, cumle):

        return (self.nGramSpellChecker.spellCheck(Sentence(cumle)).toString())

    # Yazım yanlışı yapılmış kelime için kelime önerileri sunar

    def kelimeOneri(self, kelime):

        return (self.simpleSpellChecker.candidateList(Word(kelime)))
