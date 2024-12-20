import ctypes
import time
from datetime import datetime
import os

def suspender_computador():
    """
    Suspende el computador.
    """
    ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

# Define la hora en la que deseas suspender el computador
hora_suspender = "02:15"

while True:
    hora_actual = datetime.now().strftime("%H:%M")

    if hora_actual == hora_suspender:
        print("Suspendiendo el computador...")
        suspender_computador()
        break

    time.sleep(60)  # Revisa cada minuto
