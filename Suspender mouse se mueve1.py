import ctypes
import time
from datetime import datetime
from pynput import mouse

# Constantes necesarias para el apagado de pantalla
HWND_BROADCAST = 0xFFFF
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MONITOR_OFF = 2
MONITOR_ON = -1

# Variables de control para evitar reactivar con movimiento
screen_off = False

def apagar_pantalla():
    global screen_off
    screen_off = True
    ctypes.windll.user32.BlockInput(True)  # Bloquea el teclado y mouse temporalmente
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)

def encender_pantalla():
    global screen_off
    screen_off = False
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON)
    ctypes.windll.user32.BlockInput(False)  # Desbloquea teclado y mouse

def esperar_click():
    def on_click(x, y, button, pressed):
        if pressed:  # Solo responder al clic del mouse
            encender_pantalla()
            return False  # Detener el listener después del clic

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

# Define la hora en la que deseas apagar la pantalla
hora_apagar = "19:51"

while True:
    hora_actual = datetime.now().strftime("%H:%M")

    if hora_actual == hora_apagar:
        apagar_pantalla()
        esperar_click()  # Esperar hasta que el usuario haga clic para encender la pantalla
        break

    time.sleep(60)
