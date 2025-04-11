from test import Radio


radio1 = Radio()

ligar = radio1.ESTADO=True
ajusta_frequencia = radio1.ajustar_frequencia(104.1) #104.1
ajustar_volume = radio1.ajustar_volume(8) #8

print(radio1.ESTADO)
print(f"Volume mínimo: {radio1.VOLUME_MIN}\nVolume máximo: {radio1.VOLUME_MAX}")
print(f"Frequência mínima: {radio1.FREQUÊNCIA_MIN}\nFrequência máxima: {radio1.FREQUÊNCIA_MAX}")
desligar = radio1.ESTADO=False
print(radio1.ESTADO)
