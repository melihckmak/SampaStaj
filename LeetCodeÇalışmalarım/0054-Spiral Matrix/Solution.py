class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        listem = []
    
        if len(matrix) == 0:
            return listem
            
        satir_sayisi = len(matrix)
        sutun_sayisi = len(matrix[0])
        
        ust_duvar = 0
        alt_duvar = satir_sayisi - 1
        sol_duvar = 0
        sag_duvar = sutun_sayisi - 1
        
        while ust_duvar <= alt_duvar and sol_duvar <= sag_duvar:
        
            for i in range(sol_duvar, sag_duvar + 1):
                listem.append(matrix[ust_duvar][i])
            ust_duvar += 1
    
            for i in range(ust_duvar, alt_duvar + 1):
                listem.append(matrix[i][sag_duvar])
            sag_duvar -= 1
            
            
            if ust_duvar <= alt_duvar:
                for i in range(sag_duvar, sol_duvar - 1, -1):
                    listem.append(matrix[alt_duvar][i])

                alt_duvar -= 1
                
            if sol_duvar <= sag_duvar:
                for i in range(alt_duvar, ust_duvar - 1, -1):
                    listem.append(matrix[i][sol_duvar])
                sol_duvar += 1
                
        return listem