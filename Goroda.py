from tkinter import *
from opencage.geocoder import OpenCageGeocode
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = 'ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round (results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlng={lng}"

            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {"coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nРегион/штат: {region}",
                        'map_url' : osm_url
                }
            else:
                return {"coordinates": f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nРегион/штат: {region}",
                        'map_url' : osm_url
                }
        else:
            return {"coordinates": "Город не найден", "map_url": None}
    except Exception as e:
        return {"coordinates": f"Ошибка: {e}", "map_url": None}

def show_coordinates(event=None):
    global map_url
    city = entry.get()
    result = get_coordinates(city, key)
    if isinstance(result, dict):
        label.config(text=f"Координаты города {city}:\n {result['coordinates']}")
        map_url = result['map_url']
    else:
        label.config(text=result)


def show_map():
    if map_url:
        webbrowser.open(map_url)

window = Tk()
window.title("Поиск координат города")
window.geometry("320x200")

key = '3a5258d829cd48c8a3a51b77e3caec8c'

map_url = None

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)  # Привязка события нажатия Enter

button = Button(text="Поиск координат", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите Поиск")
label.pack()

map_button = Button(text="Показать карту", command=show_map)
map_button.pack()

window.mainloop()