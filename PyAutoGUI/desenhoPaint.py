#Abrir windows abrir o Paint e desenhar um quadrado
import pyautogui
import time

time.sleep(2)
pyautogui.hotkey('win')
pyautogui.write('paint', interval=0.5)
pyautogui.press('enter')
pyautogui.moveTo(882, 398, duration=1, tween=pyautogui.easeInOutQuad)

pixels = 400
while pixels > 0:
    pyautogui.drag(pixels, 0, duration=0.7)
    pyautogui.drag(0, pixels, duration=0.7)
    pyautogui.drag(-pixels, 0, duration=0.7)
    pyautogui.drag(0, -pixels, duration=0.7)
    pixels -= 400
