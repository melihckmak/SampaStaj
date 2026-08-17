class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sonuc = []
        eleman_sayisi = len(nums)
        
        for i in range(eleman_sayisi):
            for j in range(i + 1, eleman_sayisi):
                for k in range(j + 1, eleman_sayisi):
                    
                    if nums[i] + nums[j] + nums[k] == 0:
                        # Bu üç sayıyı küçükten büyüğe sıralayıp kontrol yapıyoruz.
                        yeni_uclu = sorted([nums[i], nums[j], nums[k]])
                        
                        if yeni_uclu not in sonuc:
                            sonuc.append(yeni_uclu)
                            
        return sonuc