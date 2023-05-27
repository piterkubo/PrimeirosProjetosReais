# Servidor BKP Logtime Banco de Dados iglobal novo

import pyautogui as auto
import time
from datetime import date



# Abrindo o Postgree

auto.click(x=336, y=742)
time.sleep(6)


auto.click(x=106, y=142, clicks = 2)
time.sleep(2)



auto.click(x=102, y=158, clicks = 2)
time.sleep(2)




# Fazendo o backup do iglobal_teste


auto.click(x=727, y=554)
time.sleep(3)


auto.rightClick(x=125, y=220)
time.sleep(1)


auto.click(x=197, y=418)
time.sleep(1)






# Ajustando o caminho do backup

auto.click(x=714, y=189)
time.sleep(1)


auto.click(x=717, y=191)
time.sleep(1)


auto.click(x=451, y=218)
time.sleep(1)


auto.click(x=577, y=352, clicks = 2)
time.sleep(1)


auto.click(x=575, y=305)
time.sleep(1)


auto.press('delete')
time.sleep(1)


auto.click(x=584, y=544)
time.sleep(1)


date_atual = date.today()
data_ajustado =  date_atual.strftime('%d-%m-%y')

auto.write(data_ajustado)


auto.click(x=796, y=615)
time.sleep(1)



# Selecionando o (format)
auto.click(x=693, y=223)
time.sleep(0.5)

auto.click(x=492, y=248)
time.sleep(0.5)



# Digitando o 9 em (Compress Ratio)

auto.click(x=501, y=250)
auto.write('9')
time.sleep(0.5)



# Colocando postegree em (rolename) e clicando em backup

auto.click(x=484, y=313)
time.sleep(0.5)

auto.click(x=462, y=345)
time.sleep(0.5)

auto.click(x=652, y=544)
time.sleep(1800)



auto.click(x=654, y=546)
time.sleep(1)






# Fazendo o backup do banco Iglobal antigo

auto.rightClick(x=108, y=205)
time.sleep(1)

auto.click(x=178, y=401)
time.sleep(1)



auto.click(x=712, y=194)
time.sleep(1)


auto.click(x=454, y=215)
time.sleep(1)



auto.click(x=568, y=332, clicks = 2)
time.sleep(1)



auto.click(x=557, y=312)
time.sleep(1)


auto.press('delete')
time.sleep(1)


# Renomeando o arquivo de backup e salvando o nome

auto.click(x=595, y=541)

date_atual = date.today()
data_ajustado =  date_atual.strftime('%d-%m-%y')

auto.write(data_ajustado)

auto.click(x=796, y=615)
time.sleep(1)


# Selecionando o (format)
auto.click(x=502, y=228)
time.sleep(0.5)

auto.click(x=474, y=242)
time.sleep(0.5)



# Digitando o 9 em (Compress Ratio)

auto.click(x=479, y=259)

auto.write('9')
time.sleep(0.5)

# Colocando postegree em (rolename) e clicando em backup

auto.click(x=475, y=313)
time.sleep(0.5)

auto.click(x=487, y=342)
time.sleep(0.5)

auto.click(x=647, y=552)
time.sleep(0.5)

time.sleep(1)
