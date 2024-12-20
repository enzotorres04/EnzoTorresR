import ctypes
import time
from datetime import datetime
import os

def apagar_computador():
    """
    Apaga el computador.
    """
    os.system("shutdown /s /t 1")  # /s para apagar, /t 1 para esperar 1 segundo

# Define la hora en la que deseas suspender el computador
hora_suspender = "02:15"

while True:
    hora_actual = datetime.now().strftime("%H:%M")

    if hora_actual == hora_suspender:
        print("Apagando el computador...")
        apagar_computador()
        break

    time.sleep(60)  # Revisa cada minuto
