class Radio:
    ANO_DE_FABRICAÇÃO = None
    MARCA = None
    COR = None
    ESTADO = False
    FREQUÊNCIA_MIN = 88
    FREQUÊNCIA_MAX = 108
    VOLUME_MIN = 0
    VOLUME_MAX = 100


    def ligar_desligar(self):
        self.ESTADO = not self.ESTADO
    def ajustar_volume(self,VOLUME):
        if self.VOLUME_MIN < 100:
            self.VOLUME_MIN +=1
        if self.VOLUME_MAX > 0:
            self.VOLUME_MAX -=1
    def ajustar_frequencia(self,FREQUÊNCIA):
        if self.FREQUÊNCIA_MIN < 108:
            self.FREQUÊNCIA_MIN +=1
        if self.FREQUÊNCIA_MAX > 88:
            self.FREQUÊNCIA_MAX -=1
