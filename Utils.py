import re
class utils():
    def removePunction(text):
        '''
            Döküman içerisindeki noktalama işaretlerini kaldırır.
            @param  string text : Döküman içeriği
            @return string      : Noktalama işaretleri kaldırılmış text
        '''


        from string import punctuation
        text = ''.join([c for c in text if c not in punctuation])

        return text

    def removePunctionEnd(text):
        '''
            Döküman içerisindeki noktalama işaretlerini kaldırır.
            @param  string text : Döküman içeriği
            @return string      : Noktalama işaretleri kaldırılmış text
        '''

        regex = r"(?<!\d)[.,;:?)(](?!\d)"

        result = re.sub(regex, "", kelime, 0)
        return result

        return text


    def replaceChars(text):
        '''
            Döküman içerisinde şapkalı kararkterleri eşleniği ile değiştirir.
            @param  string  text        : Döküman içeriği
            @param  dict    char_dict   : Değişim yapılacak anahtar ve değer sözlüğü
            @return string              : Karakterleri değiştirilmiş döküman içeriği
        '''



        text = re.sub(r"Â", "A", text)
        text = re.sub(r"â", "a", text)
        text = re.sub(r"Î", "I", text)
        text = re.sub(r"î", "ı", text)
        text = re.sub(r"Û", "U", text)
        text = re.sub(r"û", "u", text)

        return text


    def toLowercase(text):
        '''
            Dökümandaki tüm büyük harfleri küçük harf dönüştürür. Python lower() fonksiyonu I harfini
            i'ye dönüştürdüğü için bu işlem regex'le yapıldı. Diğer dönüşümler için python'un varsayılan
            lower() fonksiyonu kullanıldı.
            @param string text  : Döküman içeriği
            @return             : Tüm karakterleri küçük harfe dönüştürülmüş döküman içeriği
        '''

        print ('Tüm karakterler küçük harfe dönüştürülüyor ...')

        text = re.sub(r"I", "ı", text)
        text = text.lower()

        return text


    def removeNewLine(text):
        '''
            Dökümanda bulunan yeni satırları kaldırır. Dökümanda yeni satırlar silindiğinde alt satırdaki kelimeler,
            üst satırdaki kelimelerle birleştiği için. Yeni satır silinmesi işlemi; yeni satırların önce çift boşluğa
            dönüştürülüp, daha sonra çift boşlukşların tek boşluğa dönüştürülmesiyle yapılır.
            @param string text  : Döküman içeriği
            @return             : Dökümanda bulunun yeni satırların kaldırılmış hali
        '''


        text = re.sub(r"\n", "  ", text)
        text = re.sub(r"  ", " ", text)

        return text



    def removeUndesiredCharsFromText(text,alfabe ='ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz0123456789 '+'\n'):
        '''
            Döküman içinden alfabede olmayan karakterleri siler. Varsayılan alfabe Türkçe alfabedir.
            @param  string  text            : Döküman içeriği
            @param  string  alfabe          : Silinmeden kalması istenen karakter listesi
            @return string                  : İstenmeyen karakterlerin temizlendiği text dökümanı döndürür.
        '''

        print ('Belirtilen alfabede olmayan tüm karakterleri kaldırıyor ...')

        cleaned_text = ''
        for char in text:
            if char in alfabe:
                cleaned_text = cleaned_text + char

        return cleaned_text