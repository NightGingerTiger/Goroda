from tkinter import *
from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = 'ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round (results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nРегион/штат: {region}"
            else:
                return f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}"
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"

def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {coordinates}")

window = Tk()
window.title("Поиск координат города")
window.geometry("320x200")

key = '3a5258d829cd48c8a3a51b77e3caec8c'

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)  # Привязка события нажатия Enter

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите Поиск")
label.pack()

window.mainloop()