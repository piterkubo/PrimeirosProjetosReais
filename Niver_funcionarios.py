import pandas as pd
import win32com.client as win32
import pyautogui as auto
import pyperclip as pyper
import time

auto.hotkey('winleft','r')
time.sleep(0.5)

caminho = r'C:\Base_clientes\NIVER FUNCIONARIOS.xlsx'

pyper.copy(caminho)

auto.hotkey('ctrl','v')
time.sleep(0.5)

auto.press('enter')
time.sleep(3)

auto.hotkey('alt', 'F4')
time.sleep(0.5)

auto.press('enter')
time.sleep(0.5)

df = pd.read_excel(r'C:\Base_clientes\NIVER FUNCIONARIOS.xlsx')


dados_funcionarios = df.query('mes_admissao == mes_hoje and dia_admissao == dia_hoje')[['funcionarios', 'data_admissao' ,'tempo_casa']]

print(dados_funcionarios)

dados_funcionarios.to_excel(r'C:\Base_clientes\tabela_atualizada.xlsx')



outlook = win32.Dispatch('outlook.application')


email = outlook.CreateItem(0)

email.To = 'teste@teste.com.br'

email.Subject = 'Relação de tempo de casa dos funcionários'
email.HTMLBody = f'''

<p> Prezados ! </p>

<p> Segue no anexo, planilha dos aniversariantes de tempo de casa.</p>

<p> Qualquer esclarecimento, por gentileza entrar em contato.

<p> Atenciosamente </3>

'''

anexo = (r'C:\Base_clientes\tabela_atualizada.xlsx')

email.Attachments.Add(anexo)

email.Send()
