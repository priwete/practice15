from tkinter import *
import requests
root = Tk()
root['bg'] = '#c5c5c5'
root.title('Погода')
root.geometry('640x480')
root.resizable(width=False, height=False)
frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()
info = Label(frame_bottom, text='Погода в городе', bg='red', font=40)
info.pack()
def get_weather():
    city = cityField.get()
    key = 'aca3ae2786078810bf7ea4b7c508d515'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
btn = Button(frame_top, text='Проверить', bg='yellow', command=get_weather)
btn.pack()
root.mainloop()