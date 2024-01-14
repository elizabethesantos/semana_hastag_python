import pyautogui
import time

pyautogui.PAUSE = 0.5

# Entrando no sistema 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)
# pagina login
pyautogui.click(x=2067, y=408)
pyautogui.write("eliza@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345@E")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


#importando base de dados
import pandas 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # clicando pagina formulario
    pyautogui.click(x=1998, y=295)

    # cadastro produtos

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca        
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo  
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria  
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco_unitario  
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo               
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("enter")
    pyautogui.scroll(5000)







 