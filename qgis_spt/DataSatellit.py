class DataSatellit():
    # def landsat7(self): 
    #         L_TIR1_K1_L7 = "666.09"
    #         L_TIR1_K2_L7 = "1282.71"
    #         L_TIR1_LMAX_L7 = "17.04"
    #         L_TIR1_LMIN_L7 = "0"
    #         L_TIR1_QCALMAX_L7 = "255"
    #         L_TIR1_QCALMIN_L7 = "1"

    #         L_TIR2_K1_L7 = "666.09"
    #         L_TIR2_K2_L7 = "1282.71"
    #         L_TIR1_LMAX_L7 = "17.04"
    #         L_TIR1_LMIN_L7 = "0"
    #         L_TIR1_QCALMAX_L7 = "255"
    #         L_TIR1_QCALMIN_L7 = "1"
    #         return L_TIR1_K1, L_TIR1_K2, L_TIR1_RMULT, L_TIR1_RADD, L_TIR2_K1, L_TIR2_K2, L_TIR2_RMULT, L_TIR2_RADD

    def landsat8(self): 
            L_TIR1_K1 = "774.8853"
            L_TIR1_K2 = "1321.0789"
            L_TIR1_RMULT = "0.0003342"
            L_TIR1_RADD = "0.1"
            L_TIR2_K1 = "480.8883"
            L_TIR2_K2 = "1201.1442"
            L_TIR2_RMULT = "0.0003342"
            L_TIR2_RADD = "0.1"
            return L_TIR1_K1, L_TIR1_K2, L_TIR1_RMULT, L_TIR1_RADD, L_TIR2_K1, L_TIR2_K2, L_TIR2_RMULT, L_TIR2_RADD
