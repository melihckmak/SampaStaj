class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uzunluk = len(s)
        i = 0
        ana_liste = []
        max_uzunluk = 0
        en_buyuk_liste = [] 
        
        while uzunluk > i:  
            if s[i] not in ana_liste:
                ana_liste.append(s[i])  
                if len(ana_liste) > max_uzunluk:
                    max_uzunluk = len(ana_liste)
                    en_buyuk_liste = ana_liste       
            else:
                if len(ana_liste) > max_uzunluk:
                    max_uzunluk = len(ana_liste)
                    en_buyuk_liste = ana_liste

                bolme_noktasi = ana_liste.index(s[i])
                ana_liste = ana_liste[bolme_noktasi + 1:]
                ana_liste.append(s[i])  
            i += 1  
        return max_uzunluk
            
        print("En uzun alt dizenin boyutu: ", max_uzunluk)
        print("En uzun alt dize: ", "".join(en_buyuk_liste)) 
