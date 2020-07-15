class AtTransmittance():
    def calc(self, cb_attransmit, watervapor):
        self.cb_attransmit = cb_attransmit
        self.watervapor = watervapor

        if self.cb_attransmit == "1976US Standard":  # 0.5-3 W for band TIR-1 and TIR-2
            attransmit_watervapor1 = float(-0.01646) * (float(self.watervapor) * float(self.watervapor)) - float(0.04546) * float(self.watervapor) + float(0.9744)
            attransmit_watervapor2 = float(-0.01403) * (float(self.watervapor) * float(self.watervapor)) - float(0.09748) * float(self.watervapor) + float(0.9731)
            return attransmit_watervapor1, attransmit_watervapor2

        if self.cb_attransmit == "Mid-Lat. Summer":  # 0.5-3 W for band TIR-1 and TIR-2
            attransmit_watervapor1 = float(-0.1134) * float(self.watervapor) + float(1.0335)
            attransmit_watervapor2 = float(-0.1546) * float(self.watervapor) + float(1.0078)
            return attransmit_watervapor1, attransmit_watervapor2
