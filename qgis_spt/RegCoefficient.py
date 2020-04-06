class RegCoefficient():
    def getData(self, value): 
        self.value = value
        
        if self.value == "0 - 30":
            A10 = "-59.1391"
            B10 = "0.4213"
            A11 = "-63.3921"
            B11 = "0.4565"
            return A10, B10, A11, B11

        if self.value == "0 - 40":
            A10 = "-60.9196"
            B10 = "0.4276"
            A11 = "-65.2240"
            B11 = "0.4629"
            return A10, B10, A11, B11

        if self.value == "10 - 40":
            A10 = "-62.8065"
            B10 = "0.4338"
            A11 = "-67.1728"
            B11 = "0.4694"
            return A10, B10, A11, B11

        if self.value == "10 - 50":
            A10 = "-64.6081"
            B10 = "0.4399"
            A11 = "-69.0215"
            B11 = "0.4756"
            return A10, B10, A11, B11