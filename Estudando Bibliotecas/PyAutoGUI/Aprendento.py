import pyautogui
import time

#Utilizando pyautogui.readthedocs.io/en/latest/ para aprender

larguraTela, alturatela = pyautogui.size() #para capturar Altura e larguca da tela

print(f'A largura é {larguraTela} e altura é {alturatela}')
print('')
time.sleep(1)

mouseX , mouseY = pyautogui.position() #pegar posição do mouse atraves da lina X(horizontal) e Y(vertical)

print('')
print(f'Posição do mouse no eixo X {mouseX} Posição do mouse no eixo Y {mouseY}')
time.sleep(1)
print('')

pyautogui.moveTo(500, 500) #Mover mouse para eixo X e Y especifico
print('')
time.sleep(1)

pyautogui.click()#para clicar

pyautogui.click(150, 179) #mover mouse e clicar na cordenada XY

# pyautogui.click('button.png') #ele procura e clica no objeto que tem o nome button.png na sua tela
time.sleep(1.5)
print('')

pyautogui.move(400, 0)#move 400 pixels para a direita da sua posição
pyautogui.doubleClick()#dar dois clicks com o mouse
pyautogui.moveTo(500 ,500, duration=2, tween=pyautogui.easeInOutQuad) #move o cursor do mouse até a cordenada levando dois segundos para fazer isso, tween=pyautogui.easeInOutQuad é para uma velocidade constante do cursor chama Easing / Tweening, easeInOutQuad faz começar devagar acelerar no meio e desacelerar no final.
time.sleep(1.5)
print('')

pyautogui.write('Hello World!', interval=0.25) #escreve hello world onde foi clickado no intervalo de 0.25 segundos
pyautogui.press('enter')#aperta tecla escrita
# time.sleep(1.5)
# print('')

with pyautogui.hold('shift'): #enquanto segura o shift
    pyautogui.press(['left', 'left', 'left', 'left']) #é pressionado a seta lest(esquerda) 4 vezes.
#O shift é solto automaicamente
with pyautogui.hold('ctrl'):
    pyautogui.press(['c', 'v'])
#texto para copiar

pyautogui.hotkey('crtl', 'c')#aperta as duas teclas porem ele solta o ctrl após pressiona-lo então só está funcionando como seguencia de teclas para apertar.

pyautogui.alert('automação finalizada!')#abre um pop-up com a mensagem inserida

time.sleep(5) #tempo para entrar no paint e testar
distance = 200 #escolhendo quantos pixels o mouse vai andar
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5) #move para direita
    distance -= 5 #cada volta diminui o loop de tamanho então 200 - 5 = 195
    pyautogui.drag(0, distance, duration=0.5)#move para baixo
    pyautogui.drag(-distance, 0, duration=0.5)#move para esquerda
    distance -= 5 #cada volta diminui o loop de tamanho então 195 - 5 = 190 até chegar a 0
    pyautogui.drag(0, -distance, duration=0.5)#move para cima