import pyautogui 
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.click(x=125, y=746)  

time.sleep(2)

pyautogui.write("google")   
    
time.sleep(1)

pyautogui.press("enter")

time.sleep(3)

pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.click(x=545, y=403)

time.sleep(2)

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(4)

pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("Minha Senha")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv") 

time.sleep(2)

for linha in tabela.index:

    pyautogui.doubleClick(x=510, y=257)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))                           
   
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")                            
    pyautogui.press("enter") 
   
    time.sleep(2)

    pyautogui.scroll(5000)







