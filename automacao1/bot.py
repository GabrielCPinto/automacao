import pandas as pd 
import time
import pyautogui as pg

pg.PAUSE = 0.5

def main():
    link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
    pg.press('win')
    pg.write('Google Chrome')
    pg.press('enter')
    pg.write(link)
    pg.press('enter')
    #email
    pg.click(x = -899, y = 406)
    pg.write('asd@gmail.com.br')
    #senha
    pg.press('tab')
    pg.write('asd')
    
    pg.press('tab')
    pg.press('enter')
    
    table = pd.read_csv('produtos.csv')
    
    
    
    
    for i in table.index:
        pg.press('home')
        pg.click(x = -778, y = 287)
        pg.write(table.loc[i, 'codigo'])
        pg.press('tab')
        pg.write(table.loc[i, 'marca'])
        pg.press('tab')
        pg.write(table.loc[i, 'tipo'])
        pg.press('tab')
        pg.write(str(table.loc[i, 'categoria']))
        pg.press('tab')
        pg.write(str(table.loc[i, 'preco_unitario']))
        pg.press('tab')
        pg.write(str(table.loc[i, 'custo']))
        pg.press('tab')
        obs = table.loc[i, 'obs']
        if pd.isna(obs):
            obs = ''
        else:
            obs = str(obs)
        pg.write(obs)
        pg.press('tab')
        pg.press('enter')
        
        
        
    
    #pg.hotkey('alt', 'f4')

if __name__ == '__main__':
    main()