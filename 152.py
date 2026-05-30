from tkinter import *
import requests
import json

root = Tk()
root['bg'] = '#c5c5c5'
root.title('Достопримечательности СПб')
root.geometry('640x480')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.3)

placeField = Entry(frame_top, bg='white', font=30)
placeField.pack()

info = Label(frame_bottom, text='Введи достопримечательность', bg='red', font=12, wraplength=400, justify=LEFT)
info.pack()

def get_fact():
    name = placeField.get()
    if not name:
        info['text'] = 'Введи название!'
        return
    
    try:
        url = f'https://ru.wikipedia.org/api/rest_v1/page/summary/{name}'
        headers = {'User-Agent': 'MyApp/1.0'}
        r = requests.get(url, headers=headers)
        
        if r.status_code == 200:
            data = r.json()
            fact = data.get('extract', 'нет описания')
            if len(fact) > 500:
                fact = fact[:500] + '...'
            info['text'] = f'{name}:\n{fact}'
        else:
            info['text'] = f'Не найдено (ошибка {r.status_code})'
            
    except:
        info['text'] = 'Ошибка: проверь интернет'

btn = Button(frame_top, text='Узнать', bg='yellow', command=get_fact)
btn.pack()

root.mainloop()