class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        satır = len(matrix)   #Matris içindeki virgüllerle ayrılan listelerin uzunluğunu verir.    
        sütun = len(matrix[0])    
        ''' matrix = [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60],
            ]
        '''
        
        sol = 0
        sag = (satır * sütun) - 1
        
        while sol <= sag:
            orta = (sol + sag) // 2
            
            satir = orta // sütun
            sutun = orta % sütun
            
            orta_deger = matrix[satir][sutun]
            
           
            if orta_deger == target:
                return True
            elif orta_deger < target:
                sol = orta + 1
            else:
                sag = orta - 1
                
    
        return False
