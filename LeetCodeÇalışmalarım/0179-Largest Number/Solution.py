class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        
        metin_sayilar = []
        for sayi in nums:
            metin_sayilar.append(str(sayi))        #Input: nums = [3,30,34,5,9]
                                                   #Output: "9534330"
        kac_sayi_var = len(metin_sayilar)       
        for i in range(kac_sayi_var):
            for j in range(i + 1, kac_sayi_var):
                
                ihtimal1 = metin_sayilar[i] + metin_sayilar[j]
                ihtimal2 = metin_sayilar[j] + metin_sayilar[i]
                
                if ihtimal2 > ihtimal1:
                    metin_sayilar[i], metin_sayilar[j] = metin_sayilar[j], metin_sayilar[i]
                    
        sonuc = "".join(metin_sayilar)          
        if sonuc[0] == "0":
            return "0"
            
        return sonuc